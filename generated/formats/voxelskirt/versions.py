from enum import Enum


def is_ztuac(inst):
	if inst.version == 17:
		return True


def set_ztuac(inst):
	inst.version = 17


def is_pc(inst):
	if inst.version == 18:
		return True


def set_pc(inst):
	inst.version = 18


def is_pz(inst):
	if inst.version == 19 and inst.user_version in (8340, 8724):
		return True


def set_pz(inst):
	inst.version = 19
	inst.user_version._value = 8340


def is_jwe(inst):
	if inst.version_flag == 1 and inst.version == 19 and inst.user_version in (24724, 25108):
		return True


def set_jwe(inst):
	inst.version_flag = 1
	inst.version = 19
	inst.user_version._value = 24724


games = Enum('Games',[('JURASSIC_WORLD_EVOLUTION', 'Jurassic World Evolution'), ('PLANET_COASTER', 'Planet Coaster'), ('PLANET_ZOO', 'Planet Zoo'), ('ZOO_TYCOON_ULTIMATE_ANIMAL_COLLECTION', 'Zoo Tycoon Ultimate Animal Collection'), ('UNKNOWN_GAME', 'Unknown Game')])


def get_game(inst):
	if is_ztuac(inst):
		return [games.ZOO_TYCOON_ULTIMATE_ANIMAL_COLLECTION]
	if is_pc(inst):
		return [games.PLANET_COASTER]
	if is_pz(inst):
		return [games.PLANET_ZOO]
	if is_jwe(inst):
		return [games.JURASSIC_WORLD_EVOLUTION]
	return [games.UNKOWN_GAME]


def set_game(inst, game):
	if game in {games.ZOO_TYCOON_ULTIMATE_ANIMAL_COLLECTION}:
		return set_ztuac(inst)
	if game in {games.PLANET_COASTER}:
		return set_pc(inst)
	if game in {games.PLANET_ZOO}:
		return set_pz(inst)
	if game in {games.JURASSIC_WORLD_EVOLUTION}:
		return set_jwe(inst)


