from generated.formats.dds.enum.FourCC import FourCC
from generated.formats.dds.bitstruct.PixelFormatFlags import PixelFormatFlags


class PixelFormat:

	# Always 32.
	size: int = 32

	# Non-zero for DX9, zero for DX10.
	flags: PixelFormatFlags

	# Determines compression type. Zero means no compression.
	four_c_c: FourCC

	# For non-compressed types, this is either 24 or 32 depending on whether there is an alpha channel. For compressed types, this describes the number of bits per block, which can be either 256 or 512.
	bit_count: int

	# For non-compressed types, this determines the red mask. Usually 0x00FF0000. Is zero for compressed textures.
	r_mask: int

	# For non-compressed types, this determines
	# the green mask. Usually 0x0000FF00. Is zero for compressed textures.
	g_mask: int

	# For non-compressed types, this determines
	# the blue mask. Usually 0x00FF0000. Is zero for compressed textures.
	b_mask: int

	# For non-compressed types, this determines
	# the alpha mask. Usually 0x00000000 if there is no alpha channel and 0xFF000000 if there is an alpha channel. Is zero for compressed textures.
	a_mask: int

	def __init__(self, arg=None, template=None):
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.size = 32
		self.flags = 0
		self.four_c_c = 0
		self.bit_count = 0
		self.r_mask = 0
		self.g_mask = 0
		self.b_mask = 0
		self.a_mask = 0

	def read(self, stream):

		io_start = stream.tell()
		self.size = stream.read_uint()
		self.flags = stream.read_type(PixelFormatFlags)
		self.four_c_c = stream.read_type(FourCC)
		self.bit_count = stream.read_uint()
		self.r_mask = stream.read_uint()
		self.g_mask = stream.read_uint()
		self.b_mask = stream.read_uint()
		self.a_mask = stream.read_uint()

		self.io_size = stream.tell() - io_start

	def write(self, stream):

		io_start = stream.tell()
		stream.write_uint(self.size)
		stream.write_type(self.flags)
		stream.write_type(self.four_c_c)
		stream.write_uint(self.bit_count)
		stream.write_uint(self.r_mask)
		stream.write_uint(self.g_mask)
		stream.write_uint(self.b_mask)
		stream.write_uint(self.a_mask)

		self.io_size = stream.tell() - io_start

	def __repr__(self):
		s = 'PixelFormat [Size: '+str(self.io_size)+']'
		s += '\n	* size = ' + self.size.__repr__()
		s += '\n	* flags = ' + self.flags.__repr__()
		s += '\n	* four_c_c = ' + self.four_c_c.__repr__()
		s += '\n	* bit_count = ' + self.bit_count.__repr__()
		s += '\n	* r_mask = ' + self.r_mask.__repr__()
		s += '\n	* g_mask = ' + self.g_mask.__repr__()
		s += '\n	* b_mask = ' + self.b_mask.__repr__()
		s += '\n	* a_mask = ' + self.a_mask.__repr__()
		s += '\n'
		return s
