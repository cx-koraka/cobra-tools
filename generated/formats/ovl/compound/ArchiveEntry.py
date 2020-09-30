class ArchiveEntry:

	"""
	Description of one archive
	"""

	# offset in the header's Archive Names block
	offset: int

	# starting offset of header entries
	ovs_head_offset: int

	# starting offset of file entries
	ovs_file_offset: int

	# Total amount of headers in this archive; sum of all HeaderType.num_headers
	num_headers: int

	# Total amount of Data Entries
	num_datas: int

	# Amount of HeaderType objects at start of this deflated archive.
	num_header_types: int

	# ?
	zeros: int

	# Amount of buffers in the archive
	num_buffers: int

	# Amount of Fragments in the archive
	num_fragments: int

	# Number of files in the archive
	num_files: int

	# Seek to pos to get zlib header for this archive
	read_start: int

	# size of the set and asset entry data
	set_data_size: int

	# size of the compressed ovl dat
	compressed_size: int

	# size of the uncompressed ovl dat
	uncompressed_size: int

	# ?
	zeros_3: int

	# cumulative size of all header datas preceding this archive
	ovs_header_offset: int

	# sum of the archives header entry data blocks + the ovs header offset
	header_size: int

	# Seemingly unused, can be zeroed without effect ingame in JWE
	ovs_offset: int

	def __init__(self, arg=None, template=None):
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.offset = 0
		self.ovs_head_offset = 0
		self.ovs_file_offset = 0
		self.num_headers = 0
		self.num_datas = 0
		self.num_header_types = 0
		self.zeros = 0
		self.num_buffers = 0
		self.num_fragments = 0
		self.num_files = 0
		self.read_start = 0
		self.set_data_size = 0
		self.compressed_size = 0
		self.uncompressed_size = 0
		self.zeros_3 = 0
		self.ovs_header_offset = 0
		self.header_size = 0
		self.ovs_offset = 0

	def read(self, stream):

		io_start = stream.tell()
		self.offset = stream.read_uint()
		self.ovs_head_offset = stream.read_uint()
		self.ovs_file_offset = stream.read_uint()
		self.num_headers = stream.read_uint()
		self.num_datas = stream.read_ushort()
		self.num_header_types = stream.read_ushort()
		self.zeros = stream.read_uint()
		self.num_buffers = stream.read_uint()
		self.num_fragments = stream.read_uint()
		self.num_files = stream.read_uint()
		self.read_start = stream.read_uint()
		self.set_data_size = stream.read_uint()
		self.compressed_size = stream.read_uint()
		self.uncompressed_size = stream.read_uint()
		self.zeros_3 = stream.read_uint()
		self.ovs_header_offset = stream.read_uint()
		self.header_size = stream.read_uint()
		self.ovs_offset = stream.read_uint()

		self.io_size = stream.tell() - io_start

	def write(self, stream):

		io_start = stream.tell()
		stream.write_uint(self.offset)
		stream.write_uint(self.ovs_head_offset)
		stream.write_uint(self.ovs_file_offset)
		stream.write_uint(self.num_headers)
		stream.write_ushort(self.num_datas)
		stream.write_ushort(self.num_header_types)
		stream.write_uint(self.zeros)
		stream.write_uint(self.num_buffers)
		stream.write_uint(self.num_fragments)
		stream.write_uint(self.num_files)
		stream.write_uint(self.read_start)
		stream.write_uint(self.set_data_size)
		stream.write_uint(self.compressed_size)
		stream.write_uint(self.uncompressed_size)
		stream.write_uint(self.zeros_3)
		stream.write_uint(self.ovs_header_offset)
		stream.write_uint(self.header_size)
		stream.write_uint(self.ovs_offset)

		self.io_size = stream.tell() - io_start

	def __repr__(self):
		s = 'ArchiveEntry [Size: '+str(self.io_size)+']'
		s += '\n	* offset = ' + self.offset.__repr__()
		s += '\n	* ovs_head_offset = ' + self.ovs_head_offset.__repr__()
		s += '\n	* ovs_file_offset = ' + self.ovs_file_offset.__repr__()
		s += '\n	* num_headers = ' + self.num_headers.__repr__()
		s += '\n	* num_datas = ' + self.num_datas.__repr__()
		s += '\n	* num_header_types = ' + self.num_header_types.__repr__()
		s += '\n	* zeros = ' + self.zeros.__repr__()
		s += '\n	* num_buffers = ' + self.num_buffers.__repr__()
		s += '\n	* num_fragments = ' + self.num_fragments.__repr__()
		s += '\n	* num_files = ' + self.num_files.__repr__()
		s += '\n	* read_start = ' + self.read_start.__repr__()
		s += '\n	* set_data_size = ' + self.set_data_size.__repr__()
		s += '\n	* compressed_size = ' + self.compressed_size.__repr__()
		s += '\n	* uncompressed_size = ' + self.uncompressed_size.__repr__()
		s += '\n	* zeros_3 = ' + self.zeros_3.__repr__()
		s += '\n	* ovs_header_offset = ' + self.ovs_header_offset.__repr__()
		s += '\n	* header_size = ' + self.header_size.__repr__()
		s += '\n	* ovs_offset = ' + self.ovs_offset.__repr__()
		s += '\n'
		return s
