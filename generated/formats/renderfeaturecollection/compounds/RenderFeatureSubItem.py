from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.renderfeaturecollection.imports import name_type_map


class RenderFeatureSubItem(MemStruct):

	__name__ = 'RenderFeatureSubItem'

	_import_key = 'renderfeaturecollection.compounds.RenderFeatureSubItem'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.sub_item_value_or_flags = 0
		self.sub_item_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('sub_item_name', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('sub_item_value_or_flags', name_type_map['Uint64'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'sub_item_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'sub_item_value_or_flags', name_type_map['Uint64'], (0, None), (False, None)
