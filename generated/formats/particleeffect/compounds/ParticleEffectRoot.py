from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.particleeffect.imports import name_type_map


class ParticleEffectRoot(MemStruct):

	__name__ = 'ParticleEffectRoot'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.unk_64_1 = name_type_map['Uint64'](self.context, 0, None)
		self.unk_64_2 = name_type_map['Uint64'](self.context, 0, None)
		self.unk_64_3 = name_type_map['Uint64'](self.context, 0, None)
		self.unk_64_4 = name_type_map['Uint64'](self.context, 0, None)
		self.unk_64_5 = name_type_map['Uint64'](self.context, 0, None)
		self.unk_64_6 = name_type_map['Uint64'](self.context, 0, None)
		self.unk_32_1 = name_type_map['Uint'](self.context, 0, None)
		self.unk_32_2_neg = name_type_map['Int'](self.context, 0, None)
		self.unk_32_3 = name_type_map['Uint'](self.context, 0, None)
		self.unk_32_4 = name_type_map['Uint'](self.context, 0, None)
		self.a_unk_32_1 = name_type_map['Uint'](self.context, 0, None)
		self.a_unk_32_2 = name_type_map['Uint'](self.context, 0, None)
		self.a_unk_32_3_1 = name_type_map['Uint'](self.context, 0, None)
		self.a_unk_32_4 = name_type_map['Uint'](self.context, 0, None)
		self.atlasinfo_count = name_type_map['Uint64'](self.context, 0, None)
		self.next_row_1 = name_type_map['NextRow1'](self.context, 0, None)
		self.effect_00 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_01 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_02 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_03 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_04 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_05 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_06 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_07 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect07'])
		self.effect_08 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect08'])
		self.effect_09 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect09'])
		self.effect_10 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect10'])
		self.effect_11 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_12 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_13 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_14 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_15 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_16 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_17 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_18 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_19 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_20 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_21 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_22 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_23 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_24 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_25 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.effect_26 = name_type_map['EffectRef'](self.context, 0, name_type_map['Effect'])
		self.next_row_5 = name_type_map['LastRow'](self.context, 0, None)
		self.name_foreach_textures = name_type_map['ArrayPointer'](self.context, self.atlasinfo_count, name_type_map['TextureData'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'unk_64_1', name_type_map['Uint64'], (0, None), (False, None), (None, None)
		yield 'unk_64_2', name_type_map['Uint64'], (0, None), (False, None), (None, None)
		yield 'unk_64_3', name_type_map['Uint64'], (0, None), (False, None), (None, None)
		yield 'unk_64_4', name_type_map['Uint64'], (0, None), (False, None), (None, None)
		yield 'unk_64_5', name_type_map['Uint64'], (0, None), (False, None), (None, None)
		yield 'unk_64_6', name_type_map['Uint64'], (0, None), (False, None), (None, None)
		yield 'unk_32_1', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'unk_32_2_neg', name_type_map['Int'], (0, None), (False, None), (None, None)
		yield 'unk_32_3', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'unk_32_4', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'a_unk_32_1', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'a_unk_32_2', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'a_unk_32_3_1', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'a_unk_32_4', name_type_map['Uint'], (0, None), (False, None), (None, None)
		yield 'atlasinfo_count', name_type_map['Uint64'], (0, None), (False, None), (None, None)
		yield 'name_foreach_textures', name_type_map['ArrayPointer'], (None, name_type_map['TextureData']), (False, None), (None, None)
		yield 'next_row_1', name_type_map['NextRow1'], (0, None), (False, None), (None, None)
		yield 'effect_00', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_01', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_02', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_03', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_04', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_05', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_06', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_07', name_type_map['EffectRef'], (0, name_type_map['Effect07']), (False, None), (None, None)
		yield 'effect_08', name_type_map['EffectRef'], (0, name_type_map['Effect08']), (False, None), (None, None)
		yield 'effect_09', name_type_map['EffectRef'], (0, name_type_map['Effect09']), (False, None), (None, None)
		yield 'effect_10', name_type_map['EffectRef'], (0, name_type_map['Effect10']), (False, None), (None, None)
		yield 'effect_11', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_12', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_13', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_14', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_15', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_16', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_17', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_18', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_19', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_20', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_21', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_22', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_23', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_24', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_25', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'effect_26', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None), (None, None)
		yield 'next_row_5', name_type_map['LastRow'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'unk_64_1', name_type_map['Uint64'], (0, None), (False, None)
		yield 'unk_64_2', name_type_map['Uint64'], (0, None), (False, None)
		yield 'unk_64_3', name_type_map['Uint64'], (0, None), (False, None)
		yield 'unk_64_4', name_type_map['Uint64'], (0, None), (False, None)
		yield 'unk_64_5', name_type_map['Uint64'], (0, None), (False, None)
		yield 'unk_64_6', name_type_map['Uint64'], (0, None), (False, None)
		yield 'unk_32_1', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_32_2_neg', name_type_map['Int'], (0, None), (False, None)
		yield 'unk_32_3', name_type_map['Uint'], (0, None), (False, None)
		yield 'unk_32_4', name_type_map['Uint'], (0, None), (False, None)
		yield 'a_unk_32_1', name_type_map['Uint'], (0, None), (False, None)
		yield 'a_unk_32_2', name_type_map['Uint'], (0, None), (False, None)
		yield 'a_unk_32_3_1', name_type_map['Uint'], (0, None), (False, None)
		yield 'a_unk_32_4', name_type_map['Uint'], (0, None), (False, None)
		yield 'atlasinfo_count', name_type_map['Uint64'], (0, None), (False, None)
		yield 'name_foreach_textures', name_type_map['ArrayPointer'], (instance.atlasinfo_count, name_type_map['TextureData']), (False, None)
		yield 'next_row_1', name_type_map['NextRow1'], (0, None), (False, None)
		yield 'effect_00', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_01', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_02', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_03', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_04', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_05', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_06', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_07', name_type_map['EffectRef'], (0, name_type_map['Effect07']), (False, None)
		yield 'effect_08', name_type_map['EffectRef'], (0, name_type_map['Effect08']), (False, None)
		yield 'effect_09', name_type_map['EffectRef'], (0, name_type_map['Effect09']), (False, None)
		yield 'effect_10', name_type_map['EffectRef'], (0, name_type_map['Effect10']), (False, None)
		yield 'effect_11', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_12', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_13', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_14', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_15', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_16', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_17', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_18', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_19', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_20', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_21', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_22', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_23', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_24', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_25', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'effect_26', name_type_map['EffectRef'], (0, name_type_map['Effect']), (False, None)
		yield 'next_row_5', name_type_map['LastRow'], (0, None), (False, None)
