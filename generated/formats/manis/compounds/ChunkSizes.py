from generated.base_struct import BaseStruct
from generated.formats.manis.imports import name_type_map


class ChunkSizes(BaseStruct):

	__name__ = 'ChunkSizes'

	_import_key = 'manis.compounds.ChunkSizes'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.zeros_0 = 0
		self.bone = 0
		self.counta = 0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('zeros_0', name_type_map['Uint64'], (0, None), (False, None), (None, None))
		yield ('bone', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('counta', name_type_map['Uint'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'zeros_0', name_type_map['Uint64'], (0, None), (False, None)
		yield 'bone', name_type_map['Uint'], (0, None), (False, None)
		yield 'counta', name_type_map['Uint'], (0, None), (False, None)
