import numpy
from generated.array import Array
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.uimoviedefinition.imports import name_type_map


class UiMovieHeader(MemStruct):

	__name__ = 'UiMovieHeader'

	_import_key = 'uimoviedefinition.compounds.UiMovieHeader'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.flag_1 = 0
		self.flag_2 = 0
		self.flag_3 = 0
		self.floats = Array(self.context, 0, None, (0,), name_type_map['Float'])
		self.u_0 = 0
		self.num_ui_triggers = 0
		self.u_1 = 0
		self.num_ui_names = 0
		self.num_assetpkgs = 0
		self.u_2 = 0
		self.num_list_1 = 0
		self.num_list_2 = 0
		self.num_ui_interfaces = 0
		self.u_3 = 0
		self.u_4 = 0
		self.u_5 = 0
		self.movie_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.pkg_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.category_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.type_name = name_type_map['Pointer'](self.context, 0, name_type_map['ZString'])
		self.ptr_0 = name_type_map['Pointer'](self.context, 0, None)
		self.ui_triggers = name_type_map['Pointer'](self.context, self.num_ui_triggers, name_type_map['PtrList'])
		self.ptr_1 = name_type_map['Pointer'](self.context, 0, None)
		self.ui_names = name_type_map['Pointer'](self.context, self.num_ui_names, name_type_map['PtrList'])
		self.assetpkgs = name_type_map['Pointer'](self.context, self.num_assetpkgs, name_type_map['PtrList'])
		self.ptr_2 = name_type_map['Pointer'](self.context, 0, None)
		self.list_1 = name_type_map['ArrayPointer'](self.context, self.num_list_1, name_type_map['Uint'])
		self.list_2 = name_type_map['ArrayPointer'](self.context, self.num_list_2, name_type_map['Uint'])
		self.ui_interfaces = name_type_map['Pointer'](self.context, self.num_ui_interfaces, name_type_map['PtrList'])
		self.ptr_3 = name_type_map['Pointer'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('movie_name', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('pkg_name', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('category_name', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('type_name', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('flag_1', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('flag_2', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('flag_3', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('floats', Array, (0, None, (3,), name_type_map['Float']), (False, None), (None, None))
		yield ('u_0', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('num_ui_triggers', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('u_1', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('num_ui_names', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('num_assetpkgs', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('u_2', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('num_list_1', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('num_list_2', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('num_ui_interfaces', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('u_3', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('u_4', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('u_5', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('ptr_0', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('ui_triggers', name_type_map['Pointer'], (None, None), (False, None), (None, None))
		yield ('ptr_1', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('ui_names', name_type_map['Pointer'], (None, None), (False, None), (None, None))
		yield ('assetpkgs', name_type_map['Pointer'], (None, None), (False, None), (None, None))
		yield ('ptr_2', name_type_map['Pointer'], (0, None), (False, None), (None, None))
		yield ('list_1', name_type_map['ArrayPointer'], (None, None), (False, None), (None, None))
		yield ('list_2', name_type_map['ArrayPointer'], (None, None), (False, None), (None, None))
		yield ('ui_interfaces', name_type_map['Pointer'], (None, None), (False, None), (None, None))
		yield ('ptr_3', name_type_map['Pointer'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'movie_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'pkg_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'category_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'type_name', name_type_map['Pointer'], (0, name_type_map['ZString']), (False, None)
		yield 'flag_1', name_type_map['Uint'], (0, None), (False, None)
		yield 'flag_2', name_type_map['Ushort'], (0, None), (False, None)
		yield 'flag_3', name_type_map['Ushort'], (0, None), (False, None)
		yield 'floats', Array, (0, None, (3,), name_type_map['Float']), (False, None)
		yield 'u_0', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'num_ui_triggers', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'u_1', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'num_ui_names', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'num_assetpkgs', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'u_2', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'num_list_1', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'num_list_2', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'num_ui_interfaces', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'u_3', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'u_4', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'u_5', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'ptr_0', name_type_map['Pointer'], (0, None), (False, None)
		yield 'ui_triggers', name_type_map['Pointer'], (instance.num_ui_triggers, name_type_map['PtrList']), (False, None)
		yield 'ptr_1', name_type_map['Pointer'], (0, None), (False, None)
		yield 'ui_names', name_type_map['Pointer'], (instance.num_ui_names, name_type_map['PtrList']), (False, None)
		yield 'assetpkgs', name_type_map['Pointer'], (instance.num_assetpkgs, name_type_map['PtrList']), (False, None)
		yield 'ptr_2', name_type_map['Pointer'], (0, None), (False, None)
		yield 'list_1', name_type_map['ArrayPointer'], (instance.num_list_1, name_type_map['Uint']), (False, None)
		yield 'list_2', name_type_map['ArrayPointer'], (instance.num_list_2, name_type_map['Uint']), (False, None)
		yield 'ui_interfaces', name_type_map['Pointer'], (instance.num_ui_interfaces, name_type_map['PtrList']), (False, None)
		yield 'ptr_3', name_type_map['Pointer'], (0, None), (False, None)
