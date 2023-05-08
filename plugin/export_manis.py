import logging
import random

import bpy
import mathutils

from generated.formats.manis import ManisFile
from generated.formats.manis.compounds.ManiBlock import ManiBlock
from generated.formats.ms2.compounds.packing_utils import pack_swizzle
from modules.formats.shared import djb2
from plugin.modules_export.armature import get_armature
from plugin.utils.transforms import ManisCorrector2


def pack(c_v, b_v, s):
	c_v.x, c_v.y, c_v.z = pack_swizzle([i / s for i in b_v])


def pack_int(c_v, b_v, s):
	c_v.x, c_v.y, c_v.z = pack_swizzle([int(round(i / s)) for i in b_v])


def get_max(list_of_b_vecs):
	return max(abs(c) for vec in list_of_b_vecs for c in vec)


def get_fcurves_by_type(group, dtype):
	return [fcurve for fcurve in group.channels if fcurve.data_path.endswith(dtype)]


def get_groups_for_type(b_action, dtype):
	out = {}
	for group in b_action.groups:
		# if group.name in bones_lut:
		fcurves = get_fcurves_by_type(group, dtype)
		if fcurves:
			out[group] = fcurves
	return out


def index_min_max(indices):
	if indices:
		return min(indices), max(indices)
	return -1, 0


def set_mani_info_counts(mani_info, b_action, bones_lut, m_dtype, b_dtype):
	groups = get_groups_for_type(b_action, b_dtype)
	count = len(groups)
	for s in (f"{m_dtype}_bone_count", f"{m_dtype}_bone_count_repeat", f"{m_dtype}_bone_count_related"):
		setattr(mani_info, s, count)
	indices = [bones_lut[group.name] for group in groups]
	for s, v in zip((f"{m_dtype}_bone_min", f"{m_dtype}_bone_max"), index_min_max(indices)):
		setattr(mani_info, s, v)
	return groups, indices


def update_key_indices(k, m_dtype, groups, indices, target_names):
	names = [group.name for group in groups]
	target_names.update(names)
	getattr(k, f"{m_dtype}_bones")[:] = names
	getattr(k, f"{m_dtype}_bones_p")[:] = indices
	getattr(k, f"{m_dtype}_bones_delta")[:] = [i for i, name in enumerate(names)]


# def get_bfb_matrix(bone):
# 	bind = correction_global.inverted() @ correction_local.inverted() @ bone.matrix_local @ correction_local
# 	if bone.parent:
# 		p_bind_restored = correction_global.inverted() @ correction_local.inverted() @ bone.parent.matrix_local @ correction_local
# 		bind = p_bind_restored.inverted() @ bind
#
# 	return bind.transposed()

def get_local_bone(bone):
	if bone.parent:
		return bone.parent.matrix_local.inverted() @ bone.matrix_local
	return bone.matrix_local


def save(filepath=""):
	scene = bpy.context.scene
	b_armature_ob = get_armature(scene)
	if not b_armature_ob:
		logging.warning(f"No armature was found in scene '{scene.name}' - did you delete it?")

	bones_data = {}
	for bone in b_armature_ob.data.bones:
		# bonerestmat = get_bfb_matrix(bone)
		bonerestmat = get_local_bone(bone)
		rest_trans, rest_rot, rest_scale = bonerestmat.decompose()
		print(rest_rot, rest_trans, bone.name)
		bones_data[bone.name] = rest_trans, rest_rot.to_matrix().to_4x4(), rest_scale
	# else:
	# 	# clear pose
	# 	for pbone in b_armature_ob.pose.bones:
	# 		pbone.matrix_basis = mathutils.Matrix()

	# corrector = Corrector(False)
	corrector = ManisCorrector2(False)
	mani = ManisFile()
	# hardcode for PZ for now
	mani.version = 260
	action_names = []
	target_names = set()
	bones_lut = {pose_bone.name: pose_bone["index"] for pose_bone in b_armature_ob.pose.bones}
	for b_action in bpy.data.actions:
		logging.info(f"Exporting {b_action.name}")
		action_names.append(b_action.name)
	mani.mani_count = len(action_names)
	mani.names[:] = action_names
	mani.reset_field("mani_infos")
	mani.reset_field("keys_buffer")
	for b_action, mani_info in zip(bpy.data.actions, mani.mani_infos):
		mani_info.frame_count = int(round(b_action.frame_range[1] - b_action.frame_range[0]))
		mani_info.duration = mani_info.frame_count / scene.render.fps
		mani_info.count_a = mani_info.count_b = 255
		mani_info.target_bone_count = len(b_armature_ob.pose.bones)
		pos_groups, pos_indices = set_mani_info_counts(mani_info, b_action, bones_lut, "pos", "location")
		ori_groups, ori_indices = set_mani_info_counts(mani_info, b_action, bones_lut, "ori", "quaternion")
		scl_groups, scl_indices = set_mani_info_counts(mani_info, b_action, bones_lut, "scl", "scale")
		floats = []
		mani_info.keys = ManiBlock(mani_info.context, mani_info)
		k = mani_info.keys
		update_key_indices(k, "pos", pos_groups, pos_indices, target_names)
		update_key_indices(k, "ori", ori_groups, ori_indices, target_names)
		update_key_indices(k, "scl", scl_groups, scl_indices, target_names)
		for bone_keys, group in zip(k.key_data.pos_bones, pos_groups):
			rest_trans, rest_rot, rest_scale = bones_data[group.name]
			fcurves = get_fcurves_by_type(group, "location")
			for frame_i, key in enumerate(bone_keys):
				v = mathutils.Matrix.Translation(mathutils.Vector([fcu.evaluate(frame_i) for fcu in fcurves]) + rest_trans)
				# v = v @ bone.matrix_local
				key.x, key.y, key.z = corrector.blender_bind_to_nif_bind(v).to_translation()
		for bone_keys, group in zip(k.key_data.ori_bones, ori_groups):
			rest_trans, rest_rot, rest_scale = bones_data[group.name]
			fcurves = get_fcurves_by_type(group, "quaternion")
			for frame_i, key in enumerate(bone_keys):
				q = mathutils.Quaternion([fcu.evaluate(frame_i) for fcu in fcurves]).to_matrix().to_4x4()
				# add local rest transform
				q = rest_rot @ q
				key.w, key.x, key.y, key.z = corrector.blender_bind_to_nif_bind(q).to_quaternion()
	# hard-code for now
	mani.header.names_size = 16
	mani.header.hash_block_size = len(target_names) * 4
	mani.reset_field("name_buffer")
	mani.name_buffer.bone_names[:] = sorted(target_names)
	mani.name_buffer.bone_hashes[:] = [djb2(name) for name in mani.name_buffer.bone_names]
	print(mani)
	mani.save(filepath)
	# # get selected curve b_ob
	# b_ob = bpy.context.object
	# b_cu = b_ob.data
	# if b_ob.type != "CURVE":
	# 	raise AttributeError(f"Can only export curve objects")
	# context = object()
	# # export the curve data
	# spl_root = SplRoot(context)
	# spline_data = SplData(context)
	# spl_root.spline_data.data = spline_data
	#
	# # get basic data from b_spline
	# b_spline = b_cu.splines[0]
	# spl_root.count = len(b_spline.bezier_points)
	# spl_root.length = b_spline.calc_length()
	#
	# pack(spline_data.offset, b_ob.location, 1.0)
	# spline_data.scale = get_max([bezier.co for bezier in b_spline.bezier_points]) / 32767
	# for bezier in b_spline.bezier_points:
	# 	key = Key(context)
	# 	spline_data.keys.append(key)
	# 	pack_int(key.pos, bezier.co, spline_data.scale)
	# 	left_rel = bezier.handle_left - bezier.co
	# 	right_rel = bezier.handle_right - bezier.co
	# 	key.handle_scale = get_max((left_rel, right_rel)) / 127
	# 	pack_int(key.handle_left, left_rel, key.handle_scale)
	# 	pack_int(key.handle_right, right_rel, key.handle_scale)
	#
	# with SplRoot.to_xml_file(spl_root, filepath) as xml_root:
	# 	pass
	return f"Finished manis export",
