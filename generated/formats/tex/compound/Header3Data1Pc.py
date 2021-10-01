from generated.context import ContextReference


class Header3Data1Pc:

	"""
	Data struct for headers of type 7
	"""

	context = ContextReference()

	def __init__(self, context, arg=None, template=None):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.width = 0
		self.height = 0

		# may be depth
		self.array_size = 0

		# num_mips
		self.num_mips = 0
		self.set_defaults()

	def set_defaults(self):
		self.width = 0
		self.height = 0
		self.array_size = 0
		self.num_mips = 0

	def read(self, stream):
		self.io_start = stream.tell()
		self.width = stream.read_ushort()
		self.height = stream.read_ushort()
		self.array_size = stream.read_ushort()
		self.num_mips = stream.read_ushort()

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		stream.write_ushort(self.width)
		stream.write_ushort(self.height)
		stream.write_ushort(self.array_size)
		stream.write_ushort(self.num_mips)

		self.io_size = stream.tell() - self.io_start

	def get_info_str(self):
		return f'Header3Data1Pc [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* width = {self.width.__repr__()}'
		s += f'\n	* height = {self.height.__repr__()}'
		s += f'\n	* array_size = {self.array_size.__repr__()}'
		s += f'\n	* num_mips = {self.num_mips.__repr__()}'
		return s

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
