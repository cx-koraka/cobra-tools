class Header3Data1:

	"""
	Part of a fragment, repeated for count of texture LODs / buffers.
	Data struct for headers of type 3
	24 bytes per texture buffer
	"""

	# Size of previous tex buffer
	data_size_previous: int
	zero_1: int

	# Size of this tex buffer
	data_size: int
	zero_3: int

	# is also related to data size
	unkn: int
	zero_5: int

	def __init__(self, arg=None, template=None):
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.data_size_previous = 0
		self.zero_1 = 0
		self.data_size = 0
		self.zero_3 = 0
		self.unkn = 0
		self.zero_5 = 0

	def read(self, stream):

		io_start = stream.tell()
		self.data_size_previous = stream.read_uint()
		self.zero_1 = stream.read_uint()
		self.data_size = stream.read_uint()
		self.zero_3 = stream.read_uint()
		self.unkn = stream.read_uint()
		self.zero_5 = stream.read_uint()

		self.io_size = stream.tell() - io_start

	def write(self, stream):

		io_start = stream.tell()
		stream.write_uint(self.data_size_previous)
		stream.write_uint(self.zero_1)
		stream.write_uint(self.data_size)
		stream.write_uint(self.zero_3)
		stream.write_uint(self.unkn)
		stream.write_uint(self.zero_5)

		self.io_size = stream.tell() - io_start

	def __repr__(self):
		s = 'Header3Data1 [Size: '+str(self.io_size)+']'
		s += '\n	* data_size_previous = ' + self.data_size_previous.__repr__()
		s += '\n	* zero_1 = ' + self.zero_1.__repr__()
		s += '\n	* data_size = ' + self.data_size.__repr__()
		s += '\n	* zero_3 = ' + self.zero_3.__repr__()
		s += '\n	* unkn = ' + self.unkn.__repr__()
		s += '\n	* zero_5 = ' + self.zero_5.__repr__()
		s += '\n'
		return s
