from generated.formats.base.basic import Uint
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class MediaEntry(MemStruct):

	"""
	PC: 32 bytes
	"""

	__name__ = 'MediaEntry'

	_import_path = 'generated.formats.wmeta.compounds.MediaEntry'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.hash = 0
		self.zero = 0
		self.block_name = Pointer(self.context, 0, ZString)
		self.wav_name = Pointer(self.context, 0, ZString)
		self.wem_name = Pointer(self.context, 0, ZString)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.hash = 0
		self.zero = 0
		self.block_name = Pointer(self.context, 0, ZString)
		self.wav_name = Pointer(self.context, 0, ZString)
		self.wem_name = Pointer(self.context, 0, ZString)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'hash', Uint, (0, None), (False, None)
		yield 'zero', Uint, (0, None), (False, None)
		yield 'block_name', Pointer, (0, ZString), (False, None)
		yield 'wav_name', Pointer, (0, ZString), (False, None)
		yield 'wem_name', Pointer, (0, ZString), (False, None)

	def get_info_str(self, indent=0):
		return f'MediaEntry [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
