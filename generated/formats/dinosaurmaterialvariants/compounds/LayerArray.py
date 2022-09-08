from generated.array import Array
from generated.formats.dinosaurmaterialvariants.compounds.Layer import Layer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class LayerArray(MemStruct):

	__name__ = 'LayerArray'

	_import_path = 'generated.formats.dinosaurmaterialvariants.compounds.LayerArray'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.layers = Array(self.context, 0, None, (0,), Layer)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.layers = Array(self.context, 0, None, (self.arg,), Layer)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'layers', Array, (0, None, (instance.arg,), Layer), (False, None)

	def get_info_str(self, indent=0):
		return f'LayerArray [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
