import logging
import os
import shutil
import tempfile

from generated.formats.dds import DdsFile
from generated.formats.dds.enum.DxgiFormat import DxgiFormat
from generated.formats.ovl.versions import *
from generated.formats.tex.compound.TexHeader import TexHeader
from modules.formats.BaseFormat import MemStructLoader, BaseFile
from modules.helpers import split_path

from ovl_util import texconv, imarray


def align_to(width, comp, alignment=64):
	"""Return input padded to the next closer multiple of alignment"""
	# get bpp from compression type
	if "BC1" in comp or "BC4" in comp:
		alignment *= 2
	# print("alignment",alignment)
	m = width % alignment
	if m:
		return width + alignment - m
	return width


class TexturestreamLoader(BaseFile):
	extension = ".texturestream"

	def create(self):
		# this is only to be called from DdsLoader
		self.create_root_entry()
		self.write_data_to_pool(self.root_entry.struct_ptr, 3, b"\x00" * 8)
		# data entry, assign buffer
		self.create_data_entry((b"", ))


class DdsLoader(MemStructLoader):
	target_class = TexHeader
	extension = ".tex"

	def link_streams(self):
		"""Collect other loaders"""
		self._link_streams(f"{self.file_entry.basename}_lod{lod_i}.texturestream" for lod_i in range(3))

	def increment_buffers(self, loader, buffer_i):
		"""Linearly increments buffer indices for games that need it"""
		# create increasing buffer indices for PZ (still needed 22-05-10), JWE1
		if not is_jwe2(self.ovl):
			for buff in loader.data_entry.buffers:
				buff.index = buffer_i
				buffer_i += 1
		return buffer_i

	def create(self):
		name_ext, name, ext = split_path(self.file_entry.path)
		super().create()
		logging.debug(f"Creating image {name_ext}")
		if is_jwe(self.ovl) or is_pz(self.ovl) or is_pz16(self.ovl) or is_jwe2(self.ovl):
			# there's one empty buffer at the end!
			buffers = [b"" for _ in range(self.header.stream_count + 1)]
			# decide where to store the buffers
			static_lods = 2
			streamed_lods = len(buffers) - static_lods
			logging.info(f"buffers: {len(buffers)} streamed lods: {streamed_lods}")
			buffer_i = 0
			# generate ovs and lod names - highly idiosyncratic
			if streamed_lods == 0:
				indices = ()
			elif streamed_lods == 1:
				# 1 lod: lod0 -> L1
				# same in JWE2
				indices = ((0, 1),)
			elif streamed_lods == 2:
				# 2 lods: lod0 -> L1, lod1 -> L0
				# 22-05-10: this seems to have changed for PZ, same in JWE2
				# 2 lods: lod0 -> L0, lod1 -> L1
				indices = ((0, 0), (1, 1), )
			else:
				raise IndexError(f"Don't know how to handle more than 2 streams for {name_ext}")
			for lod_i, ovs_i in indices:
				ovs_name = f"Textures_L{ovs_i}"
				# create texturestream file - dummy_dir is ignored
				texstream_loader = self.ovl.create_file(f"dummy_dir/{name}_lod{lod_i}.texturestream", ovs_name=ovs_name)
				self.streams.append(texstream_loader)
				buffer_i = self.increment_buffers(texstream_loader, buffer_i)
			self.create_data_entry(buffers[streamed_lods:])
			self.increment_buffers(self, buffer_i)
			# ready, now inject
			self.load_image(self.file_entry.path)
		elif is_pc(self.ovl) or is_ztuac(self.ovl):
			logging.error(f"Only modern texture format supported for now!")

	def collect(self):
		super().collect()
		# print("\n", self.file_entry.name)
		# for buff in self.data_entry.buffers:
		# 	print(buff.index, buff.size)
		# for stream_loader in self.file_entry.streams:
		# 	print(stream_loader.file_entry.name)
		# 	for buff in stream_loader.data_entry.buffers:
		# 		print(buff.index, buff.size)

	def load(self, file_path):
		# this loads the tex file and updates the header
		super().load(file_path)
		self.load_image(file_path)

	def load_image(self, file_path):
		# this assumes self.header matches the specs of the tex in file_path
		logging.debug(f"Loading image {file_path}")
		tmp_dir = tempfile.mkdtemp("-cobra-tools")
		png_path = imarray.png_from_tex(file_path, tmp_dir)
		if png_path:
			self.load_png(png_path, tmp_dir)
		# elif ext == ".dds":
		# 	self.load_dds(file_path)
		shutil.rmtree(tmp_dir)

	def load_png(self, file_path, tmp_dir):
		logging.info(f"Loading PNG {file_path}")
		# convert the png into a dds, then inject that
		size_info = self.get_tex_structs()
		compression = self.header.compression_type.name
		dds_file_path = texconv.png_to_dds(
			file_path, size_info.height * size_info.array_size, tmp_dir, codec=compression, mips=size_info.num_mips)
		# inject the dds generated by texconv
		self.load_dds(dds_file_path)

	def load_dds(self, file_path):
		logging.info(f"Loading DDS {file_path}")
		size_info = self.get_tex_structs()
		# tex_d = size_info.depth
		tex_d = 1
		tex_h = size_info.height
		tex_w = size_info.width
		tex_a = size_info.array_size
		tex_w = align_to(tex_w, self.header.compression_type.name)

		# load dds
		dds_file = DdsFile()
		dds_file.load(file_path)
		self.ensure_size_match(dds_file, tex_h, tex_w, tex_d, tex_a)
		sorted_streams = self.get_sorted_streams()
		tex_buffers = self.header.buffer_infos.data
		if is_pc(self.ovl):
			for buffer, tex_header_3 in zip(sorted_streams, tex_buffers):
				dds_buff = dds_file.pack_mips_pc(tex_header_3.num_mips)
				self.overwrite_buffer(buffer, dds_buff)
		else:
			out_bytes = dds_file.pack_mips(size_info.num_mips)
			out_bytes2 = dds_file.pack_mips_new(size_info.mip_maps)
			if out_bytes != out_bytes2:
				logging.warning(f"Mip packers got different results")
			# update data in buffers according to tex header buffer specifications
			for buffer_entry, b_info in zip(sorted_streams, tex_buffers):
				self.overwrite_buffer(buffer_entry, out_bytes[b_info.offset: b_info.offset + b_info.size])
			# sanity check
			sum_of_buffers = sum(buffer.size for buffer in sorted_streams)
			if len(out_bytes) != sum_of_buffers:
				logging.warning(
					f"Packing of MipMaps failed. OVL expects {sum_of_buffers} bytes, but packing generated {len(out_bytes)} bytes.")

	def get_sorted_streams(self):
		# lod0 | lod1 | static
		# PZ assigns the buffer index for the complete struct 0 | 1 | 2, 3
		# from JWE2, buffer index for streams is 0 | 0 | 0, 1
		# the last buffer is always 0 bytes
		all_buffers = []
		for loader in sorted(self.streams, key=lambda f: f.file_entry.name):
			# seen 1 per stream
			all_buffers.extend(loader.data_entry.buffers)
		# seen 2
		all_buffers.extend(self.data_entry.buffers)
		return all_buffers

	@staticmethod
	def overwrite_buffer(buffer, dds_buff):
		if len(dds_buff) < buffer.size:
			logging.warning(f"Last {buffer.size - len(dds_buff)} bytes of DDS buffer are not overwritten!")
			dds_buff = dds_buff + buffer.data[len(dds_buff):]
		buffer.update_data(dds_buff)

	def get_tex_structs(self):
		if is_dla(self.ovl):
			return self.header
		if is_pc(self.ovl) or is_ztuac(self.ovl):
			# this corresponds to a stripped down size_info
			return self.header.buffer_infos.data[0]
		else:
			return self.header.size_info.data.data

	def extract(self, out_dir, show_temp_files, progress_callback):
		tex_paths = super().extract(out_dir, show_temp_files, progress_callback)
		tex_name = self.root_entry.name
		basename = os.path.splitext(tex_name)[0]
		dds_name = basename + ".dds"
		logging.info(f"Writing {tex_name}")

		# get joined output buffer
		buffer_data = b"".join([buffer.data for buffer in self.get_sorted_streams()])

		out_files = []
		out_files.extend(tex_paths)

		dds_file = DdsFile()
		size_info = self.get_tex_structs()
		if is_dla(self.ovl):
			dds_file.width = size_info.width
			dds_file.height = size_info.height
			dds_file.mipmap_count = size_info.num_mips
			dds_file.depth = 1
		elif is_pc(self.ovl) or is_ztuac(self.ovl):
			dds_file.width = size_info.width
			# hack until we have proper support for array_size on the image editors
			# todo - this is most assuredly not array size for ED
			dds_file.height = size_info.height  # * max(1, size_info.array_size)
			dds_file.mipmap_count = size_info.mip_index
			dds_file.depth = 1
		else:
			if not len(buffer_data) == size_info.data_size:
				logging.warning(
					f"7_1 data size ({size_info.data_size}) and actual data size of combined buffers ({len(buffer_data)}) do not match up (bug)")
			dds_file.width = size_info.width
			# hack until we have proper support for array_size on the image editors
			dds_file.height = size_info.height * size_info.array_size
			dds_file.depth = size_info.depth
			dds_file.mipmap_count = size_info.num_mips
			# todo - regenerate continous buffer data
			# buffer_datas = []
		try:
			dds_type = self.header.compression_type.name
			logging.info(self.header.compression_type)
			# account for aliases
			if dds_type.endswith(("_B", "_C")):
				dds_type = dds_type[:-2]
			dds_compression_types = ((dds_type, DxgiFormat[dds_type]),)
		except KeyError:
			dds_compression_types = [(x.name, x) for x in DxgiFormat]
			logging.warning(f"Unknown compression type {self.header.compression_type}, trying all compression types")
		logging.debug(f"dds_compression_type {dds_compression_types}")

		dds_file.buffer = buffer_data
		dds_file.linear_size = len(buffer_data)
		# write out everything for each compression type
		for dds_type, dds_value in dds_compression_types:
			# print(dds_file.width)
			# header attribs
			if not is_ztuac(self.ovl):
				dds_file.width = align_to(dds_file.width, dds_type)
	
			# dx 10 stuff
			dds_file.dx_10.dxgi_format = dds_value
	
			# start out
			dds_path = out_dir(dds_name)
			if len(dds_compression_types) > 1:
				dds_path += f"_{dds_type}.dds"
	
			# write dds
			dds_file.save(dds_path)
			# print(dds_file)
			if show_temp_files:
				out_files.append(dds_path)
	
			# convert the dds to PNG, PNG must be visible so put it in out_dir
			png_file_path = texconv.dds_to_png(dds_path, dds_file.height)
	
			if os.path.isfile(png_file_path):
				# postprocessing of the png
				out_files.extend(imarray.wrapper(png_file_path, size_info, self.ovl))
		return out_files

	def ensure_size_match(self, dds_header, tex_h, tex_w, tex_d, tex_a):
		"""Check that DDS files have the same basic size"""
		dds_h = dds_header.height
		dds_w = dds_header.width
		dds_d = dds_header.depth
		dds_a = dds_header.dx_10.array_size
	
		if dds_h * dds_w * dds_d * dds_a != tex_h * tex_w * tex_d * tex_a:
			raise AttributeError(
				f"Dimensions do not match for {self.file_entry.name}!\n\n"
				f"Dimensions: height x width x depth [array size]\n"
				f"OVL Texture: {tex_h} x {tex_w} x {tex_d} [{tex_a}]\n"
				f"Injected texture: {dds_h} x {dds_w} x {dds_d} [{dds_a}]\n\n"
				f"Make the external texture's dimensions match the OVL texture and try again!")
