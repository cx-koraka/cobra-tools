from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.tex.imports import name_type_map


class TexBuffer(MemStruct):

	"""
	Describes one buffer of a tex / texturestream file.
	24 bytes per texture buffer
	"""

	__name__ = 'TexBuffer'

	_import_key = 'tex.compounds.TexBuffer'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# byte offset in the combined buffer
		self.offset = 0

		# byte size of this tex buffer
		self.size = 0

		# index of first mip used in this buffer
		self.first_mip = 0

		# amount of mip levels included in this buffer
		self.mip_count = 0
		self.padding_0 = 0
		self.padding_1 = 0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('offset', name_type_map['Uint64'], (0, None), (False, None), (None, None))
		yield ('size', name_type_map['Uint64'], (0, None), (False, None), (None, None))
		yield ('first_mip', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('mip_count', name_type_map['Ubyte'], (0, None), (False, None), (None, None))
		yield ('padding_0', name_type_map['Short'], (0, None), (True, 0), (None, None))
		yield ('padding_1', name_type_map['Int'], (0, None), (True, 0), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'offset', name_type_map['Uint64'], (0, None), (False, None)
		yield 'size', name_type_map['Uint64'], (0, None), (False, None)
		yield 'first_mip', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'mip_count', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'padding_0', name_type_map['Short'], (0, None), (True, 0)
		yield 'padding_1', name_type_map['Int'], (0, None), (True, 0)
