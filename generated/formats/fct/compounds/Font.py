from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class Font(MemStruct):

	"""
	JWE1: 16 bytes
	"""

	__name__ = 'Font'

	_import_path = 'generated.formats.fct.compounds.Font'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.data_size = 0
		self.zero = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.data_size = 0
		self.zero = 0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.data_size = Uint64.from_stream(stream, instance.context, 0, None)
		instance.zero = Uint64.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint64.to_stream(stream, instance.data_size)
		Uint64.to_stream(stream, instance.zero)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'data_size', Uint64, (0, None), (False, None)
		yield 'zero', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'Font [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
