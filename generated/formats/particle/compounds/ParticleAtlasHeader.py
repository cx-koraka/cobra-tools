from generated.formats.base.basic import Uint
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class ParticleAtlasHeader(MemStruct):

	__name__ = 'ParticleAtlasHeader'

	_import_path = 'generated.formats.particle.compounds.ParticleAtlasHeader'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# matches number in tex file name
		self.id = 0
		self.zero = 0
		self.tex_name = Pointer(self.context, 0, ZString)
		self.gfr_name = Pointer(self.context, 0, ZString)

		# tex file used by atlas
		self.dependency_name = Pointer(self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.id = 0
		self.zero = 0
		self.tex_name = Pointer(self.context, 0, ZString)
		self.gfr_name = Pointer(self.context, 0, ZString)
		self.dependency_name = Pointer(self.context, 0, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'tex_name', Pointer, (0, ZString), (False, None)
		yield 'gfr_name', Pointer, (0, ZString), (False, None)
		yield 'id', Uint, (0, None), (False, None)
		yield 'zero', Uint, (0, None), (False, None)
		yield 'dependency_name', Pointer, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'ParticleAtlasHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
