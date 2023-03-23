import logging
import traceback

from generated.array import Array
from generated.formats.base.basic import Float
from generated.formats.base.compounds.PadAlign import get_padding_size, get_padding
from generated.formats.ms2.compounds.MeshCollisionData import MeshCollisionData
from generated.formats.ms2.versions import is_old
from generated.formats.ms2.compounds.MeshCollisionData import MeshCollisionData
from generated.formats.ms2.compounds.Model import Model
from generated.formats.ms2.compounds.BoneInfo import BoneInfo
from generated.formats.ms2.enums.CollisionType import CollisionType
from generated.base_struct import BaseStruct


from generated.base_struct import BaseStruct


class ModelReader(BaseStruct):

	"""
	This reads and assigns models to each model_info that is passed to it
	"""

	__name__ = 'ModelReader'

	_import_key = 'ms2.compounds.ModelReader'

	_attribute_list = BaseStruct._attribute_list + [
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)

	def __init__(self, context, arg=None, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.bone_infos = []
		self.bone_info_start = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		pass

	@classmethod
	def read_fields(cls, stream, instance):
		instance.io_start = stream.tell()
		instance.bone_infos = []
		logging.debug(f"ModelReader starts at {instance.io_start}")
		i = 0
		specials = []
		if instance.context.version < 47:
			# start = instance.io_start
			start = instance.arg.io_start
			# meh, add it here even though it's really interleaved
			instance.bone_info_start = stream.tell()
			for model_info in instance.arg:
				# logging.debug(model_info)
				s = stream.tell()
				try:
					model_info.model = Model.from_stream(stream, instance.context, model_info)
				except:
					logging.exception(f"Failed reading model for model_info {model_info}")
					# logging.warning(model_info.model)
				# this little patch solves reading all of PC anubis models
				if model_info.model.lods:
					if model_info.model.lods[0].distance != 900.0:
						logging.warning(f"Distance is wrong")
						stream.seek(s+8)
						specials.append(i)
						try:
							model_info.model = Model.from_stream(stream, instance.context, model_info)
						except:
							logging.exception(f"Failed reading model for model_info {model_info}")
				# logging.debug(f"Model {i} {model_info.model}")
				# alignment, not sure if really correct
				if model_info.increment_flag:
					model_info.model_padding = stream.read(get_padding_size(stream.tell() - start, alignment=16))
				else:
					model_info.model_padding = stream.read(get_padding_size(stream.tell() - start, alignment=8))
				# logging.debug(f"model padding {model_info.model_padding}")
				i = instance.assign_bone_info(i, model_info, stream)

		else:
			for model_info in instance.arg:
				# logging.debug(model_info)
				model_info.model = Model.from_stream(stream, instance.context, model_info)
				# logging.debug(f"Model {i} {model_info.model}")
			instance.bone_info_start = stream.tell()
			for model_info in instance.arg:
				try:
					i = instance.assign_bone_info(i, model_info, stream)
				except:
					traceback.print_exc()
					raise AttributeError(f"Bone info {i} failed")
		logging.info(f"Specials {specials}")
		instance.io_size = stream.tell() - instance.io_start

	def assign_bone_info(self, i, model_info, stream):
		if model_info.increment_flag:
			logging.debug(f"Reading bone info {i} at {stream.tell()}")
			try:
				model_info.bone_info = self.read_bone_info(stream, i)
				# logging.info(model_info.bone_info)
				# logging.debug(f"Bone info {i} worked {model_info.bone_info}")
				self.bone_infos.append(model_info.bone_info)
				# return
			except:
				logging.warning(f"Bone info {i} failed for model_info")
				logging.warning(model_info)
				logging.warning(model_info.model)
				logging.warning(f"here's the bone info before:")
				logging.warning(self.bone_infos[-1])
			i += 1
		else:
			logging.debug(f"Using previous bone info")
			if self.bone_infos:
				model_info.bone_info = self.bone_infos[-1]
			else:
				model_info.bone_info = None
		return i

	def get_hitchecks(self, bone_info):
		"""Collect all hitchecks in a flat list"""
		# need to handle bone infos that have no joints
		if hasattr(bone_info, "joints") and bone_info.joints:
			h = [hitcheck for joint in bone_info.joints.joint_infos for hitcheck in joint.hitchecks]
			return h
		return []

	def read_bone_info(self, stream, i):

		logging.debug(f"BONE INFO {i} starts at {stream.tell()}")
		# 22-05: in PC anubis, we do have padding here
		# there's never padding before the first bone info, and after the last
		# if not is_old(self.context) and i == 0:
		if (not is_old(self.context)) and i:
			self.get_padding(stream)
		bone_info = BoneInfo.from_stream(stream, self.context)
		# logging.info(bone_info)
		self.read_hitcheck_verts(bone_info, stream)
		logging.debug(f"end of bone info {i} at {stream.tell()}")

		# if bone_info.joints and is_old(self):
		# 	names_l = bone_info.joints.namespace_length
		# 	pad_l = len(bone_info.joints.joint_names_padding.data)
		# 	hits = sum(j.hitcheck_count for j in bone_info.joints.joint_infos_old)
		# 	logging.debug(f"names total len: {names_l + pad_l} names: {names_l} padding: {pad_l} hits: {hits} joints: {bone_info.joints.joint_count}")
		# 	if bone_info.joints.joint_infos_old:
		# 		j = bone_info.joints.joint_infos_old[0]
		# 		h = j.hitchecks[0]
		# 		for t, size in enumerate(
		# 				(h.io_start - self.buffer_1_offset,
		# 				h.io_start - bone_info.io_start,
		# 				h.io_start - bone_info.joints.io_start)
		# 			):
		# 			# any of those may not actually be padding
		# 			for elem in (range(pad_l)):
		# 				rel_size = size-elem
		# 				for al in (32, 40, 48, 64):
		# 					mod = rel_size % al
		# 					# logging.debug(f"rel_size: {rel_size} mod{al}: {mod}")
		# 					k = (t, elem, al)
		# 					# see if it modulos to 0
		# 					if not mod:
		# 						if k not in self.dic:
		# 							self.dic[k] = 0
		# 						self.dic[k] += 1
		return bone_info

	def get_padding(self, stream, alignment=16, rel=None):
		if rel is None:
			rel = self.bone_info_start
		abs_offset = stream.tell()
		relative_offset = abs_offset - rel
		# currently no other way to predict the padding, no correlation to joint count
		padding_len = get_padding_size(relative_offset, alignment=alignment)
		padding = stream.read(padding_len)
		if padding != b'\x00' * padding_len:
			# logging.warning(f"Padding is nonzero {padding} at offset {abs_offset}")
			raise AttributeError(f"Padding is nonzero {padding} at offset {abs_offset}")
		logging.debug(f"padding: {padding_len} aligned to {alignment}")

	def read_hitcheck_verts(self, bone_info, stream):
		try:
			start = stream.tell()
			logging.debug(f"Reading additional hitcheck data at {start}")
			for hitcheck in self.get_hitchecks(bone_info):
				if hitcheck.dtype in (CollisionType.CONVEX_HULL_P_C, CollisionType.CONVEX_HULL):
					# not aligned to 16!
					# self.get_padding(stream, alignment=16, rel=start)
					logging.debug(f"Reading vertices for {hitcheck.dtype.name} at {stream.tell()}")
					hitcheck.collider.vertices = Array.from_stream(stream, self.context, 0, None, (hitcheck.collider.vertex_count, 3), Float)
				if hitcheck.dtype in (CollisionType.MESH_COLLISION,):
					self.get_padding(stream, alignment=16, rel=start)
					logging.debug(f"Reading vertices for {hitcheck.dtype.name} at {stream.tell()}")
					hitcheck.collider.data = MeshCollisionData.from_stream(stream, self.context, hitcheck.collider, None)
		except:
			logging.exception(f"Reading hitchecks failed")

	def write_hitcheck_verts(self, bone_info, stream):
		logging.debug(f"Writing additional hitcheck data")
		for hitcheck in self.get_hitchecks(bone_info):
			if hitcheck.dtype in (CollisionType.CONVEX_HULL_P_C, CollisionType.CONVEX_HULL):
				logging.debug(f"Writing vertices for {hitcheck.dtype}")
				Array.to_stream(hitcheck.collider.vertices, stream, self.context, dtype=Float)

	@classmethod
	def write_fields(cls, stream, instance):
		instance.io_start = stream.tell()
		i = 0
		previous_bone_info = None
		if instance.context.version < 47:
			raise NotImplementedError("Can't write old style mesh and bone info blocks")
		else:
			for model_info in instance.arg:
				model_info.model.to_stream(model_info.model, stream, instance.context)
			instance.bone_info_start = stream.tell()
			for model_info in instance.arg:
				# check if they have a different bone info
				if previous_bone_info is not model_info.bone_info:
					logging.debug(f"{model_info.name} has its own bone_info")
					model_info.increment_flag = 1
					logging.debug(f"BONE INFO {i} starts at {stream.tell()}")
					model_info.bone_info.to_stream(model_info.bone_info, stream, instance.context)
					instance.write_hitcheck_verts(model_info.bone_info, stream)
					# PZ lion needs padding after last boneinfo, crashes if missing, adding probably won't hurt other cases
					# if i + 1 < len(instance.bone_infos):
					relative_offset = stream.tell() - instance.bone_info_start
					padding = get_padding(relative_offset)
					logging.debug(f"Writing padding {padding}")
					stream.write(padding)
					i += 1
				else:
					logging.debug(f"{model_info.name} reuses previous bone_info")
					model_info.increment_flag = 0
				previous_bone_info = model_info.bone_info
			instance.bone_info_size = stream.tell() - instance.bone_info_start
		instance.io_size = stream.tell() - instance.io_start

	@classmethod
	def get_fields_str(cls, instance, indent=0):
		s = ''
		for model_info in instance.arg:
			s += str(model_info.model)
			s += str(model_info.bone_info)
		return s

