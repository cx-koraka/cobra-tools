from generated.formats.dinosaurmaterialvariants.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class Vector3F(MemStruct):

	__name__ = 'Vector3f'

	_import_key = 'dinosaurmaterialvariants.compounds.Vector3F'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('x', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('y', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('z', name_type_map['Float'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'x', name_type_map['Float'], (0, None), (False, None)
		yield 'y', name_type_map['Float'], (0, None), (False, None)
		yield 'z', name_type_map['Float'], (0, None), (False, None)
