from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.particleeffect.imports import name_type_map


class LastRow(MemStruct):

	__name__ = 'LastRow'

	_import_key = 'particleeffect.compounds.LastRow'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.unk_01 = 0
		self.unk_02 = 0
		self.unk_03 = 0
		self.unk_04 = 0
		self.unk_05 = 0
		self.unk_06 = 0
		self.unk_07 = 0
		self.unk_08 = 0
		self.unk_09 = 0
		self.unk_10 = 0
		self.unk_11 = 0
		self.unk_12 = 0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('unk_01', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_02', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_03', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_04', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_05', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_06', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_07', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_08', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_09', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_10', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_11', name_type_map['Ushort'], (0, None), (False, None), (None, None))
		yield ('unk_12', name_type_map['Ushort'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'unk_01', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_02', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_03', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_04', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_05', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_06', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_07', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_08', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_09', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_10', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_11', name_type_map['Ushort'], (0, None), (False, None)
		yield 'unk_12', name_type_map['Ushort'], (0, None), (False, None)
