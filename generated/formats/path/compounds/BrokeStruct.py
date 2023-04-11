from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.path.imports import name_type_map


class BrokeStruct(MemStruct):

	__name__ = 'BrokeStruct'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.unk_vector_1 = name_type_map['Vector3'](self.context, 0, None)
		self.unk_vector_2 = name_type_map['Vector3'](self.context, 0, None)
		self.support = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.fallen_support = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.head = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'support', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'fallen_support', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'head', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None), (None, None)
		yield 'unk_vector_1', name_type_map['Vector3'], (0, None), (False, None), (None, None)
		yield 'unk_vector_2', name_type_map['Vector3'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'support', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'fallen_support', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'head', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'unk_vector_1', name_type_map['Vector3'], (0, None), (False, None)
		yield 'unk_vector_2', name_type_map['Vector3'], (0, None), (False, None)
