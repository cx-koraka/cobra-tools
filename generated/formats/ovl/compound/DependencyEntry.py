from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint
from generated.formats.ovl.compound.HeaderPointer import HeaderPointer


class DependencyEntry(BaseStruct):

	"""
	Description of dependency; links it to an entry from this archive
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# Hash of this dependency, for lookup in hash dict. Can be either external or internal.
		self.file_hash = 0

		# offset for extension into string name table
		self.offset = 0

		# index into ovl file table, points to the file entry where this dependency is used
		self.file_index = 0

		# pointer into flattened list of all archives' pools
		self.link_ptr = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		print(f'set_defaults {self.__class__.__name__}')
		self.file_hash = 0
		self.offset = 0
		self.file_index = 0
		self.link_ptr = HeaderPointer(self.context, 0, None)

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
		super().read_fields(stream, instance)
		instance.file_hash = stream.read_uint()
		instance.offset = stream.read_uint()
		instance.file_index = stream.read_uint()
		instance.link_ptr = HeaderPointer.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		stream.write_uint(instance.file_hash)
		stream.write_uint(instance.offset)
		stream.write_uint(instance.file_index)
		HeaderPointer.to_stream(stream, instance.link_ptr)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('file_hash', Uint, (0, None))
		yield ('offset', Uint, (0, None))
		yield ('file_index', Uint, (0, None))
		yield ('link_ptr', HeaderPointer, (0, None))

	def get_info_str(self, indent=0):
		return f'DependencyEntry [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* file_hash = {self.fmt_member(self.file_hash, indent+1)}'
		s += f'\n	* offset = {self.fmt_member(self.offset, indent+1)}'
		s += f'\n	* file_index = {self.fmt_member(self.file_index, indent+1)}'
		s += f'\n	* link_ptr = {self.fmt_member(self.link_ptr, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
