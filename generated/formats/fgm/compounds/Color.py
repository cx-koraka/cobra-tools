from generated.formats.fgm.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class Color(MemStruct):

	"""
	4 bytes
	"""

	__name__ = 'Color'

	_import_key = 'fgm.compounds.Color'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.r = name_type_map['Ubyte'](self.context, 0, None)
		self.g = name_type_map['Ubyte'](self.context, 0, None)
		self.b = name_type_map['Ubyte'](self.context, 0, None)
		self.a = name_type_map['Ubyte'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('r', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('g', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('b', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('a', name_type_map['Ubyte'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'r', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'g', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'b', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'a', name_type_map['Ubyte'], (0, None), (False, None)
