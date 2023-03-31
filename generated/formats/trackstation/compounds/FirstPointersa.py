from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.trackstation.compounds.CommonChunk import CommonChunk


class FirstPointersa(MemStruct):

	"""
	PZ and PC: 320 bytes
	"""

	__name__ = 'FirstPointersa'

	_import_key = 'trackstation.compounds.FirstPointersa'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.pointer_stuff_1 = CommonChunk(self.context, 0, None)
		self.pointer_stuff_2 = CommonChunk(self.context, 0, None)
		self.pointer_stuff_3 = CommonChunk(self.context, 0, None)
		self.zero = 0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('pointer_stuff_1', CommonChunk, (0, None), (False, None), (None, None))
		yield ('pointer_stuff_2', CommonChunk, (0, None), (False, None), (None, None))
		yield ('pointer_stuff_3', CommonChunk, (0, None), (False, None), (None, None))
		yield ('zero', Uint64, (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'pointer_stuff_1', CommonChunk, (0, None), (False, None)
		yield 'pointer_stuff_2', CommonChunk, (0, None), (False, None)
		yield 'pointer_stuff_3', CommonChunk, (0, None), (False, None)
		yield 'zero', Uint64, (0, None), (False, None)


FirstPointersa.init_attributes()
