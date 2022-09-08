from generated.formats.base.basic import Uint64
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class FontInfo(MemStruct):

	"""
	24 bytes
	"""

	__name__ = 'FontInfo'

	_import_path = 'generated.formats.scaleformlanguagedata.compounds.FontInfo'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.flag_or_count = 0
		self.style_name = Pointer(self.context, 0, ZString)
		self.font_file = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.flag_or_count = 0
		self.style_name = Pointer(self.context, 0, ZString)
		self.font_file = Pointer(self.context, 0, ZString)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'style_name', Pointer, (0, ZString), (False, None)
		yield 'font_file', Pointer, (0, ZString), (False, None)
		yield 'flag_or_count', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'FontInfo [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
