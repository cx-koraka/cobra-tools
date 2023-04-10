from generated.formats.frenderlodspec.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class FRenderLodSpecRoot(MemStruct):

	__name__ = 'FRenderLodSpecRoot'

	_import_key = 'frenderlodspec.compounds.FRenderLodSpecRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.spec_count = 0
		self.unknown = 0
		self.spec_list = name_type_map['ArrayPointer'](self.context, self.spec_count, name_type_map['LodSpecItem'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('spec_list', name_type_map['ArrayPointer'], (None, None), (False, None), (None, None))
		yield ('spec_count', name_type_map['Uint64'], (0, None), (False, None), (None, None))
		yield ('unknown', name_type_map['Uint64'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'spec_list', name_type_map['ArrayPointer'], (instance.spec_count, name_type_map['LodSpecItem']), (False, None)
		yield 'spec_count', name_type_map['Uint64'], (0, None), (False, None)
		yield 'unknown', name_type_map['Uint64'], (0, None), (False, None)
