import numpy
from generated.array import Array
from generated.formats.base.basic import Ubyte
from generated.formats.ovl_base.compound.GenericHeader import GenericHeader
from generated.formats.tex.compound.SizeInfo import SizeInfo
from generated.formats.tex.compound.TexBuffer import TexBuffer
from generated.formats.tex.compound.TexBufferPc import TexBufferPc
from generated.formats.tex.compound.TexHeader import TexHeader


class TexInfoHeader(GenericHeader):

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.tex_info = 0
		self.frag_01 = 0
		self.frag_11 = 0

		# pad whole frag_11 struct to 320 bytes
		self.padding = 0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		print(f'set_defaults {self.__class__.__name__}')
		self.tex_info = TexHeader(self.context, 0, None)
		if 17 <= self.context.version <= 18:
			self.frag_01 = Array((self.tex_info.stream_count,), TexBufferPc, self.context, 0, None)
		if self.context.version >= 19:
			self.frag_01 = Array((self.tex_info.stream_count,), TexBuffer, self.context, 0, None)
			self.frag_11 = SizeInfo(self.context, 0, None)
		if ((not self.context.user_version.is_jwe) and (self.context.version == 20)) or (((not self.context.user_version.is_jwe) and (self.context.version >= 19)) or (self.context.user_version.is_jwe and (self.context.version == 20))):
			self.padding = numpy.zeros((320 - self.frag_11.io_size,), dtype=numpy.dtype('uint8'))
		if self.context.user_version.is_jwe and (self.context.version == 19):
			self.padding = numpy.zeros((384 - self.frag_11.io_size,), dtype=numpy.dtype('uint8'))

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
		instance.tex_info = TexHeader.from_stream(stream, instance.context, 0, None)
		if 17 <= instance.context.version <= 18:
			instance.frag_01 = Array.from_stream(stream, (instance.tex_info.stream_count,), TexBufferPc, instance.context, 0, None)
		if instance.context.version >= 19:
			instance.frag_01 = Array.from_stream(stream, (instance.tex_info.stream_count,), TexBuffer, instance.context, 0, None)
			instance.frag_11 = SizeInfo.from_stream(stream, instance.context, 0, None)
		if ((not instance.context.user_version.is_jwe) and (instance.context.version == 20)) or (((not instance.context.user_version.is_jwe) and (instance.context.version >= 19)) or (instance.context.user_version.is_jwe and (instance.context.version == 20))):
			instance.padding = stream.read_ubytes((320 - instance.frag_11.io_size,))
		if instance.context.user_version.is_jwe and (instance.context.version == 19):
			instance.padding = stream.read_ubytes((384 - instance.frag_11.io_size,))

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		TexHeader.to_stream(stream, instance.tex_info)
		if 17 <= instance.context.version <= 18:
			Array.to_stream(stream, instance.frag_01, (instance.tex_info.stream_count,), TexBufferPc, instance.context, 0, None)
		if instance.context.version >= 19:
			Array.to_stream(stream, instance.frag_01, (instance.tex_info.stream_count,), TexBuffer, instance.context, 0, None)
			SizeInfo.to_stream(stream, instance.frag_11)
		if ((not instance.context.user_version.is_jwe) and (instance.context.version == 20)) or (((not instance.context.user_version.is_jwe) and (instance.context.version >= 19)) or (instance.context.user_version.is_jwe and (instance.context.version == 20))):
			stream.write_ubytes(instance.padding)
		if instance.context.user_version.is_jwe and (instance.context.version == 19):
			stream.write_ubytes(instance.padding)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		super()._get_filtered_attribute_list(instance)
		yield ('tex_info', TexHeader, (0, None))
		if 17 <= instance.context.version <= 18:
			yield ('frag_01', Array, ((instance.tex_info.stream_count,), TexBufferPc, 0, None))
		if instance.context.version >= 19:
			yield ('frag_01', Array, ((instance.tex_info.stream_count,), TexBuffer, 0, None))
			yield ('frag_11', SizeInfo, (0, None))
		if ((not instance.context.user_version.is_jwe) and (instance.context.version == 20)) or (((not instance.context.user_version.is_jwe) and (instance.context.version >= 19)) or (instance.context.user_version.is_jwe and (instance.context.version == 20))):
			yield ('padding', Array, ((320 - instance.frag_11.io_size,), Ubyte, 0, None))
		if instance.context.user_version.is_jwe and (instance.context.version == 19):
			yield ('padding', Array, ((384 - instance.frag_11.io_size,), Ubyte, 0, None))

	def get_info_str(self, indent=0):
		return f'TexInfoHeader [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* tex_info = {self.fmt_member(self.tex_info, indent+1)}'
		s += f'\n	* frag_01 = {self.fmt_member(self.frag_01, indent+1)}'
		s += f'\n	* frag_11 = {self.fmt_member(self.frag_11, indent+1)}'
		s += f'\n	* padding = {self.fmt_member(self.padding, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s
