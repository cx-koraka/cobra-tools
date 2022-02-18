import logging
import os
import struct

from generated.formats.manis.compound.SizedStrData import SizedStrData
from generated.formats.manis import ManisFile
from modules.formats.BaseFormat import BaseFile
from modules.formats.shared import get_versions
from modules.helpers import as_bytes


class ManisLoader(BaseFile):

	def collect(self):
		self.assign_ss_entry()
				
	def extract(self, out_dir, show_temp_files, progress_callback):
		name = self.sized_str_entry.name
		logging.info(f"Writing {name}")
		if not self.sized_str_entry.data_entry:
			raise AttributeError(f"No data entry for {name}")
		ss_ptr = self.sized_str_entry.pointers[0]
		header = ss_ptr.load_as(SizedStrData)[0]
		print(header)
		# print(len(ss_data), ss_data)
		buffers = self.sized_str_entry.data_entry.buffer_datas
		# print(len(buffers))
		ovl_header = self.pack_header(b"MANI")
		manis_header = struct.pack("<I", len(self.sized_str_entry.children))
	
		# sizedstr data + 3 buffers
		# sized str data gives general info
		# buffer 0 holds all mani infos - weirdly enough, its first 10 bytes come from the sized str data!
		# buffer 1 is list of hashes and zstrs for each bone name
		# buffer 2 has the actual keys
		out_path = out_dir(name)
		with open(out_path, 'wb') as outfile:
			outfile.write(ovl_header)
			outfile.write(manis_header)
			for mani in self.sized_str_entry.children:
				outfile.write(as_bytes(mani.name))
			outfile.write(ss_ptr.data)
			for buff in self.sized_str_entry.data_entry.buffers:
				outfile.write(buff.data)
	
		# for i, buff in enumerate(self.sized_str_entry.data_entry.buffers):
		# 	with open(out_path+str(i), 'wb') as outfile:
		# 		outfile.write(buff.data)
	
		return out_path,

	def create(self):
		manis_file = ManisFile()
		manis_file.load(self.file_entry.path)
		ms2_dir = os.path.dirname(self.file_entry.path)

		manis_entry = self.create_ss_entry(self.file_entry)
		manis_entry.children = []

		versions = get_versions(self.ovl)

		# create mani files
		for mani_name in manis_file.names:
			mani_path = os.path.join(ms2_dir, mani_name+".mani")
			mani_file_entry = self.get_file_entry(mani_path)

			mani_entry = self.create_ss_entry(mani_file_entry)
			mani_entry.pointers[0].pool_index = -1
			manis_entry.children.append(mani_entry)

		# todo - is the length right, also pool type
		manis_ss_bytes = as_bytes(manis_file.header, version_info=versions)
		self.write_to_pool(manis_entry.pointers[0], 2, manis_ss_bytes)

		self.create_data_entry(manis_entry, manis_file.buffers)
