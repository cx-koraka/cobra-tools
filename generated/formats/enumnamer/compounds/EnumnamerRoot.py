from generated.formats.base.basic import Uint64
from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.ovl_base.compounds.Pointer import Pointer


class EnumnamerRoot(MemStruct):

	__name__ = 'EnumnamerRoot'

	_import_path = 'generated.formats.enumnamer.compounds.EnumnamerRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.count = 0
		self.strings = Pointer(self.context, self.count, EnumnamerRoot._import_path_map["generated.formats.enumnamer.compounds.PtrList"])
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.count = 0
		self.strings = Pointer(self.context, self.count, EnumnamerRoot._import_path_map["generated.formats.enumnamer.compounds.PtrList"])

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.count = Uint64.from_stream(stream, instance.context, 0, None)
		instance.strings = Pointer.from_stream(stream, instance.context, instance.count, EnumnamerRoot._import_path_map["generated.formats.enumnamer.compounds.PtrList"])
		if not isinstance(instance.strings, int):
			instance.strings.arg = instance.count

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Uint64.to_stream(stream, instance.count)
		Pointer.to_stream(stream, instance.strings)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'count', Uint64, (0, None), (False, None)
		yield 'strings', Pointer, (instance.count, EnumnamerRoot._import_path_map["generated.formats.enumnamer.compounds.PtrList"]), (False, None)

	def get_info_str(self, indent=0):
		return f'EnumnamerRoot [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
