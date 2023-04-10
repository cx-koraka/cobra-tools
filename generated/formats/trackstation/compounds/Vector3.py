from generated.formats.ovl_base.compounds.MemStruct import MemStruct
from generated.formats.trackstation.imports import name_type_map


class Vector3(MemStruct):

	"""
	A vector in 3D space (x,y,z).
	"""

	__name__ = 'Vector3'

	_import_key = 'trackstation.compounds.Vector3'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# First coordinate.
		self.x = 0.0

		# Second coordinate.
		self.y = 0.0

		# Third coordinate.
		self.z = 0.0
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('x', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('y', name_type_map['Float'], (0, None), (False, None), (None, None))
		yield ('z', name_type_map['Float'], (0, None), (False, None), (None, None))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'x', name_type_map['Float'], (0, None), (False, None)
		yield 'y', name_type_map['Float'], (0, None), (False, None)
		yield 'z', name_type_map['Float'], (0, None), (False, None)
