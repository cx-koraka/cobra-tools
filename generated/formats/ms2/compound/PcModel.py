from generated.array import Array
from generated.context import ContextReference
from generated.formats.ms2.compound.FloatsY import FloatsY
from generated.formats.ms2.compound.LodInfo import LodInfo
from generated.formats.ms2.compound.LodInfoZT import LodInfoZT
from generated.formats.ms2.compound.MaterialName import MaterialName
from generated.formats.ms2.compound.MeshLink import MeshLink
from generated.formats.ms2.compound.PcModelData import PcModelData
from generated.formats.ms2.compound.SmartPadding import SmartPadding
from generated.formats.ms2.compound.ZTPreBones import ZTPreBones
from generated.formats.ms2.compound.ZtModelData import ZtModelData


class PcModel:

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# uses uint here, two uints elsewhere
		self.materials = Array((self.arg.num_materials), MaterialName, self.context, 0, None)
		self.lods = Array((self.arg.num_lods), LodInfoZT, self.context, 0, None)
		self.lods = Array((self.arg.num_lods), LodInfo, self.context, 0, None)
		self.objects = Array((self.arg.num_objects), MeshLink, self.context, 0, None)

		# pad to 8 bytes alignment
		self.padding = 0
		self.models = Array((self.arg.num_models), PcModelData, self.context, 0, None)
		self.models = Array((self.arg.num_models), ZtModelData, self.context, 0, None)
		self.ztuac_pre_bones = ZTPreBones(self.context, 0, None)

		# see if it is a flag for ztuac too, so might be totally wrong here
		self.floatsy = Array((self.arg.render_flag), FloatsY, self.context, 0, None)

		# sometimes 00 byte
		self.weird_padding = SmartPadding(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.materials = Array((self.arg.num_materials), MaterialName, self.context, 0, None)
		if self.context.version == 17:
			self.lods = Array((self.arg.num_lods), LodInfoZT, self.context, 0, None)
		if self.context.version == 18:
			self.lods = Array((self.arg.num_lods), LodInfo, self.context, 0, None)
		self.objects = Array((self.arg.num_objects), MeshLink, self.context, 0, None)
		if self.context.version == 17 and (self.arg.num_materials + self.arg.num_objects) % 2:
			self.padding = 0
		if self.context.version == 18:
			self.models = Array((self.arg.num_models), PcModelData, self.context, 0, None)
		if self.context.version == 17:
			self.models = Array((self.arg.num_models), ZtModelData, self.context, 0, None)
		if self.context.version == 17 and self.arg.last_count:
			self.ztuac_pre_bones = ZTPreBones(self.context, 0, None)
		self.floatsy = Array((self.arg.render_flag), FloatsY, self.context, 0, None)
		self.weird_padding = SmartPadding(self.context, 0, None)

	def read(self, stream):
		self.io_start = stream.tell()
		self.materials.read(stream, MaterialName, self.arg.num_materials, None)
		if self.context.version == 17:
			self.lods.read(stream, LodInfoZT, self.arg.num_lods, None)
		if self.context.version == 18:
			self.lods.read(stream, LodInfo, self.arg.num_lods, None)
		self.objects.read(stream, MeshLink, self.arg.num_objects, None)
		if self.context.version == 17 and (self.arg.num_materials + self.arg.num_objects) % 2:
			self.padding = stream.read_uint()
		if self.context.version == 18:
			self.models.read(stream, PcModelData, self.arg.num_models, None)
		if self.context.version == 17:
			self.models.read(stream, ZtModelData, self.arg.num_models, None)
		if self.context.version == 17 and self.arg.last_count:
			self.ztuac_pre_bones = stream.read_type(ZTPreBones, (self.context, 0, None))
		self.floatsy.read(stream, FloatsY, self.arg.render_flag, None)
		self.weird_padding = stream.read_type(SmartPadding, (self.context, 0, None))

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		self.materials.write(stream, MaterialName, self.arg.num_materials, None)
		if self.context.version == 17:
			self.lods.write(stream, LodInfoZT, self.arg.num_lods, None)
		if self.context.version == 18:
			self.lods.write(stream, LodInfo, self.arg.num_lods, None)
		self.objects.write(stream, MeshLink, self.arg.num_objects, None)
		if self.context.version == 17 and (self.arg.num_materials + self.arg.num_objects) % 2:
			stream.write_uint(self.padding)
		if self.context.version == 18:
			self.models.write(stream, PcModelData, self.arg.num_models, None)
		if self.context.version == 17:
			self.models.write(stream, ZtModelData, self.arg.num_models, None)
		if self.context.version == 17 and self.arg.last_count:
			stream.write_type(self.ztuac_pre_bones)
		self.floatsy.write(stream, FloatsY, self.arg.render_flag, None)
		stream.write_type(self.weird_padding)

		self.io_size = stream.tell() - self.io_start

	def get_info_str(self):
		return f'PcModel [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* materials = {self.materials.__repr__()}'
		s += f'\n	* lods = {self.lods.__repr__()}'
		s += f'\n	* objects = {self.objects.__repr__()}'
		s += f'\n	* padding = {self.padding.__repr__()}'
		s += f'\n	* models = {self.models.__repr__()}'
		s += f'\n	* ztuac_pre_bones = {self.ztuac_pre_bones.__repr__()}'
		s += f'\n	* floatsy = {self.floatsy.__repr__()}'
		s += f'\n	* weird_padding = {self.weird_padding.__repr__()}'
		return s

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
