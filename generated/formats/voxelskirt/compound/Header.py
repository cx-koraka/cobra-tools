from generated.context import ContextReference
from generated.formats.voxelskirt.bitfield.VersionInfo import VersionInfo
from generated.formats.voxelskirt.compound.FixedString import FixedString
from generated.formats.voxelskirt.compound.SizedStrData import SizedStrData


class Header:

	"""
	Found at the beginning of every OVL file
	"""

	context = ContextReference()

	def __init__(self, context, arg=None, template=None):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# 'VOXE'
		self.magic = FixedString(self.context, 4, None)

		# if 0x08 then 64bit, 0x01 for JWE, PZ, 0x08 for PC
		self.version_flag = 0

		# 0x12 = PC, 0x13 = JWE, PZ
		self.version = 0

		# endianness?, usually zero
		self.bitswap = 0

		# always = 1
		self.seventh_byte = 1

		# determines compression format (none, zlib or oodle) and apparently type of data (additional fields)
		self.user_version = VersionInfo()

		# always = 0
		self.info = SizedStrData(self.context, None, None)
		self.set_defaults()

	def set_defaults(self):
		self.magic = FixedString(self.context, 4, None)
		self.version_flag = 0
		self.version = 0
		self.bitswap = 0
		self.seventh_byte = 1
		self.user_version = VersionInfo()
		self.info = SizedStrData(self.context, None, None)

	def read(self, stream):
		self.io_start = stream.tell()
		self.magic = stream.read_type(FixedString, (self.context, 4, None))
		self.version_flag = stream.read_byte()
		self.context.version_flag = self.version_flag
		self.version = stream.read_byte()
		self.context.version = self.version
		self.bitswap = stream.read_byte()
		self.seventh_byte = stream.read_byte()
		self.user_version = stream.read_type(VersionInfo)
		self.context.user_version = self.user_version
		self.info = stream.read_type(SizedStrData, (self.context, None, None))

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		stream.write_type(self.magic)
		stream.write_byte(self.version_flag)
		self.context.version_flag = self.version_flag
		stream.write_byte(self.version)
		self.context.version = self.version
		stream.write_byte(self.bitswap)
		stream.write_byte(self.seventh_byte)
		stream.write_type(self.user_version)
		self.context.user_version = self.user_version
		stream.write_type(self.info)

		self.io_size = stream.tell() - self.io_start

	def get_info_str(self):
		return f'Header [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* magic = {self.magic.__repr__()}'
		s += f'\n	* version_flag = {self.version_flag.__repr__()}'
		s += f'\n	* version = {self.version.__repr__()}'
		s += f'\n	* bitswap = {self.bitswap.__repr__()}'
		s += f'\n	* seventh_byte = {self.seventh_byte.__repr__()}'
		s += f'\n	* user_version = {self.user_version.__repr__()}'
		s += f'\n	* info = {self.info.__repr__()}'
		return s

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
