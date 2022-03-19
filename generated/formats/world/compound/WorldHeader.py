from generated.context import ContextReference
from generated.formats.ovl_base.compound.Pointer import Pointer


class WorldHeader:

	"""
	# NOTE, World struct in JWE1 has an extra pointer this import/export is not accounting for yet
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.world_type = 0
		self.asset_pkg_count = 0
		self.prefab_count = 0
		self.ptr_asset_pkg = Pointer(self.context, 0, None)
		self.ptr_lua = Pointer(self.context, 0, None)
		self.ptr_0 = Pointer(self.context, 0, None)
		self.ptr_1 = Pointer(self.context, 0, None)
		self.ptr_prefab = Pointer(self.context, 0, None)
		self.ptr_2 = Pointer(self.context, 0, None)
		self.ptr_3 = Pointer(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.world_type = 0
		self.asset_pkg_count = 0
		self.prefab_count = 0
		self.ptr_asset_pkg = Pointer(self.context, 0, None)
		self.ptr_lua = Pointer(self.context, 0, None)
		self.ptr_0 = Pointer(self.context, 0, None)
		self.ptr_1 = Pointer(self.context, 0, None)
		self.ptr_prefab = Pointer(self.context, 0, None)
		self.ptr_2 = Pointer(self.context, 0, None)
		self.ptr_3 = Pointer(self.context, 0, None)

	def read(self, stream):
		self.io_start = stream.tell()
		self.read_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		self.write_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	@classmethod
	def read_fields(cls, stream, instance):
		instance.world_type = stream.read_uint64()
		instance.ptr_asset_pkg = Pointer.from_stream(stream, instance.context, 0, None)
		instance.asset_pkg_count = stream.read_uint64()
		instance.ptr_lua = Pointer.from_stream(stream, instance.context, 0, None)
		instance.ptr_0 = Pointer.from_stream(stream, instance.context, 0, None)
		instance.ptr_1 = Pointer.from_stream(stream, instance.context, 0, None)
		instance.ptr_prefab = Pointer.from_stream(stream, instance.context, 0, None)
		instance.ptr_2 = Pointer.from_stream(stream, instance.context, 0, None)
		instance.prefab_count = stream.read_uint64()
		instance.ptr_3 = Pointer.from_stream(stream, instance.context, 0, None)
		instance.ptr_asset_pkg.arg = 0
		instance.ptr_lua.arg = 0
		instance.ptr_0.arg = 0
		instance.ptr_1.arg = 0
		instance.ptr_prefab.arg = 0
		instance.ptr_2.arg = 0
		instance.ptr_3.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_uint64(instance.world_type)
		Pointer.to_stream(stream, instance.ptr_asset_pkg)
		stream.write_uint64(instance.asset_pkg_count)
		Pointer.to_stream(stream, instance.ptr_lua)
		Pointer.to_stream(stream, instance.ptr_0)
		Pointer.to_stream(stream, instance.ptr_1)
		Pointer.to_stream(stream, instance.ptr_prefab)
		Pointer.to_stream(stream, instance.ptr_2)
		stream.write_uint64(instance.prefab_count)
		Pointer.to_stream(stream, instance.ptr_3)

	@classmethod
	def from_stream(cls, stream, context, arg=0, template=None):
		instance = cls(context, arg, template, set_default=False)
		instance.io_start = stream.tell()
		cls.read_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance

	@classmethod
	def to_stream(cls, stream, instance):
		instance.io_start = stream.tell()
		cls.write_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance

	def get_info_str(self):
		return f'WorldHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* world_type = {self.world_type.__repr__()}'
		s += f'\n	* ptr_asset_pkg = {self.ptr_asset_pkg.__repr__()}'
		s += f'\n	* asset_pkg_count = {self.asset_pkg_count.__repr__()}'
		s += f'\n	* ptr_lua = {self.ptr_lua.__repr__()}'
		s += f'\n	* ptr_0 = {self.ptr_0.__repr__()}'
		s += f'\n	* ptr_1 = {self.ptr_1.__repr__()}'
		s += f'\n	* ptr_prefab = {self.ptr_prefab.__repr__()}'
		s += f'\n	* ptr_2 = {self.ptr_2.__repr__()}'
		s += f'\n	* prefab_count = {self.prefab_count.__repr__()}'
		s += f'\n	* ptr_3 = {self.ptr_3.__repr__()}'
		return s

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
