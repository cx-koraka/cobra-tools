from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class MatcolRoot(MemStruct):

	"""
	root_entry data
	"""

	__name__ = 'MatcolRoot'

	_import_path = 'generated.formats.matcol.compounds.MatcolRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# always 1
		self.one = 0
		self.main = Pointer(self.context, 0, MatcolRoot._import_path_map["generated.formats.matcol.compounds.RootFrag"])
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.one = 0
		self.main = Pointer(self.context, 0, MatcolRoot._import_path_map["generated.formats.matcol.compounds.RootFrag"])

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.main = Pointer.from_stream(stream, instance.context, 0, MatcolRoot._import_path_map["generated.formats.matcol.compounds.RootFrag"])
		instance.one = Uint64.from_stream(stream, instance.context, 0, None)
		if not isinstance(instance.main, int):
			instance.main.arg = 0

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Pointer.to_stream(stream, instance.main)
		Uint64.to_stream(stream, instance.one)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'main', Pointer, (0, MatcolRoot._import_path_map["generated.formats.matcol.compounds.RootFrag"]), (False, None)
		yield 'one', Uint64, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'MatcolRoot [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
