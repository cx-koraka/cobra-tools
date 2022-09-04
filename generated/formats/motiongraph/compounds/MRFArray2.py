from generated.array import Array
from generated.formats.motiongraph.compounds.MRFEntry2 import MRFEntry2
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class MRFArray2(MemStruct):

	__name__ = 'MRFArray2'

	_import_path = 'generated.formats.motiongraph.compounds.MRFArray2'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.states = Array(self.context, 0, None, (0,), MRFEntry2)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.states = Array(self.context, 0, None, (self.arg,), MRFEntry2)

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.states = Array.from_stream(stream, instance.context, 0, None, (instance.arg,), MRFEntry2)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Array.to_stream(stream, instance.states, instance.context, 0, None, (instance.arg,), MRFEntry2)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'states', Array, (0, None, (instance.arg,), MRFEntry2), (False, None)

	def get_info_str(self, indent=0):
		return f'MRFArray2 [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* states = {self.fmt_member(self.states, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
