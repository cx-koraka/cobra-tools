from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.specdef.imports import name_type_map


class Int16Data(MemStruct):

	"""
	8 bytes
	"""

	__name__ = 'Int16Data'

	_import_key = 'specdef.compounds.Int16Data'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.imin = 0
		self.imax = 0
		self.ivalue = 0
		self.ioptional = 0
		self.enum = name_type_map['Pointer'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('imin', name_type_map['Short'], (0, None), (False, None), (None, None))
		yield ('imax', name_type_map['Short'], (0, None), (False, None), (None, None))
		yield ('ivalue', name_type_map['Short'], (0, None), (False, None), (None, None))
		yield ('ioptional', name_type_map['Short'], (0, None), (False, None), (None, None))
		yield ('enum', name_type_map['Pointer'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'imin', name_type_map['Short'], (0, None), (False, None)
		yield 'imax', name_type_map['Short'], (0, None), (False, None)
		yield 'ivalue', name_type_map['Short'], (0, None), (False, None)
		yield 'ioptional', name_type_map['Short'], (0, None), (False, None)
		yield 'enum', name_type_map['Pointer'], (0, None), (False, None)
