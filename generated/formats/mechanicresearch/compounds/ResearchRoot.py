from generated.formats.mechanicresearch.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class ResearchRoot(MemStruct):

	__name__ = 'ResearchRoot'

	_import_key = 'mechanicresearch.compounds.ResearchRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count = 0
		self.levels = name_type_map['ArrayPointer'](self.context, self.count, name_type_map['Research'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('levels', name_type_map['ArrayPointer'], (None, None), (False, None), (None, None))
		yield ('count', name_type_map['Uint64'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'levels', name_type_map['ArrayPointer'], (instance.count, name_type_map['Research']), (False, None)
		yield 'count', name_type_map['Uint64'], (0, None), (False, None)
