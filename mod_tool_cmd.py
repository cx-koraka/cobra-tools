#!/usr/bin/env python3

# Filename: mod_tool_cmd.py

"""Mod Packing tool - Command line version"""

import sys
import os
import shutil
import pathlib
import logging

from ovl_util.config import logging_setup, get_version_str, get_commit_str

logging_setup("mod_tool_cmd")
logging.info(f"Running python {sys.version}")
logging.info(f"Running cobra-tools {get_version_str()}, {get_commit_str()}")

from ovl_util.widgets import OvlReporter
from generated.formats.ovl import games, set_game

__version__ = '0.1'
__author__ = 'Open-Naja'

def unpack_ovl(file, gamestr, pathsrc, pathdst):
	srcbasepath = pathsrc
	dstbasepath = pathdst
	dstfolder = os.path.relpath(file, dstbasepath)
	logging.info(f"Unpacking {dstfolder}")
	filename = os.path.splitext(os.path.basename(dstfolder))[0]
	srcfolder = os.path.join(srcbasepath, os.path.dirname(dstfolder), filename)

	if not os.path.exists(srcfolder):
		logging.info(srcfolder)
		os.makedirs(srcfolder)

	ovl_data = OvlReporter()
	ovl_data.load(file)
	out_paths, error_files = ovl_data.extract(srcfolder, show_temp_files=False)


def get_dst_file_list(basepath=''):

	file_list = list()
	for (dirpath, dirnames, filenames) in os.walk(basepath):
		file_list += [os.path.join(dirpath, file) for file in filenames]

	return file_list

def unpack_mod(gamestr, pathsrc, pathdst):
	srcbasepath = pathsrc
	dstbasepath = pathdst
	if not srcbasepath or not dstbasepath:
		return

	logging.info("Unpacking mod")
	dstfiles = get_dst_file_list(dstbasepath)
	for file in dstfiles:
		# ignore all other files, unpack ovl files only.
		if file.lower().endswith(".ovl"):
			unpack_ovl(file, gamestr, pathsrc, pathdst)
			continue

	# The previous loop will not copy Manifest.xml and Readme.md files if any
	copy_file(dstbasepath, srcbasepath, "Manifest.xml")
	copy_file(dstbasepath, srcbasepath, "Readme.md")
	copy_file(dstbasepath, srcbasepath, "License")


def create_ovl(gamestr, ovl_dir, dst_file):
	# clear the ovl
	ovl_data = OvlReporter()

	set_game(ovl_data.context, gamestr)
	set_game(ovl_data, gamestr)

	try:
		ovl_data.create(ovl_dir)
		ovl_data.save(dst_file)
		return True
	except:
		logging.exception(f"Could not create OVL from {ovl_dir}")
		return False


# relative path
def pack_folder(folder, gamestr, pathsrc, pathdst):
	logging.info(f"Packing {folder}")
	srcbasepath = pathsrc
	dstbasepath = pathdst

	if not srcbasepath:
		logging.warning(f"Source must be set")
		return
	src_path = os.path.join(srcbasepath, folder)
	dst_file = os.path.join(dstbasepath, folder) + ".ovl"
	dst_path = os.path.dirname(dst_file)
	if not os.path.exists(dst_path):
		os.makedirs(dst_path)

	create_ovl(gamestr, src_path, dst_file)


def get_src_folder_list(basepath=''):

	root = pathlib.Path(basepath)
	non_empty_dirs = {os.path.relpath(str(p.parent), basepath) for p in root.rglob('*') if p.is_file()}

	return non_empty_dirs

def copy_file(srcpath, dstpath, fname):
	try:
		shutil.copyfile(os.path.join(srcpath, fname), os.path.join(dstpath, fname))
	except:
		logging.info(f"error copying: {fname}")


def pack_mod(gamestr, pathsrc, pathdst):
	logging.info("Packing mod")
	subfolders = get_src_folder_list(pathsrc)
	for folder in subfolders:
		# ignore the project root for packing
		if folder == '.':
			# logging.info(f"Skipping {folder}: root")
			continue
		print(f"processing: {folder}")			
		pack_folder(folder, gamestr, pathsrc, pathdst)

	# Also copy Manifest.xml and Readme.md files if any
	srcbasepath = pathsrc
	dstbasepath = pathdst
	copy_file(srcbasepath, dstbasepath, "Manifest.xml")
	copy_file(srcbasepath, dstbasepath, "Readme.md")
	copy_file(srcbasepath, dstbasepath, "License")


def usage(msg):
	print(f"{msg}\n")
	print("Usage: mod_tool_cmd.py GAMESTR ACTION folder/src folder/dst\n")
	print("GAMESTR is one of the following:")
	print("  - Disneyland Adventure")
	print("  - Jurassic World Evolution")
	print("  - Jurassic World Evolution 2")
	print("  - Planet Coaster")
	print("  - Planet Zoo")
	print("  - Planet Zoo pre-1.6")
	print("  - Zoo Tycoon Ultimate Animal Collection")
	print("  - Unknown Game")
	print("ACTION is one of the following:")
	print("  - PACK")
	print("  - UNPACK")
	print("* UNPACK will extract from folder/dst into folder/src")
	exit()

if __name__ == '__main__':

	if len( sys.argv ) < 4:
		usage("Wrong number of arguments.")

	gamestr = sys.argv[1]
	action  = sys.argv[2]
	pathsrc = sys.argv[3]
	pathdst = sys.argv[4]

	if gamestr not in games._value2member_map_:
		usage("Wrong game string")

	if action.lower() not in ['pack', 'unpack']:
		usage("Wrong action")

	if not os.path.isdir(pathsrc):
		usage("Wrong source path")

	if not os.path.isdir(pathdst):
		usage("Wrong destination path")

	if action.lower() == 'pack':
		pack_mod(gamestr, pathsrc, pathdst)

	if action.lower() == 'unpack':
		unpack_mod(gamestr, pathsrc, pathdst)

	print("done.\n\n")
