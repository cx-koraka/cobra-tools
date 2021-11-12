import struct
from modules.formats.BaseFormat import BaseFile


class MatlayersLoader(BaseFile):

	def collect(self):
		self.assign_ss_entry()
		print("\nMatlayers:", self.sized_str_entry.name)

		# Sized string initpos = position of first fragment for matcol
		self.sized_str_entry.fragments = self.ovs.frags_from_pointer(self.sized_str_entry.pointers[0], 2)
		self.sized_str_entry.f0, self.sized_str_entry.f1 = self.sized_str_entry.fragments

		shader = bytearray(self.sized_str_entry.f0.pointers[1].data)
		print(shader)
		# decode the names
		for i in range(len(shader)):
			shader[i] = max(0, shader[i]-1)
		print(shader)
		# print(self.sized_str_entry.f0)
		# 0,0,collection count,0, 0,0,
		# print(self.sized_str_entry.f1.pointers[0].data, len(self.sized_str_entry.f1.pointers[0].data))
		f0_d0 = struct.unpack("<6I", self.sized_str_entry.f1.pointers[0].data)

		layer_count = f0_d0[2]
		byte_size = 16 + ((layer_count - 1) * 24)
		print(f0_d0, byte_size)
		self.sized_str_entry.tex_frags = self.ovs.frags_accumulate_from_pointer(
			self.sized_str_entry.f1.pointers[1], byte_size)

		# layer_count = f0_d0[2]
		# print(f0_d0)
		# self.sized_str_entry.tex_frags = self.ovs.frags_from_pointer(self.sized_str_entry.f1.pointers[1],
		# 															 layer_count)

		for tex in self.sized_str_entry.tex_frags:
			# p0 is just 1 or 0, but weird since 8 and 16 bytes alternate
			# first is fgm name, second layer identity name
			# b'Swatch_Thero_TRex_LumpySkin\x00'
			# b'Ichthyosaurus_Layer_01\x00'
			print(tex.pointers[1].data)
			tex.name = self.sized_str_entry.name


class MatvarsLoader(BaseFile):

	def collect(self):
		self.assign_ss_entry()
		print("\nMatvars:", self.sized_str_entry.name)

		# Sized string initpos = position of first fragment for matcol
		self.sized_str_entry.fragments = self.ovs.frags_from_pointer(self.sized_str_entry.pointers[0], 2)
		self.sized_str_entry.f0, self.sized_str_entry.f1 = self.sized_str_entry.fragments

		print(self.sized_str_entry.f0.pointers[1].data)
		# print(self.sized_str_entry.f0)
		# 0,0,collection count,0, 0,0,
		# print(self.sized_str_entry.f1.pointers[0].data, len(self.sized_str_entry.f1.pointers[0].data))
		f0_d0 = struct.unpack("<6I", self.sized_str_entry.f1.pointers[0].data)
		layer_count = f0_d0[2] - 1
		print(f0_d0)
		self.sized_str_entry.tex_frags = self.ovs.frags_from_pointer(self.sized_str_entry.f1.pointers[1],
																	 layer_count)
		for tex in self.sized_str_entry.tex_frags:
			# p0 is just 1 or 0, but weird since 8 and 16 bytes alternate
			# first is fgm name, second layer identity name
			# b'Swatch_Thero_TRex_LumpySkin\x00'
			# b'Ichthyosaurus_Layer_01\x00'
			print(tex.pointers[1].data)
			tex.name = self.sized_str_entry.name


class MateffsLoader(BaseFile):

	def collect(self):
		self.assign_ss_entry()
		print("\nMateffs:", self.sized_str_entry.name)

		# Sized string initpos = position of first fragment for matcol
		self.sized_str_entry.fragments = self.ovs.frags_from_pointer(self.sized_str_entry.pointers[0], 1)
		self.sized_str_entry.f0 = self.sized_str_entry.fragments[0]

		print(self.sized_str_entry.f0.pointers[1].data)
		print(self.sized_str_entry.f0.pointers[0].data)
	# print(self.sized_str_entry.f0)
	# 0,0,collection count,0, 0,0,
	# print(self.sized_str_entry.f1.pointers[0].data, len(self.sized_str_entry.f1.pointers[0].data))
	# f0_d0 = struct.unpack("<6I", self.sized_str_entry.f1.pointers[0].data)
	# layer_count = f0_d0[2] - 1
	# print(f0_d0)
	# self.sized_str_entry.tex_frags = self.ovs.frags_from_pointer(self.sized_str_entry.f1.pointers[1],
	#															 layer_count)
	# for tex in self.sized_str_entry.tex_frags:
	# p0 is just 1 or 0, but weird since 8 and 16 bytes alternate
	# first is fgm name, second layer identity name
	# b'Swatch_Thero_TRex_LumpySkin\x00'
	# b'Ichthyosaurus_Layer_01\x00'
	# print(tex.pointers[1].data)
	# tex.name = self.sized_str_entry.name


class MatpatsLoader(BaseFile):

	def collect(self):
		self.assign_ss_entry()
		print("\nMatpats:", self.sized_str_entry.name)

		# Sized string initpos = position of first fragment for matcol
		self.sized_str_entry.fragments = self.ovs.frags_from_pointer(self.sized_str_entry.pointers[0], 1)
		self.sized_str_entry.f0 = self.sized_str_entry.fragments[0]

		print(self.sized_str_entry.f0.pointers[1].data)
		# print(self.sized_str_entry.f0)
		# 0,0,collection count,0, 0,0,
		# print(self.sized_str_entry.f1.pointers[0].data, len(self.sized_str_entry.f1.pointers[0].data))
		f0_d0 = struct.unpack("<4I", self.sized_str_entry.f0.pointers[0].data)
		layer_count = f0_d0[2]
		print(f0_d0)
		self.sized_str_entry.fragments.extend(
			self.ovs.frags_from_pointer(self.sized_str_entry.pointers[0], layer_count * 2))

		self.sized_str_entry.f1 = self.sized_str_entry.fragments[1]
		self.sized_str_entry.f2 = self.sized_str_entry.fragments[2]
		print(self.sized_str_entry.f1.pointers[1].data)
		f2_d0 = struct.unpack("<6I", self.sized_str_entry.f2.pointers[0].data)
		layer_count2 = f2_d0[2] - 1
		print(f2_d0)

		self.sized_str_entry.tex_frags = self.ovs.frags_from_pointer(self.sized_str_entry.f2.pointers[1], layer_count2)

		# print(self.sized_str_entry.fragments)
		for tex in self.sized_str_entry.tex_frags:
			# p0 is just 1 or 0, but weird since 8 and 16 bytes alternate
			# first is fgm name, second layer identity name
			# b'Swatch_Thero_TRex_LumpySkin\x00'
			# b'Ichthyosaurus_Layer_01\x00'
			print(tex.pointers[1].data)
			tex.name = self.sized_str_entry.name
