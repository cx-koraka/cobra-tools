from generated.array import Array
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class CurveList(MemStruct):

	"""
	this is not null ptr terminated, but padded to 16 bytes at the end
	"""

	__name__ = 'CurveList'

	_import_path = 'generated.formats.renderparameters.compounds.CurveList'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.ptrs = Array(self.context, 0, CurveList._import_path_map["generated.formats.renderparameters.compounds.KeyPoint"], (0,), Pointer)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'ptrs', Array, (0, CurveList._import_path_map["generated.formats.renderparameters.compounds.KeyPoint"], (instance.arg,), Pointer), (False, None)

	def get_info_str(self, indent=0):
		return f'CurveList [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
