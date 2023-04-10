from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.pscollection.imports import name_type_map


class Arg(MemStruct):

	__name__ = 'Arg'

	_import_key = 'pscollection.compounds.Arg'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.u_0 = 0
		self.arg_type = 0

		# one-based index
		self.arg_index = 0
		self.u_1 = 0
		self.u_2 = 0
		self.u_3 = 0
		self.u_4 = 0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('u_0', name_type_map['Ubyte'], (0, None), (True, 0), (None, None))
		yield ('arg_type', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('arg_index', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('u_1', name_type_map['Ubyte'], (0, None), (True, 0), (None, None))
		yield ('u_2', name_type_map['Uint'], (0, None), (True, 0), (None, None))
		yield ('u_3', name_type_map['Uint64'], (0, None), (True, 0), (None, None))
		yield ('u_4', name_type_map['Uint64'], (0, None), (True, 0), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'u_0', name_type_map['Ubyte'], (0, None), (True, 0)
		yield 'arg_type', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'arg_index', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'u_1', name_type_map['Ubyte'], (0, None), (True, 0)
		yield 'u_2', name_type_map['Uint'], (0, None), (True, 0)
		yield 'u_3', name_type_map['Uint64'], (0, None), (True, 0)
		yield 'u_4', name_type_map['Uint64'], (0, None), (True, 0)
