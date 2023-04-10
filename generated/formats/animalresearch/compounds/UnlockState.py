from generated.formats.animalresearch.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class UnlockState(MemStruct):

	__name__ = 'UnlockState'

	_import_key = 'animalresearch.compounds.UnlockState'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.entity_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.level_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('entity_name', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('level_name', name_type_map['Pointer'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'entity_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'level_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
