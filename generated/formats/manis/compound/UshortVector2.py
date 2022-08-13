from generated.base_struct import BaseStruct
from generated.formats.base.basic import Ushort


class UshortVector2(BaseStruct):

	"""
	A vector in 2D space (x,y).
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# First coordinate.
		self.u = 0

		# Second coordinate.
		self.v = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		print(f'set_defaults {self.__class__.__name__}')
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
		super().read_fields(stream, instance)
		instance.u = stream.read_ushort()
		instance.v = stream.read_ushort()

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		stream.write_ushort(instance.u)
		stream.write_ushort(instance.v)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('u', Ushort, (0, None))
		yield ('v', Ushort, (0, None))

	def get_info_str(self, indent=0):
		return f'UshortVector2 [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* u = {self.fmt_member(self.u, indent+1)}'
		s += f'\n	* v = {self.fmt_member(self.v, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
