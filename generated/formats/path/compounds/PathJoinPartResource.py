from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.path.imports import name_type_map


class PathJoinPartResource(MemStruct):

	__name__ = 'PathJoinPartResource'

	_import_key = 'path.compounds.PathJoinPartResource'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.padding_1 = 0
		self.unk_byte_1 = 0
		self.unk_byte_2 = 0
		self.unk_byte_3 = 0
		self.num_points_1 = 0
		self.num_points_1_copy = 0
		self.num_points_2 = 0
		self.num_points_2_copy = 0
		self.num_points_3 = 0
		self.padding_2 = 0
		self.unk_points_1 = name_type_map['Pointer'](self.context, self.num_points_1, name_type_map['PointsList'])
		self.unk_points_2 = name_type_map['Pointer'](self.context, self.num_points_2, name_type_map['PointsList'])
		self.unk_vector = name_type_map['ArrayPointer'](self.context, 1, name_type_map['Vector4'])
		self.unk_shorts = name_type_map['ArrayPointer'](self.context, 8, name_type_map['Ushort'])
		self.unk_points_3 = name_type_map['Pointer'](self.context, self.num_points_3, name_type_map['PointsList'])
		self.pathresource = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('unk_points_1', name_type_map['Pointer'], (None, None), (False, None), (None, None))
		yield ('unk_points_2', name_type_map['Pointer'], (None, None), (False, None), (None, None))
		yield ('unk_vector', name_type_map['ArrayPointer'], (1, None), (False, None), (None, None))
		yield ('unk_shorts', name_type_map['ArrayPointer'], (8, None), (False, None), (None, None))
		yield ('unk_points_3', name_type_map['Pointer'], (None, None), (False, None), (None, None))
		yield ('padding_1', name_type_map['Uint64'], (0, None), (True, 0), (None, None))
		yield ('pathresource', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('unk_byte_1', name_type_map['Byte'], (0, None), (False, None), (None, None))
		yield ('unk_byte_2', name_type_map['Byte'], (0, None), (False, None), (None, None))
		yield ('unk_byte_3', name_type_map['Byte'], (0, None), (False, None), (None, None))
		yield ('num_points_1', name_type_map['Byte'], (0, None), (False, None), (None, None))
		yield ('num_points_1_copy', name_type_map['Byte'], (0, None), (False, None), (None, None))
		yield ('num_points_2', name_type_map['Byte'], (0, None), (False, None), (None, None))
		yield ('num_points_2_copy', name_type_map['Byte'], (0, None), (False, None), (None, None))
		yield ('num_points_3', name_type_map['Byte'], (0, None), (False, None), (None, None))
		yield ('padding_2', name_type_map['Uint64'], (0, None), (True, 0), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'unk_points_1', name_type_map['Pointer'], (instance.num_points_1, name_type_map['PointsList']), (False, None)
		yield 'unk_points_2', name_type_map['Pointer'], (instance.num_points_2, name_type_map['PointsList']), (False, None)
		yield 'unk_vector', name_type_map['ArrayPointer'], (1, name_type_map['Vector4']), (False, None)
		yield 'unk_shorts', name_type_map['ArrayPointer'], (8, name_type_map['Ushort']), (False, None)
		yield 'unk_points_3', name_type_map['Pointer'], (instance.num_points_3, name_type_map['PointsList']), (False, None)
		yield 'padding_1', name_type_map['Uint64'], (0, None), (True, 0)
		yield 'pathresource', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'unk_byte_1', name_type_map['Byte'], (0, None), (False, None)
		yield 'unk_byte_2', name_type_map['Byte'], (0, None), (False, None)
		yield 'unk_byte_3', name_type_map['Byte'], (0, None), (False, None)
		yield 'num_points_1', name_type_map['Byte'], (0, None), (False, None)
		yield 'num_points_1_copy', name_type_map['Byte'], (0, None), (False, None)
		yield 'num_points_2', name_type_map['Byte'], (0, None), (False, None)
		yield 'num_points_2_copy', name_type_map['Byte'], (0, None), (False, None)
		yield 'num_points_3', name_type_map['Byte'], (0, None), (False, None)
		yield 'padding_2', name_type_map['Uint64'], (0, None), (True, 0)
