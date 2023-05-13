# START_GLOBALS
import logging

from generated.base_struct import BaseStruct
from generated.formats.base.compounds.PadAlign import get_padding
from generated.formats.manis.compounds.CompressedManiData import CompressedManiData
from generated.formats.manis.compounds.ManiBlock import ManiBlock
from generated.formats.manis.compounds.UnkChunkList import UnkChunkList
from modules.formats.shared import get_padding_size

# END_GLOBALS


class KeysReader(BaseStruct):

	# START_CLASS

	@classmethod
	def read_fields(cls, stream, instance):
		instance.io_start = stream.tell()
		for mani_info in instance.arg:
			print(mani_info)
			print(stream.tell())
			if mani_info.dtype != 70 and mani_info.count_a > 0 and mani_info.count_b > 0:
				try:
					mani_info.keys = ManiBlock.from_stream(stream, instance.context, mani_info, None)
					print(mani_info.keys)

					# sum_bytes = sum(mb.byte_size for mb in mani_info.keys.repeats)
					# print("sum_bytes", sum_bytes)
					# sum_bytes2 = sum(mb.byte_size + get_padding_size(mb.byte_size) for mb in mani_info.keys.repeats)
					# print("sum_bytes + padding", sum_bytes2)
					if isinstance(mani_info.keys.key_data, CompressedManiData):
						for mb in mani_info.keys.key_data.repeats:
							# print(bone_name, stream.tell())
							mb.data = stream.read(mb.byte_size)
							pad_size = get_padding_size(mb.byte_size)
							mb.padding = stream.read(pad_size)
							assert mb.padding == b"\x00" * pad_size
							# print("end", stream.tell())
					# if (mani_info.keys.count > 0) and (mani_info.dtype > 5):
						# mani_info.subchunks = UnkChunkList.from_stream(stream, instance.context, mani_info, None)
						# print(mani_info.subchunks)
					# # break
				except:
					logging.exception(f"Reading ManiBlock failed")
		instance.io_size = stream.tell() - instance.io_start

	@classmethod
	def write_fields(cls, stream, instance):
		instance.io_start = stream.tell()
		for mani_info in instance.arg:
			if mani_info.dtype != 70 and mani_info.count_a > 0 and mani_info.count_b > 0:
				ManiBlock.to_stream(mani_info.keys, stream, instance.context)
				if isinstance(mani_info.keys.key_data, CompressedManiData):
					for mb in mani_info.keys.key_data.repeats:
						stream.write(mb.data)
						stream.write(get_padding(mb.byte_size))
				# if (mani_info.keys.count > 0) and (mani_info.dtype > 5):
				# 	UnkChunkList.to_stream(mani_info.subchunks, stream, mani_info.subchunks.context)
		instance.io_size = stream.tell() - instance.io_start

	@classmethod
	def get_fields_str(cls, instance, indent=0):
		s = ''
		for mani_info in instance.arg:
			s += str(mani_info.keys)
		return s

