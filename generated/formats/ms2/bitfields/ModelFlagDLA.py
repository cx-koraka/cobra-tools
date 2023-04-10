from generated.bitfield import BasicBitfield
from generated.bitfield import BitfieldMember
from generated.formats.base.basic import Uint
from generated.formats.ovl_base.basic import Bool


class ModelFlagDLA(BasicBitfield):

	"""
	Determines the data held by a mesh.
	"""

	__name__ = 'ModelFlagDLA'
	_storage = Uint
	vertex_offset = BitfieldMember(pos=1, mask=0x2, return_type=Bool.from_value)
	stripify = BitfieldMember(pos=5, mask=0x20, return_type=Bool.from_value)

	def set_defaults(self):
		pass
