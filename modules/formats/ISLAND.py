from generated.formats.island.compounds.IslandRoot import IslandRoot
from modules.formats.BaseFormat import MemStructLoader


class IslandLoader(MemStructLoader):
	extension = ".island"
	target_class = IslandRoot
