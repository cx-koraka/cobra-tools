from generated.formats.base.basic import Ushort
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class TexBufferPc(MemStruct):

	"""
	The different tex buffers contain the smallest mip
	"""

	__name__ = 'TexBufferPc'

	_import_path = 'generated.formats.tex.compounds.TexBufferPc'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.width = 0
		self.height = 0

		# may be depth
		self.array_size = 0

		# the first ie. biggest levels are clipped off
		self.num_mips = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.width = 0
		self.height = 0
		if self.context.version >= 18:
			self.array_size = 0
		self.num_mips = 0

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'width', Ushort, (0, None), (False, None)
		yield 'height', Ushort, (0, None), (False, None)
		if instance.context.version >= 18:
			yield 'array_size', Ushort, (0, None), (False, None)
		yield 'num_mips', Ushort, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'TexBufferPc [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
