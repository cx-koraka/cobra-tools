from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint
from generated.formats.ovl.compound.AssetEntry import AssetEntry
from generated.formats.ovl.compound.SetEntry import SetEntry


class SetHeader(BaseStruct):

	"""
	defines amount of sets and assets
	"""

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.set_count = 0
		self.asset_count = 0

		# must be 1065336831
		self.sig_a = 0

		# must be 16909320
		self.sig_b = 0
		self.sets = 0
		self.assets = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		print(f'set_defaults {self.__class__.__name__}')
		self.set_count = 0
		self.asset_count = 0
		self.sig_a = 1065336831
		self.sig_b = 16909320
		self.sets = Array((self.set_count,), SetEntry, self.context, 0, None)
		self.assets = Array((self.asset_count,), AssetEntry, self.context, 0, None)

	def read(self, stream):
		self.io_start = stream.tell()
		self.read_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		self.write_fields(stream, self)
		self.io_size = stream.tell() - self.io_start

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.set_count = stream.read_uint()
		instance.asset_count = stream.read_uint()
		instance.sig_a = stream.read_uint()
		instance.sig_b = stream.read_uint()
		instance.sets = Array.from_stream(stream, (instance.set_count,), SetEntry, instance.context, 0, None)
		instance.assets = Array.from_stream(stream, (instance.asset_count,), AssetEntry, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		stream.write_uint(instance.set_count)
		stream.write_uint(instance.asset_count)
		stream.write_uint(instance.sig_a)
		stream.write_uint(instance.sig_b)
		Array.to_stream(stream, instance.sets, (instance.set_count,), SetEntry, instance.context, 0, None)
		Array.to_stream(stream, instance.assets, (instance.asset_count,), AssetEntry, instance.context, 0, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('set_count', Uint, (0, None))
		yield ('asset_count', Uint, (0, None))
		yield ('sig_a', Uint, (0, None))
		yield ('sig_b', Uint, (0, None))
		yield ('sets', Array, ((instance.set_count,), SetEntry, 0, None))
		yield ('assets', Array, ((instance.asset_count,), AssetEntry, 0, None))

	def get_info_str(self, indent=0):
		return f'SetHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* set_count = {self.fmt_member(self.set_count, indent+1)}'
		s += f'\n	* asset_count = {self.fmt_member(self.asset_count, indent+1)}'
		s += f'\n	* sig_a = {self.fmt_member(self.sig_a, indent+1)}'
		s += f'\n	* sig_b = {self.fmt_member(self.sig_b, indent+1)}'
		s += f'\n	* sets = {self.fmt_member(self.sets, indent+1)}'
		s += f'\n	* assets = {self.fmt_member(self.assets, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
