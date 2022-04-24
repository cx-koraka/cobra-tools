from source.formats.base.basic import fmt_member
from generated.context import ContextReference


class UshortVector2:

	"""
	A vector in 2D space (x,y).
	"""

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

		# First coordinate.
		self.u = 0

		# Second coordinate.
		self.v = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.u = 0
		self.v = 0

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
		instance.u = stream.read_ushort()
		instance.v = stream.read_ushort()

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write_ushort(instance.u)
		stream.write_ushort(instance.v)

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

	def get_info_str(self, indent=0):
		return f'UshortVector2 [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += f'\n	* u = {fmt_member(self.u, indent+1)}'
		s += f'\n	* v = {fmt_member(self.v, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
