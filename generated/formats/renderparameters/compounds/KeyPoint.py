from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.renderparameters.imports import name_type_map


class KeyPoint(MemStruct):

	__name__ = 'KeyPoint'

	_import_key = 'renderparameters.compounds.KeyPoint'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.time = 0.0
		self.value = 0.0
		self.tangent_before = 0.0
		self.tangent_after = 0.0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('time', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('value', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('tangent_before', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('tangent_after', name_type_map['Float'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'time', name_type_map['Float'], (0, None), (False, None)
		yield 'value', name_type_map['Float'], (0, None), (False, None)
		yield 'tangent_before', name_type_map['Float'], (0, None), (False, None)
		yield 'tangent_after', name_type_map['Float'], (0, None), (False, None)
