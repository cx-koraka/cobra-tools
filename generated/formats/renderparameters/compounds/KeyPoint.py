from generated.formats.base.basic import Float
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class KeyPoint(MemStruct):

	__name__ = 'KeyPoint'

	_import_path = 'generated.formats.renderparameters.compounds.KeyPoint'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.time = 0.0
		self.value = 0.0
		self.tangent_before = 0.0
		self.tangent_after = 0.0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.time = 0.0
		self.value = 0.0
		self.tangent_before = 0.0
		self.tangent_after = 0.0

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'time', Float, (0, None), (False, None)
		yield 'value', Float, (0, None), (False, None)
		yield 'tangent_before', Float, (0, None), (False, None)
		yield 'tangent_after', Float, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'KeyPoint [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
