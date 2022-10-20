from generated.formats.semanticflexicolours.compounds.SemanticFlexiColoursRoot import SemanticFlexiColoursRoot
from modules.formats.BaseFormat import MemStructLoader


class SemanticFlexiColoursLoader(MemStructLoader):
    target_class = SemanticFlexiColoursRoot
    extension = ".semanticflexicolours"