from generated.formats.manis.imports import name_type_map
import io
import logging
import struct

from generated.formats.manis.bitfields.ChannelSize import ChannelSize
from generated.formats.manis.bitfields.ManisDtype import ManisDtype
from generated.formats.manis.compounds.InfoHeader import InfoHeader
from generated.io import IoFile
import os

from ovl_util.config import logging_setup


def hex_test():
	for i in range(20):
		x = 2 ** i
		print(i, bin(i), x, bin(x))


class ManisFile(InfoHeader, IoFile):

	def __init__(self):
		super().__init__(self)

	def load(self, filepath):
		# store file name for later
		self.file = filepath
		self.dir, self.basename = os.path.split(filepath)
		self.path_no_ext = os.path.splitext(self.file)[0]

		with open(filepath, "rb") as stream:
			self.read_fields(stream, self)
			self.eoh = stream.tell()
			# print(self)
			for mi, name in zip(self.mani_infos, self.names):
				mi.name = name
				if hasattr(mi, "keys"):
					mi.keys.name = name
				# print(mi)
				assert mi.pos_bone_count == mi.pos_bone_count_repeat
				assert mi.ori_bone_count == mi.ori_bone_count_repeat
			for i, bone_name in enumerate(self.name_buffer.bone_names):
				print(i, bone_name)

	def iter_compressed_keys(self):
		for mani_info in self.mani_infos:
			logging.info(f"mani {mani_info.name} compression {mani_info.dtype.compression}")
			if hasattr(mani_info, "keys"):
				if hasattr(mani_info.keys.key_data, "repeats"):
					for i, mb in enumerate(mani_info.keys.key_data.repeats):
						yield mani_info, i, mb

	def dump_keys(self):
		for mani_info, i, mb in self.iter_compressed_keys():
			# print(binascii.hexlify(data[:40]), padding, stream.tell())
			with open(os.path.join(self.dir, f"{self.path_no_ext}_{mani_info.name}_{i}.maniskeys"), "wb") as f:
				f.write(mb.data)

	def parse_keys(self):
		for mani_info, i, mb in self.iter_compressed_keys():
			with io.BytesIO(mb.data) as f:
				channel_type = ChannelSize.from_stream(f, self.context)
				# channel_type = struct.unpack("<H", f.read(2))[0]
				logging.info(f"{channel_type}")


if __name__ == "__main__":
	logging_setup("mani")
	# for k in (0, 1, 4, 5, 6, 32, 34, 36, 37, 38, 64, 66, 68, 69, 70):
	# 	print(ManisDtype.from_value(k))
	mani = ManisFile()
	mani.load("C:/Users/arnfi/Desktop/Wheel/animation.maniset9637aeb4.manis")
	mani.dump_keys()
	mani.parse_keys()
	# # mani.load("C:/Users/arnfi/Desktop/donationbox/animation.maniseteaf333c5.manis")
	# # mani.load("C:/Users/arnfi/Desktop/kangaroo/animation.maniset32dc487b.manis")
	mani.load("C:/Users/arnfi/Desktop/gate/animation.manisetd2b36ae0.manis")
	# print(mani)
	# # mani.load("C:/Users/arnfi/Desktop/JWE2/pyro/hatcheryexitcamera.maniset8c6441b9.manis")
	mani.parse_keys()
	# mani.load("C:/Users/arnfi/Desktop/dilo/locomotion.maniset1c05e0f4.manis")
	# mani.load("C:/Users/arnfi/Desktop/ostrich/ugcres.maniset8982114c.manis")
	# mani.load("C:/Users/arnfi/Desktop/Coding/ovl/OVLs/anim test/rot_x_0_22_42.manis")
	# mani.load("C:/Users/arnfi/Desktop/Coding/ovl/OVLs/anim test/ugcres.maniset8982114c0.manis")
	# mani.load("C:/Users/arnfi/Desktop/Coding/ovl/OVLs/anim test/ugcres.maniset8982114c1.manis")
	# mani.load("C:/Users/arnfi/Desktop/Coding/ovl/OVLs/anim test/ugcres.maniset8982114c2.manis")
	# mani.load("C:/Users/arnfi/Desktop/Coding/ovl/PZ 1.6/anim/animation.maniset9637aeb4.manis")
	# mani.load("C:/Users/arnfi/Desktop/Coding/ovl/PZ 1.6/anim/animationmotionextractedbehaviour.maniset5f721adf.manis")
	# mani.load("C:/Users/arnfi/Desktop/Coding/ovl/PZ 1.6/anim/animationmotionextractedlocomotion.maniset58076276.manis")
	# mani.load("C:/Users/arnfi/Desktop/lemur/animationnotmotionextractedpartials.maniset919dac12.manis")
	# mani.load("C:/Users/arnfi/Desktop/lemur/animationmotionextractedfighting.maniset9c749130.manis")
	# mani.load("C:/Users/arnfi/Desktop/lemur/animationnotmotionextractedlocomotion.maniset87d072d8.manis")

	# mani.load("C:/Users/arnfi/Desktop/Coding/Frontier/anim/wheel/animation.maniset9637aeb4.manis")

	# mani.load("C:/Users/arnfi/Desktop/Coding/Frontier/anim/Iron_piston/ugcres.maniset8982114c.manis")
	# mani.load("C:/Users/arnfi/Desktop/Coding/Frontier/anim/pc dino/animation.maniset293c241f.manis")

	# mani.load("C:/Users/arnfi/Desktop/Coding/Frontier/anim/dilo/notmotionextracted.manisetf2b1fd43.manis")  # ok 0000 24 bytes f
	# mani.load("C:/Users/arnfi/Desktop/Coding/Frontier/anim/dilo/motionextracted.maniset1823adb0.manis")  # 0111 48 bytes f
	# mani.load("C:/Users/arnfi/Desktop/Coding/Frontier/anim/dilo/motionextracted.maniset1bfb6052.manis")  # 0, 2, 3, 1

	# mani.load("C:/Users/arnfi/Desktop/Coding/Frontier/anim/ceara/hatcheryexitcamera.maniset9762d823.manis")
	# mani.load("C:/Users/arnfi/Desktop/Coding/Frontier/anim/ceara/motionextracted.maniset7e6b0db3.manis") # keys are external
	# mani.load("C:/Users/arnfi/Desktop/Coding/Frontier/anim/ceara/motionextracted.manisetf2b6c52d.manis")
	# print(mani)

	# mani.load("C:/Users/arnfi/Desktop/manis/fee_feeder_ground.maniset2759dfaf.manis")
	# mani.load("C:/Users/arnfi/Desktop/manis/motionextracted.maniset167ed454.manis")
	# hex_test()