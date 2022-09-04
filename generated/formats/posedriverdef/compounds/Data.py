import numpy
from generated.array import Array
from generated.formats.base.basic import Float
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class Data(MemStruct):

	__name__ = 'Data'

	_import_path = 'generated.formats.posedriverdef.compounds.Data'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.floats = Array(self.context, 0, None, (0,), Float)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.floats = numpy.zeros((16,), dtype=numpy.dtype('float32'))

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.floats = Array.from_stream(stream, instance.context, 0, None, (16,), Float)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Array.to_stream(stream, instance.floats, instance.context, 0, None, (16,), Float)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'floats', Array, (0, None, (16,), Float), (False, None)

	def get_info_str(self, indent=0):
		return f'Data [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
