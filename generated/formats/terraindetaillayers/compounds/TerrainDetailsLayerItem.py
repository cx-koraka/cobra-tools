from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.terraindetaillayers.imports import name_type_map


class TerrainDetailsLayerItem(MemStruct):

	"""
	# 88 bytes
	"""

	__name__ = 'TerrainDetailsLayerItem'

	_import_key = 'terraindetaillayers.compounds.TerrainDetailsLayerItem'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.info_count = 0
		self.float_1 = 0.0
		self.float_2 = 0.0
		self.float_3 = 0.0
		self.float_4 = 0.0
		self.float_5 = 0.0
		self.float_6 = 0.0
		self.unk_2 = 0
		self.detail_count = 0
		self.floata_1 = 0.0
		self.floata_2 = 0.0
		self.floata_3 = 0.0
		self.floata_4 = 0.0
		self.floata_5 = 0.0
		self.floata_6 = 0.0
		self.floata_7 = 0.0
		self.floata_8 = 0.0
		self.unk_3_flags = 0
		self.unk_4_found_as_1 = 0
		self.unk_5_as_0 = 0
		self.unk_6_as_0 = 0
		self.unk_7_as_0 = 0
		self.unk_8_as_0 = 0
		self.unk_9_as_0 = 0
		self.unk_a_as_0 = 0
		self.unk_b_as_0 = 0
		self.floatb_1 = 0.0
		self.floatb_2 = 0.0
		self.layer_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.info_list = name_type_map['ArrayPointer'](self.context, self.info_count, name_type_map['InfoStruct'])
		self.detail_list = name_type_map['ArrayPointer'](self.context, self.detail_count, name_type_map['DetailStruct'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('layer_name', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('info_list', name_type_map['ArrayPointer'], (None, None), (False, None), (None, None))
		yield ('info_count', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('float_1', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('float_2', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('float_3', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('float_4', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('float_5', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('float_6', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('unk_2', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('detail_list', name_type_map['ArrayPointer'], (None, None), (False, None), (None, None))
		yield ('detail_count', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('floata_1', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('floata_2', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('floata_3', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('floata_4', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('floata_5', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('floata_6', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('floata_7', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('floata_8', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('unk_3_flags', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('unk_4_found_as_1', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('unk_5_as_0', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('unk_6_as_0', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('unk_7_as_0', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('unk_8_as_0', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('unk_9_as_0', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('unk_a_as_0', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('unk_b_as_0', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('floatb_1', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('floatb_2', name_type_map['Float'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'layer_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'info_list', name_type_map['ArrayPointer'], (instance.info_count, name_type_map['InfoStruct']), (False, None)
		yield 'info_count', name_type_map['Uint'], (0, None), (False, None)
		yield 'float_1', name_type_map['Float'], (0, None), (False, None)
		yield 'float_2', name_type_map['Float'], (0, None), (False, None)
		yield 'float_3', name_type_map['Float'], (0, None), (False, None)
		yield 'float_4', name_type_map['Float'], (0, None), (False, None)
		yield 'float_5', name_type_map['Float'], (0, None), (False, None)
		yield 'float_6', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_2', name_type_map['Uint'], (0, None), (False, None)
		yield 'detail_list', name_type_map['ArrayPointer'], (instance.detail_count, name_type_map['DetailStruct']), (False, None)
		yield 'detail_count', name_type_map['Uint'], (0, None), (False, None)
		yield 'floata_1', name_type_map['Float'], (0, None), (False, None)
		yield 'floata_2', name_type_map['Float'], (0, None), (False, None)
		yield 'floata_3', name_type_map['Float'], (0, None), (False, None)
		yield 'floata_4', name_type_map['Float'], (0, None), (False, None)
		yield 'floata_5', name_type_map['Float'], (0, None), (False, None)
		yield 'floata_6', name_type_map['Float'], (0, None), (False, None)
		yield 'floata_7', name_type_map['Float'], (0, None), (False, None)
		yield 'floata_8', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_3_flags', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_4_found_as_1', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_5_as_0', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_6_as_0', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_7_as_0', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_8_as_0', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_9_as_0', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_a_as_0', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_b_as_0', name_type_map['Uint'], (0, None), (False, None)
		yield 'floatb_1', name_type_map['Float'], (0, None), (False, None)
		yield 'floatb_2', name_type_map['Float'], (0, None), (False, None)
