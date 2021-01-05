import os
from modules.formats.shared import djb


def dat_hasher(ovl, name_tups):
	print(f"Hashing for {name_tups}")
	ovl_lists = [ovl.files, ovl.dependencies, ovl.dirs]
	# ovl_lists = [ovl.files, ]
	ovs_lists = []
	for ovs in ovl.ovs_files:
		ovs_lists.extend((
			ovs.data_entries,
			ovs.set_header.sets,
			ovs.set_header.assets,
			ovs.header_entries,
			ovs.sized_str_entries
		 	))
	old_hash_to_new = {}
	# first go over the ovl lists to generate new hashes
	for i, entry_list in enumerate(ovl_lists):
		for entry in entry_list:
			try:
				if "bad hash" in entry.name:
					print("Skipping", entry.name, entry.file_hash)
					continue
				new_name = entry.name
				for old, new in name_tups:
					new_name = new_name.replace(old, new)
				if hasattr(entry, "file_hash"):
					new_hash = djb(new_name)
					old_hash_to_new[entry.file_hash] = (new_name, new_hash)
					print(f"List{i} {entry.name} -> {new_name},  {entry.file_hash} ->  {new_hash}")
					entry.file_hash = new_hash
				else:
					print(f"List{i} {entry.name} -> {new_name},  [NOT HASHED]")
				entry.name = new_name
			except Exception as err:
				print(err)

	# we do this in a second step to resolve the links
	for i, entry_list in enumerate(ovs_lists):
		for entry in entry_list:
			new_name, new_hash = old_hash_to_new[entry.file_hash]
			entry.file_hash = new_hash
			entry.name = f"{new_name}.{entry.ext}"

	# update the name buffer and offsets
	ovl.names.update_with((
		(ovl.dependencies, "ext"),
		(ovl.dirs, "name"),
		(ovl.mimes, "name"),
		(ovl.files, "name")
	))
	ovl.len_names = len(ovl.names.data)
	# resort the file entries
	for i, file in enumerate(ovl.files):
		file.old_index = i

	# sort the different lists according to the criteria specified
	ovl.files.sort(key=lambda x: (x.ext, x.file_hash))
	ovl.dependencies.sort(key=lambda x: x.file_hash)

	# create a lookup table to map the old indices to the new ones
	lut = {}
	for i, file in enumerate(ovl.files):
		lut[file.old_index] = i

	# update the file indices
	for dependency in ovl.dependencies:
		dependency.file_index = lut[dependency.file_index]
	for aux in ovl.aux_entries:
		aux.file_index = lut[aux.file_index]

	print("Done!")
