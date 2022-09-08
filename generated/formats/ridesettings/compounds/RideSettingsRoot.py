from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class RideSettingsRoot(MemStruct):

	__name__ = 'RideSettingsRoot'

	_import_path = 'generated.formats.ridesettings.compounds.RideSettingsRoot'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.unk_0 = 0.0
		self.unk_1 = 0
		self.count = 0
		self.pad_0 = 0
		self.pad_1 = 0
		self.pad_2 = 0
		self.array_1 = ArrayPointer(self.context, self.count, RideSettingsRoot._import_path_map["generated.formats.ridesettings.compounds.Pair"])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'unk_0', Float, (0, None), (False, None)
		yield 'unk_1', Uint, (0, None), (False, None)
		yield 'array_1', ArrayPointer, (instance.count, RideSettingsRoot._import_path_map["generated.formats.ridesettings.compounds.Pair"]), (False, None)
		yield 'count', Uint, (0, None), (False, None)
		yield 'pad_0', Uint, (0, None), (False, None)
		yield 'pad_1', Uint, (0, None), (False, None)
		yield 'pad_2', Uint, (0, None), (False, None)

	def get_info_str(self, indent=0):
		return f'RideSettingsRoot [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
