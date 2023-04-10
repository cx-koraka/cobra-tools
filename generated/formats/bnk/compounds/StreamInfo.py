from generated.base_struct import BaseStruct
from generated.formats.bnk.imports import name_type_map


class StreamInfo(BaseStruct):

	"""
	Describes a wem file in an s type bank stream
	"""

	__name__ = 'StreamInfo'

	_import_key = 'bnk.compounds.StreamInfo'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.offset = 0
		self.size = 0

		# referred to by the events aux file
		self.event_id = 0
		self.zero = 0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('offset', name_type_map['Uint64'], (0, None), (False, None), (None, None))
		yield ('size', name_type_map['Uint64'], (0, None), (False, None), (None, None))
		yield ('event_id', name_type_map['Uint'], (0, None), (False, None), (None, None))
		yield ('zero', name_type_map['Uint'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'offset', name_type_map['Uint64'], (0, None), (False, None)
		yield 'size', name_type_map['Uint64'], (0, None), (False, None)
		yield 'event_id', name_type_map['Uint'], (0, None), (False, None)
		yield 'zero', name_type_map['Uint'], (0, None), (False, None)
