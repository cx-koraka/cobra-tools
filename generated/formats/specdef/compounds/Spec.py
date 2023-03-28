from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.specdef.enums.SpecdefDtype import SpecdefDtype


class Spec(MemStruct):

	__name__ = 'Spec'

	_import_key = 'specdef.compounds.Spec'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.dtype = SpecdefDtype(self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('dtype', SpecdefDtype, (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'dtype', SpecdefDtype, (0, None), (False, None)


Spec.init_attributes()
