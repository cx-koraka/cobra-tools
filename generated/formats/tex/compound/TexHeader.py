from generated.context import ContextReference


class TexHeader:

	"""
	Sized str entry of 8 or 16 bytes
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# ?
		self.zero_0 = 0

		# ?
		self.zero_1 = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.zero_0 = 0
		if not (self.context.version < 19):
			self.zero_1 = 0

	def read(self, stream):
		self.io_start = stream.tell()
		self.zero_0 = stream.read_uint64()
		if not (self.context.version < 19):
			self.zero_1 = stream.read_uint64()

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		stream.write_uint64(self.zero_0)
		if not (self.context.version < 19):
			stream.write_uint64(self.zero_1)

		self.io_size = stream.tell() - self.io_start

	def get_info_str(self):
		return f'TexHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* zero_0 = {self.zero_0.__repr__()}'
		s += f'\n	* zero_1 = {self.zero_1.__repr__()}'
		return s

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
