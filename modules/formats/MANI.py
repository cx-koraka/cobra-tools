import logging
import os
import struct

from generated.formats.manis.compounds.ManisRoot import ManisRoot
from generated.formats.manis import ManisFile
from modules.formats.BaseFormat import BaseFile, MemStructLoader
from modules.helpers import as_bytes


class ManiLoader(BaseFile):
	extension = ".mani"
	can_extract = False

	def create(self, file_path):
		self.root_ptr = (None, 0)


class ManisLoader(MemStructLoader):
	extension = ".manis"
	target_class = ManisRoot
				
	def extract(self, out_dir):
		name = self.name
		logging.info(f"Writing {name}")
		if not self.data_entry:
			raise AttributeError(f"No data entry for {name}")

		# root gives general info
		# buffer 0 - all mani infos
		# buffer 1 - list of hashes and zstrs for each bone name
		# buffer 2 - actual keys
		out_path = out_dir(name)
		with open(out_path, 'wb') as outfile:
			outfile.write(struct.pack("<II", self.mime_version, len(self.children)))
			for mani in self.children:
				outfile.write(as_bytes(mani.basename))
			outfile.write(as_bytes(self.header))
			for buff in self.data_entry.buffers:
				outfile.write(buff.data)
			# JWE2 can now have a secondary data entry holding a buffer 2 in an ovs
			for ovs_name, ext_data in self.data_entries.items():
				if ovs_name != "STATIC":
					logging.debug(f"Extracting from {ovs_name}")
					for buff in ext_data.buffers:
						outfile.write(buff.data)
	
		# for i, buff in enumerate(self.data_entry.buffers):
		# 	with open(out_path+str(i), 'wb') as outfile:
		# 		outfile.write(buff.data)
	
		return out_path,

	def create(self, file_path):
		manis_file, root_data, b0, b1, b2 = self._get_data(file_path)
		ms2_dir = os.path.dirname(file_path)

		# create mani files
		for mani_name in manis_file.names:
			mani_path = os.path.join(ms2_dir, mani_name+".mani")
			mani_loader = self.ovl.create_file(mani_path)
			self.children.append(mani_loader)

		self.write_root_bytes(root_data)
		self.create_data_entry((b0, b1, b2))

	def _get_data(self, file_path):
		"""Loads and returns the data for a manis"""
		manis_file = ManisFile()
		manis_file.load(file_path)
		return manis_file, as_bytes(manis_file.header), \
			as_bytes(manis_file.mani_infos), as_bytes(manis_file.name_buffer), \
			as_bytes(manis_file.keys_buffer)
