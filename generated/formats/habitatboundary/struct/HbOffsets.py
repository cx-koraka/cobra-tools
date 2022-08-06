from source.formats.base.basic import fmt_member
from generated.formats.habitatboundary.struct.HbPhysicsOffsets import HbPhysicsOffsets
from generated.formats.ovl_base.compound.MemStruct import MemStruct


class HbOffsets(MemStruct):

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		super().__init__(context, arg, template, set_default)
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.physics = HbPhysicsOffsets(self.context, 0, None)

		# Vertical offset of visible post above wall. Post height = wall_height + post_height_offset.
		self.post_height_offset = 0.0

		# The starting height of the barrier wall.
		self.wall_height = 0.0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.physics = HbPhysicsOffsets(self.context, 0, None)
		self.post_height_offset = 0.0
		self.wall_height = 0.0

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
		instance.physics = HbPhysicsOffsets.from_stream(stream, instance.context, 0, None)
		instance.post_height_offset = stream.read_float()
		instance.wall_height = stream.read_float()

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		HbPhysicsOffsets.to_stream(stream, instance.physics)
		stream.write_float(instance.post_height_offset)
		stream.write_float(instance.wall_height)

	@classmethod
	def from_stream(cls, stream, context, arg=0, template=None):
		instance = cls(context, arg, template, set_default=False)
		instance.io_start = stream.tell()
		cls.read_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance

	@classmethod
	def to_stream(cls, stream, instance):
		instance.io_start = stream.tell()
		cls.write_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance

	def get_info_str(self, indent=0):
		return f'HbOffsets [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* physics = {fmt_member(self.physics, indent+1)}'
		s += f'\n	* post_height_offset = {fmt_member(self.post_height_offset, indent+1)}'
		s += f'\n	* wall_height = {fmt_member(self.wall_height, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
