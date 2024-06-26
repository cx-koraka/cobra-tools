from generated.array import Array
from generated.formats.janitorsettings.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class JanitorSettingsRoot(MemStruct):

	"""
	PC: 272 bytes
	PZ: 304 bytes
	
	huge batch of arrays at the head of the file
	todo pz has different data types for the arrays
	"""

	__name__ = 'JanitorSettingsRoot'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.a = name_type_map['Float'].from_value(1.0)
		self.b = name_type_map['Float'].from_value(0.5)
		self.c = name_type_map['Uint64'].from_value(0)
		self.d = name_type_map['Float'].from_value(0.2)
		self.e = name_type_map['Float'].from_value(1.0)
		self.f = name_type_map['Float'].from_value(1.0)
		self.g = name_type_map['Float'].from_value(1.0)
		self.h = name_type_map['Float'].from_value(0.0)
		self.i = name_type_map['Float'].from_value(1.0)
		self.unk_0 = name_type_map['Float'].from_value(0.9)
		self.unk_1 = name_type_map['Float'].from_value(1.1)
		self.unk_2 = name_type_map['Float'].from_value(0.25)
		self.extra_f_pz_1 = name_type_map['Float'](self.context, 0, None)
		self.extra_f_pz_2 = name_type_map['Float'](self.context, 0, None)
		self.unk_3 = name_type_map['Float'].from_value(-0.02)
		self.unk_4 = name_type_map['Float'](self.context, 0, None)
		self.unk_5 = name_type_map['Float'](self.context, 0, None)
		self.unk_6 = name_type_map['Float'](self.context, 0, None)
		self.unk_7 = name_type_map['Float'](self.context, 0, None)
		self.unk_8 = name_type_map['Uint'](self.context, 0, None)
		self.unk_9 = name_type_map['Float'](self.context, 0, None)
		self.unk_10 = name_type_map['Float'](self.context, 0, None)
		self.count_0 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_1 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_2 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_3 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_4 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_5 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_6 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_7 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_8 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_9 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_10 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_11 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_12 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_13 = name_type_map['Ubyte'](self.context, 0, None)
		self.count_14 = name_type_map['Ubyte'](self.context, 0, None)
		self.padding = Array(self.context, 0, None, (0,), name_type_map['Ubyte'])
		self.unk_11 = name_type_map['Float'].from_value(4.0)
		self.unk_12 = name_type_map['Float'].from_value(8.0)
		self.unk_13 = name_type_map['Float'](self.context, 0, None)
		self.unk_14 = name_type_map['Float'](self.context, 0, None)
		self.unk_15 = name_type_map['Float'](self.context, 0, None)
		self.unk_16 = name_type_map['Float'](self.context, 0, None)
		self.unk_17 = name_type_map['Float'](self.context, 0, None)
		self.unk_18 = name_type_map['Float'](self.context, 0, None)
		self.unk_19 = name_type_map['Float'](self.context, 0, None)
		self.unk_20 = name_type_map['Float'](self.context, 0, None)
		self.unk_21 = name_type_map['Float'](self.context, 0, None)
		self.unk_22 = name_type_map['Float'](self.context, 0, None)
		self.unk_23 = name_type_map['Float'](self.context, 0, None)
		self.unk_24 = name_type_map['Float'](self.context, 0, None)
		self.unk_25 = name_type_map['Float'](self.context, 0, None)
		self.unk_26 = name_type_map['Float'](self.context, 0, None)
		self.unk_27 = name_type_map['Float'](self.context, 0, None)
		self.unk_28 = name_type_map['Float'](self.context, 0, None)
		self.unk_29 = name_type_map['Float'](self.context, 0, None)
		self.unk_30 = name_type_map['Float'](self.context, 0, None)
		self.unk_31 = name_type_map['Float'](self.context, 0, None)
		self.unk_32 = name_type_map['Float'](self.context, 0, None)
		self.array_0 = name_type_map['ArrayPointer'](self.context, self.count_0, name_type_map['UIntPair'])
		self.array_1 = name_type_map['ArrayPointer'](self.context, self.count_1, name_type_map['UIntPair'])
		self.array_2 = name_type_map['ArrayPointer'](self.context, self.count_2, name_type_map['UIntPair'])
		self.array_3 = name_type_map['ArrayPointer'](self.context, self.count_3, name_type_map['UIntPair'])
		self.array_4 = name_type_map['ArrayPointer'](self.context, self.count_4, name_type_map['UIntPair'])
		self.array_5 = name_type_map['ArrayPointer'](self.context, self.count_5, name_type_map['UIntPair'])
		self.array_6 = name_type_map['ArrayPointer'](self.context, self.count_6, name_type_map['Uint'])
		self.array_7 = name_type_map['ArrayPointer'](self.context, self.count_7, name_type_map['Uint'])
		self.array_8 = name_type_map['ArrayPointer'](self.context, self.count_8, name_type_map['Uint'])
		self.array_9 = name_type_map['ArrayPointer'](self.context, self.count_9, name_type_map['Float'])
		self.array_10 = name_type_map['ArrayPointer'](self.context, self.count_10, name_type_map['Float'])
		self.array_11 = name_type_map['ArrayPointer'](self.context, self.count_11, name_type_map['Float'])
		self.array_12 = name_type_map['ArrayPointer'](self.context, self.count_12, name_type_map['Float'])
		self.array_13 = name_type_map['ArrayPointer'](self.context, self.count_13, name_type_map['Float'])
		self.array_14 = name_type_map['ArrayPointer'](self.context, self.count_14, name_type_map['Float'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'array_0', name_type_map['ArrayPointer'], (None, name_type_map['UIntPair']), (False, None), (None, None)
		yield 'array_1', name_type_map['ArrayPointer'], (None, name_type_map['UIntPair']), (False, None), (None, None)
		yield 'a', name_type_map['Float'], (0, None), (False, 1.0), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'b', name_type_map['Float'], (0, None), (False, 0.5), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'c', name_type_map['Uint64'], (0, None), (False, 0), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'd', name_type_map['Float'], (0, None), (False, 0.2), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'e', name_type_map['Float'], (0, None), (False, 1.0), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'f', name_type_map['Float'], (0, None), (False, 1.0), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'g', name_type_map['Float'], (0, None), (False, 1.0), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'h', name_type_map['Float'], (0, None), (False, 0.0), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'i', name_type_map['Float'], (0, None), (False, 1.0), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'array_2', name_type_map['ArrayPointer'], (None, name_type_map['UIntPair']), (False, None), (None, None)
		yield 'array_3', name_type_map['ArrayPointer'], (None, name_type_map['UIntPair']), (False, None), (None, None)
		yield 'array_4', name_type_map['ArrayPointer'], (None, name_type_map['UIntPair']), (False, None), (None, None)
		yield 'array_5', name_type_map['ArrayPointer'], (None, name_type_map['UIntPair']), (False, None), (None, None)
		yield 'array_6', name_type_map['ArrayPointer'], (None, name_type_map['Uint']), (False, None), (None, None)
		yield 'array_7', name_type_map['ArrayPointer'], (None, name_type_map['Uint']), (False, None), (None, None)
		yield 'array_8', name_type_map['ArrayPointer'], (None, name_type_map['Uint']), (False, None), (None, None)
		yield 'array_9', name_type_map['ArrayPointer'], (None, name_type_map['Float']), (False, None), (None, None)
		yield 'array_10', name_type_map['ArrayPointer'], (None, name_type_map['Float']), (False, None), (None, None)
		yield 'array_11', name_type_map['ArrayPointer'], (None, name_type_map['Float']), (False, None), (None, None)
		yield 'array_12', name_type_map['ArrayPointer'], (None, name_type_map['Float']), (False, None), (None, None)
		yield 'array_13', name_type_map['ArrayPointer'], (None, name_type_map['Float']), (False, None), (lambda context: context.version == 18, None)
		yield 'array_14', name_type_map['ArrayPointer'], (None, name_type_map['Float']), (False, None), (lambda context: context.version == 18, None)
		yield 'unk_0', name_type_map['Float'], (0, None), (False, 0.9), (None, None)
		yield 'unk_1', name_type_map['Float'], (0, None), (False, 1.1), (None, None)
		yield 'unk_2', name_type_map['Float'], (0, None), (False, 0.25), (None, None)
		yield 'extra_f_pz_1', name_type_map['Float'], (0, None), (False, None), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'extra_f_pz_2', name_type_map['Float'], (0, None), (False, None), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'unk_3', name_type_map['Float'], (0, None), (False, -0.02), (None, None)
		yield 'unk_4', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_5', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_6', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_7', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_8', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'unk_9', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_10', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'count_0', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_1', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_2', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_3', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_4', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_5', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_6', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_7', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_8', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_9', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_10', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_11', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_12', name_type_map['Ubyte'], (0, None), (False, None), (None, None)
		yield 'count_13', name_type_map['Ubyte'], (0, None), (False, None), (lambda context: context.version == 18, None)
		yield 'count_14', name_type_map['Ubyte'], (0, None), (False, None), (lambda context: context.version == 18, None)
		yield 'padding', Array, (0, None, (7,), name_type_map['Ubyte']), (False, None), (lambda context: (not context.user_version.use_djb) and (context.version >= 19), None)
		yield 'padding', Array, (0, None, (5,), name_type_map['Ubyte']), (False, None), (lambda context: context.version == 18, None)
		yield 'unk_11', name_type_map['Float'], (0, None), (False, 4.0), (None, None)
		yield 'unk_12', name_type_map['Float'], (0, None), (False, 8.0), (None, None)
		yield 'unk_13', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_14', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_15', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_16', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_17', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_18', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_19', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_20', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_21', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_22', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_23', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_24', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_25', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_26', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_27', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_28', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_29', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_30', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_31', name_type_map['Float'], (0, None), (False, None), (None, None)
		yield 'unk_32', name_type_map['Float'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'array_0', name_type_map['ArrayPointer'], (instance.count_0, name_type_map['UIntPair']), (False, None)
		yield 'array_1', name_type_map['ArrayPointer'], (instance.count_1, name_type_map['UIntPair']), (False, None)
		if (not instance.context.user_version.use_djb) and (instance.context.version >= 19):
			yield 'a', name_type_map['Float'], (0, None), (False, 1.0)
			yield 'b', name_type_map['Float'], (0, None), (False, 0.5)
			yield 'c', name_type_map['Uint64'], (0, None), (False, 0)
			yield 'd', name_type_map['Float'], (0, None), (False, 0.2)
			yield 'e', name_type_map['Float'], (0, None), (False, 1.0)
			yield 'f', name_type_map['Float'], (0, None), (False, 1.0)
			yield 'g', name_type_map['Float'], (0, None), (False, 1.0)
			yield 'h', name_type_map['Float'], (0, None), (False, 0.0)
			yield 'i', name_type_map['Float'], (0, None), (False, 1.0)
		yield 'array_2', name_type_map['ArrayPointer'], (instance.count_2, name_type_map['UIntPair']), (False, None)
		yield 'array_3', name_type_map['ArrayPointer'], (instance.count_3, name_type_map['UIntPair']), (False, None)
		yield 'array_4', name_type_map['ArrayPointer'], (instance.count_4, name_type_map['UIntPair']), (False, None)
		yield 'array_5', name_type_map['ArrayPointer'], (instance.count_5, name_type_map['UIntPair']), (False, None)
		yield 'array_6', name_type_map['ArrayPointer'], (instance.count_6, name_type_map['Uint']), (False, None)
		yield 'array_7', name_type_map['ArrayPointer'], (instance.count_7, name_type_map['Uint']), (False, None)
		yield 'array_8', name_type_map['ArrayPointer'], (instance.count_8, name_type_map['Uint']), (False, None)
		yield 'array_9', name_type_map['ArrayPointer'], (instance.count_9, name_type_map['Float']), (False, None)
		yield 'array_10', name_type_map['ArrayPointer'], (instance.count_10, name_type_map['Float']), (False, None)
		yield 'array_11', name_type_map['ArrayPointer'], (instance.count_11, name_type_map['Float']), (False, None)
		yield 'array_12', name_type_map['ArrayPointer'], (instance.count_12, name_type_map['Float']), (False, None)
		if instance.context.version == 18:
			yield 'array_13', name_type_map['ArrayPointer'], (instance.count_13, name_type_map['Float']), (False, None)
			yield 'array_14', name_type_map['ArrayPointer'], (instance.count_14, name_type_map['Float']), (False, None)
		yield 'unk_0', name_type_map['Float'], (0, None), (False, 0.9)
		yield 'unk_1', name_type_map['Float'], (0, None), (False, 1.1)
		yield 'unk_2', name_type_map['Float'], (0, None), (False, 0.25)
		if (not instance.context.user_version.use_djb) and (instance.context.version >= 19):
			yield 'extra_f_pz_1', name_type_map['Float'], (0, None), (False, None)
			yield 'extra_f_pz_2', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_3', name_type_map['Float'], (0, None), (False, -0.02)
		yield 'unk_4', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_5', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_6', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_7', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_8', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_9', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_10', name_type_map['Float'], (0, None), (False, None)
		yield 'count_0', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_1', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_2', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_3', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_4', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_5', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_6', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_7', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_8', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_9', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_10', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_11', name_type_map['Ubyte'], (0, None), (False, None)
		yield 'count_12', name_type_map['Ubyte'], (0, None), (False, None)
		if instance.context.version == 18:
			yield 'count_13', name_type_map['Ubyte'], (0, None), (False, None)
			yield 'count_14', name_type_map['Ubyte'], (0, None), (False, None)
		if (not instance.context.user_version.use_djb) and (instance.context.version >= 19):
			yield 'padding', Array, (0, None, (7,), name_type_map['Ubyte']), (False, None)
		if instance.context.version == 18:
			yield 'padding', Array, (0, None, (5,), name_type_map['Ubyte']), (False, None)
		yield 'unk_11', name_type_map['Float'], (0, None), (False, 4.0)
		yield 'unk_12', name_type_map['Float'], (0, None), (False, 8.0)
		yield 'unk_13', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_14', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_15', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_16', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_17', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_18', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_19', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_20', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_21', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_22', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_23', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_24', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_25', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_26', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_27', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_28', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_29', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_30', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_31', name_type_map['Float'], (0, None), (False, None)
		yield 'unk_32', name_type_map['Float'], (0, None), (False, None)
