import typing


class Mdl2FourtyInfo:

	# 0, 1, 0, 0, 0
	unknowns: typing.List[int]

	def __init__(self, arg=None, template=None):
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.unknowns = 0

	def read(self, stream):

		io_start = stream.tell()
		self.unknowns = [stream.read_uint64() for _ in range(5)]

		self.io_size = stream.tell() - io_start

	def write(self, stream):

		io_start = stream.tell()
		for item in self.unknowns: stream.write_uint64(item)

		self.io_size = stream.tell() - io_start

	def __repr__(self):
		s = 'Mdl2FourtyInfo [Size: '+str(self.io_size)+']'
		s += '\n	* unknowns = ' + self.unknowns.__repr__()
		s += '\n'
		return s
