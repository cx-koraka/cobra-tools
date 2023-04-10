from generated.formats.motiongraph.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class CoordinatedAnimationActivityData(MemStruct):

	"""
	72 bytes
	"""

	__name__ = 'CoordinatedAnimationActivityData'

	_import_key = 'motiongraph.compounds.CoordinatedAnimationActivityData'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.waiting_anim_data_streams = name_type_map['DataStreamResourceDataList'](self.context, 0, None)
		self.coordinated_anim_data_streams = name_type_map['DataStreamResourceDataList'](self.context, 0, None)
		self.priorities = 0
		self.looping = 0
		self._pad = 0
		self.blend_time = 0.0
		self.coord_group = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.waiting_anim = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.coordinated_anim = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.output_prop_through_variable = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('coord_group', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('waiting_anim', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('waiting_anim_data_streams', name_type_map['DataStreamResourceDataList'], (0, None), (False, None), (None, None))
		yield ('coordinated_anim', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('coordinated_anim_data_streams', name_type_map['DataStreamResourceDataList'], (0, None), (False, None), (None, None))
		yield ('priorities', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('looping', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('_pad', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('blend_time', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('output_prop_through_variable', name_type_map['Pointer'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'coord_group', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'waiting_anim', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'waiting_anim_data_streams', name_type_map['DataStreamResourceDataList'], (0, None), (False, None)
		yield 'coordinated_anim', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'coordinated_anim_data_streams', name_type_map['DataStreamResourceDataList'], (0, None), (False, None)
		yield 'priorities', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'looping', name_type_map['Ubyte'], (0, None), (False, None)
		yield '_pad', name_type_map['Ushort'], (0, None), (False, None)
		yield 'blend_time', name_type_map['Float'], (0, None), (False, None)
		yield 'output_prop_through_variable', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
