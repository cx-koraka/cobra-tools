from generated.formats.wsm.compound.WsmHeader import WsmHeader
from modules.formats.BaseFormat import MemStructLoader


class WsmLoader(MemStructLoader):
	extension = ".wsm"
	target_class = WsmHeader

	# def extract(self, out_dir, progress_callback):
	# 	name = self.root_entry.name
	# 	logging.info(f"Writing {name}")
	# 	ovl_header = self.pack_header(b"WSM ")
	#
	# 	out_path = out_dir(name)
	# 	with open(out_path, 'wb') as outfile:
	# 		outfile.write(ovl_header)
	# 		outfile.write(self.root_entry.struct_ptr.data)
	# 		for f in self.fragments:
	# 			outfile.write(f.link_ptr.data)
