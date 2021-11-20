from generated.array import Array
from generated.context import ContextReference
from generated.formats.matcol.compound.AttribWrapper import AttribWrapper
from generated.formats.matcol.compound.InfoWrapper import InfoWrapper
from generated.formats.matcol.compound.LayeredAttrib import LayeredAttrib
from generated.formats.matcol.compound.LayeredInfo import LayeredInfo


class Layer:

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.name = ''
		self.info_info = LayeredInfo(self.context, 0, None)
		self.infos = Array((self.info_info.info_count), InfoWrapper, self.context, 0, None)
		self.attrib_info = LayeredAttrib(self.context, 0, None)
		self.attribs = Array((self.attrib_info.attrib_count), AttribWrapper, self.context, 0, None)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		self.name = ''
		self.info_info = LayeredInfo(self.context, 0, None)
		self.infos = Array((self.info_info.info_count), InfoWrapper, self.context, 0, None)
		self.attrib_info = LayeredAttrib(self.context, 0, None)
		self.attribs = Array((self.attrib_info.attrib_count), AttribWrapper, self.context, 0, None)

	def read(self, stream):
		self.io_start = stream.tell()
		self.name = stream.read_zstring()
		self.info_info = stream.read_type(LayeredInfo, (self.context, 0, None))
		self.infos.read(stream, InfoWrapper, self.info_info.info_count, None)
		self.attrib_info = stream.read_type(LayeredAttrib, (self.context, 0, None))
		self.attribs.read(stream, AttribWrapper, self.attrib_info.attrib_count, None)

		self.io_size = stream.tell() - self.io_start

	def write(self, stream):
		self.io_start = stream.tell()
		stream.write_zstring(self.name)
		stream.write_type(self.info_info)
		self.infos.write(stream, InfoWrapper, self.info_info.info_count, None)
		stream.write_type(self.attrib_info)
		self.attribs.write(stream, AttribWrapper, self.attrib_info.attrib_count, None)

		self.io_size = stream.tell() - self.io_start

	def get_info_str(self):
		return f'Layer [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* name = {self.name.__repr__()}'
		s += f'\n	* info_info = {self.info_info.__repr__()}'
		s += f'\n	* infos = {self.infos.__repr__()}'
		s += f'\n	* attrib_info = {self.attrib_info.__repr__()}'
		s += f'\n	* attribs = {self.attribs.__repr__()}'
		return s

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
