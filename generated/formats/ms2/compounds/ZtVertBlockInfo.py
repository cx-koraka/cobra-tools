import numpy
from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Ubyte
from generated.formats.base.basic import Uint


class ZtVertBlockInfo(BaseStruct):

	"""
	16 bytes total
	"""

	__name__ = 'ZtVertBlockInfo'

	_import_path = 'generated.formats.ms2.compounds.ZtVertBlockInfo'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.vertex_count = 0
		self.flags = Array(self.context, 0, None, (0,), Ubyte)
		self.zero = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.vertex_count = 0
		self.flags = numpy.zeros((8,), dtype=numpy.dtype('uint8'))
		self.zero = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.vertex_count = Uint.from_stream(stream, instance.context, 0, None)
		instance.flags = Array.from_stream(stream, instance.context, 0, None, (8,), Ubyte)
		instance.zero = Uint.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint.to_stream(stream, instance.vertex_count)
		Array.to_stream(stream, instance.flags, instance.context, 0, None, (8,), Ubyte)
		Uint.to_stream(stream, instance.zero)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'vertex_count', Uint, (0, None), (False, None)
		yield 'flags', Array, (0, None, (8,), Ubyte), (False, None)
		yield 'zero', Uint, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'ZtVertBlockInfo [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
