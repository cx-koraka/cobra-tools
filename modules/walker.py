import os
import time
import logging
from collections import Counter

from experimentals.convert_constants import write_mimes_dict, write_hashes_dict
from generated.formats.fgm.compounds.FgmHeader import FgmHeader
from generated.formats.ms2.enums.CollisionType import CollisionType
from generated.formats.ovl_base import OvlContext

from generated.formats.ms2 import Ms2File
from generated.formats.ovl import OvlFile
from generated.formats.ovl_base.versions import games
from ovl_util.mimes import Mime, Shader
from root_path import root_dir

# get this huge dict from fgm walker, use in ms2 walker
shader_map = {}


def walk_type(start_dir, extension=".ovl"):
	logging.info(f"Scanning {start_dir} for {extension} files")
	ret = []
	for root, dirs, files in os.walk(start_dir, topdown=False):
		for name in files:
			if name.lower().endswith(extension):
				ret.append(os.path.join(root, name))
	return ret


def generate_hash_table(gui, start_dir):
	hashes = {}
	if start_dir:
		start_time = time.time()
		# don't use internal data
		ovl_data = OvlFile()
		all_deps_exts = set()
		# these are the input for which hashes should be stored
		hash_exts = {'.enumnamer', '.lua', '.model2stream', '.particleatlas', '.prefab', '.specdef', '.tex'}
		# plain arrays without fields, np vectorized arrays with tuple of field names
		lists = {"mimes_name": (), "mimes_triplets": (), "mimes": ("mime_hash", "mime_version"), "files": ("pool_type", "set_pool_type")}

		valid_packages = ("GameMain", "Content")
		mimes = {}
		error_files = []
		ovl_files = walk_type(start_dir, extension=".ovl")
		of_max = len(ovl_files)
		for of_index, ovl_path in enumerate(ovl_files):
			# filter ovl files to only accept stock names, discard any usermade ovl that does not agree
			if not any(p in ovl_path for p in valid_packages):
				logging.warning(f"Ignoring usermade {ovl_path}")
				continue
			gui.update_progress(f"Hashing", value=of_index, vmax=of_max)
			try:
				# read ovl file
				new_hashes, new_exts = ovl_data.load(ovl_path, commands={"generate_hash_table": hash_exts})
				all_deps_exts.update(new_exts)
				for list_id, attribs in lists.items():
					array = getattr(ovl_data, list_id)
					if attribs:
						arrays = {att: array[att] for att in attribs}
					else:
						arrays = {list_id: array}
					exts = ovl_data.mimes_ext if "mimes" in list_id else ovl_data.files_ext
					for list_name, subarray in arrays.items():
						for ext, v in zip(exts, subarray):

							short_var = list_name.replace("mime_", "").replace("mimes_", "").replace("files_", "").replace("_type", "")
							if short_var == "triplets":
								v = [(t.a, t.b, t.c) for t in v]
							# if the value already exists, make sure it is indeed constant (for this version)
							if ext in mimes:
								v_old = getattr(mimes[ext], short_var)
								if v != v_old and v_old:
									logging.error(f"{list_name}.{short_var} is not constant for {ext}! ({v} vs. {v_old})")
							else:
								mimes[ext] = Mime("", 0, 0, [], 0, 0)
							setattr(mimes[ext], short_var, v)
				hashes.update(new_hashes)
			except:
				logging.exception(f"Reading {ovl_path} failed")
				error_files.append(ovl_path)
		if error_files:
			logging.error(f"{error_files} caused errors!")
		out_dir = get_output_dir(start_dir)
		# with open(os.path.join(out_dir, "hashes.json"), "w") as json_writer:
		# 	json.dump(hashes, json_writer, indent="\t", sort_keys=True)
		write_hashes_dict(os.path.join(out_dir, "hashes.py"), hashes)
		write_mimes_dict(os.path.join(out_dir, "mimes.py"), mimes)
		logging.info(f"Read {len(hashes)} hashes in {time.time() - start_time:.2f} seconds")
		logging.info(f"Formats used in dependencies: {[s.replace(':', '.') for s in sorted(all_deps_exts)]}")


def get_output_dir(start_dir):
	# try to find a matching game
	for game in reversed(games):
		if game.value in start_dir:
			out_dir = os.path.join(root_dir, "constants", game.value)
			break
	else:
		logging.warning(f"Could not find a matching game, storing results in /constants/")
		out_dir = os.path.join(root_dir, "constants")
	return out_dir


def bulk_test_models(gui, start_dir, walk_ovls=True, walk_models=True):
	errors = []
	if start_dir:
		export_dir = os.path.join(start_dir, "walker_export")

		ms2_data = Ms2File()
		if walk_ovls:
			bulk_extract_ovls(errors, export_dir, gui, start_dir, (".ms2",))

		# holds different types of flag - list of byte maps pairs
		type_dic = {}
		blend_modes = set()
		shaders = {}
		# for last_count
		last_counts = set()
		flags = set()
		flag_0 = set()
		flag_1 = set()
		scale_float = set()
		constraints_0 = set()
		constraints_1 = set()
		no_bones = set()
		mesh_collision = set()
		max_bones = -1
		max_bones_ms2 = None
		if walk_models:
			start_time = time.time()
			ms2_files = walk_type(export_dir, extension=".ms2")
			mf_max = len(ms2_files)
			for mf_index, ms2_path in enumerate(ms2_files):
				ms2_name = os.path.basename(ms2_path)
				gui.update_progress(f"Walking MS2 files: {ms2_name}", value=mf_index, vmax=mf_max)
				try:
					ms2_data.load(ms2_path, read_editable=True)
					for mdl2_name, model_info in zip(ms2_data.mdl_2_names, ms2_data.model_infos):
						for i, mat in enumerate(model_info.model.materials):
							blend_modes.add(mat.blend_mode)
							fgm = mat.name.lower()
							if shader_map:
								shader = shader_map[fgm]
								if mat.blend_mode not in shaders:
									shaders[mat.blend_mode] = set()
								shaders[mat.blend_mode].add(shader.lower())
						for i, wrapper in enumerate(model_info.model.meshes):
							mesh_id = f"{mdl2_name}[{i}] in {ms2_name}"
							mesh = wrapper.mesh
							if hasattr(wrapper.mesh, "vert_chunks"):
								for v in wrapper.mesh.vert_chunks:
									scale_float.add((v.pack_base, v.scale))
							if mesh.flag not in type_dic:
								type_dic[mesh.flag] = ([], [])
							type_dic[mesh.flag][0].append(mesh_id)
						# 	type_dic[model.flag][1].append((model.bytes_mean, model.bytes_max, model.bytes_min))
						last_counts.add(model_info.last_count)
						if model_info.bone_info:
							if model_info.bone_info.bone_count > max_bones:
								max_bones = model_info.bone_info.bone_count
								max_bones_ms2 = ms2_path
							if model_info.bone_info.joint_count:
								# if model_info.bone_info.joints.count_0:
								# 	constraints_0.add(ms2_path)
								# if model_info.bone_info.joints.count_1:
								# 	constraints_1.add(ms2_path)
								for j in model_info.bone_info.joints.joint_infos:
									for hit in j.hitchecks:
										flag_0.add(hit.flag_0)
										flag_1.add(hit.flag_1)
										if hit.dtype == CollisionType.MESH_COLLISION:
											mesh_collision.add(ms2_path)
						else:
							no_bones.add(ms2_path)
				except Exception as ex:
					logging.exception("Walking models errored")
					errors.append((ms2_path, ex))
		# report
		print(f"\nThe following {len(errors)} errors occured:")
		for file_path, ex in errors:
			print(file_path, str(ex))

		print("\nThe following type - map pairs were found:")
		# for flag, tup in sorted(type_dic.items()):
		# 	print(flag)
		# 	names, maps_list = tup
		# 	print("Some files:", list(sorted(set(names)))[:25])
		# 	print("num meshes", len(names))
		print(f"scale_float: {list(sorted(scale_float))}")
		print(f"last_counts: {last_counts}")
		print(f"flags: {flags}")
		print(f"flag_0: {flag_0}")
		print(f"flag_1: {flag_1}")
		print(f"constraints_0: {constraints_0}")
		print(f"constraints_1: {constraints_1}")
		print(f"no_bones: {no_bones}")
		print(f"mesh_collision: {mesh_collision}")
		print(f"Max bones: {max_bones} in {max_bones_ms2}")
		# print(f"blend_modes: {blend_modes}")
		if shader_map:
			print(f"shaders: {shaders}")
		msg = f"Loaded {mf_max} models {time.time() - start_time:.2f} seconds"
		logging.info(msg)
		gui.update_progress(msg, value=1, vmax=1)


def bulk_extract_ovls(errors, export_dir, gui, start_dir, only_types):
	# don't use internal data
	ovl_data = OvlFile()
	ovl_files = walk_type(start_dir, extension=".ovl")
	of_max = len(ovl_files)
	for of_index, ovl_path in enumerate(ovl_files):
		gui.update_progress(f"Walking OVL files: {os.path.basename(ovl_path)}", value=of_index, vmax=of_max)
		try:
			# read ovl file
			ovl_data.load(ovl_path, commands={"only_types": only_types})
			# create an output folder for it
			rel_p = os.path.relpath(ovl_path, start=start_dir)
			rel_d = os.path.splitext(rel_p)[0]
			out_dir = os.path.join(export_dir, rel_d)
			out_paths = ovl_data.extract(out_dir, only_types=only_types)
		except Exception as ex:
			logging.exception(f"OVL failed: {ovl_path}")
			errors.append((ovl_path, ex))


def get_fgm_values(gui, start_dir, walk_ovls=True, walk_fgms=True):
	errors = []
	if start_dir:
		export_dir = os.path.join(start_dir, "walker_export")
		if walk_ovls:
			bulk_extract_ovls(errors, export_dir, gui, start_dir, (".fgm",))
		shaders = {}
		# used to debug the mapping of blend modes in ms2 material slots to predict them
		fgm_to_shader = {}
		if walk_fgms:
			context = OvlContext()
			fgm_files = walk_type(export_dir, extension=".fgm")
			mf_max = len(fgm_files)
			for mf_index, fgm_path in enumerate(fgm_files):
				gui.update_progress(f"Walking FGM files", value=mf_index, vmax=mf_max)
				try:
					header = FgmHeader.from_xml_file(fgm_path, context)

					if header.shader_name not in shaders:
						# shaders[header.shader_name] = ([], {})
						shaders[header.shader_name] = Shader(set(), {})
					shader = shaders[header.shader_name]
					# for ms2 debugging
					# fgm_name = os.path.basename(fgm_path)
					# fgm_to_shader[os.path.splitext(fgm_name)[0].lower()] = header.shader_name
					for attrib, attrib_data in zip(header.attributes.data, header.value_foreach_attributes.data):
						val = tuple(attrib_data.value)
						if attrib.name not in shader.attributes:
							shader.attributes[attrib.name] = (int(attrib.dtype), [])
						shader.attributes[attrib.name][1].append(val)
					for texture in header.textures.data:
						shader.textures.add(texture.name)

				except Exception as ex:
					logging.exception(f"FGM failed: {fgm_path}")
					errors.append((fgm_path, ex))

		for shader_name, shader in shaders.items():
			# only keep the five most common for this shader
			for att, val in shader.attributes.items():
				shader.attributes[att] = (val[0], Counter(tuple(sorted(tup)) for tup in val[1]).most_common(5))

		# report
		if errors:
			print("\nThe following errors occurred:")
			for file_path, ex in errors:
				print(file_path, str(ex))

		out_dir = get_output_dir(start_dir)
		with open(os.path.join(out_dir, "shaders.py"), "w") as f:
			f.write("shaders = {\n")
			for shader_name, shader in sorted(shaders.items()):
				f.write(f"\t'{shader_name}': (\n")

				f.write("\t\t[\n")
				for tex_name in sorted(shader.textures):
					f.write(f"\t\t\t'{tex_name}',\n")
				f.write("\t\t],\n")
				f.write("\t\t{\n")
				for attr_name, attr in sorted(shader.attributes.items()):
					f.write(f"\t\t\t'{attr_name}': {attr},\n")
				f.write("\t\t}\n")
				f.write("\t),\n")
			f.write("}\n")
