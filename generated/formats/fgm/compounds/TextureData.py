from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class TextureData(MemStruct):

	__name__ = 'TextureData'

	_import_path = 'generated.formats.fgm.compounds.TextureData'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# only present if textured
		self.dependency_name = Pointer(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		if self.arg.dtype == 8:
			self.dependency_name = Pointer(self.context, 0, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		if instance.arg.dtype == 8:
			yield 'dependency_name', Pointer, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'TextureData [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
