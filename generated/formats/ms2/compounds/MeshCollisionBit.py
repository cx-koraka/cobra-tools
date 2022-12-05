import numpy
from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Ushort


class MeshCollisionBit(BaseStruct):

	__name__ = 'MeshCollisionBit'

	_import_key = 'ms2.compounds.MeshCollisionBit'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# ?
		self.a = Array(self.context, 0, None, (0,), Ushort)

		# incrementing by 16 from 0, or if around 32769: incrementing by 1, mostly
		self.b = Array(self.context, 0, None, (0,), Ushort)

		# usually, but not always the first value
		self.min_of_b = 0

		# ?
		self.c = 0

		# always 2954754766?
		self.consts = Array(self.context, 0, None, (0,), Uint)
		if set_default:
			self.set_defaults()

	_attribute_list = BaseStruct._attribute_list + [
		('a', Array, (0, None, (24,), Ushort), (False, None), None),
		('b', Array, (0, None, (8,), Ushort), (False, None), None),
		('min_of_b', Ushort, (0, None), (False, None), None),
		('c', Ushort, (0, None), (False, None), None),
		('consts', Array, (0, None, (3,), Uint), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'a', Array, (0, None, (24,), Ushort), (False, None)
		yield 'b', Array, (0, None, (8,), Ushort), (False, None)
		yield 'min_of_b', Ushort, (0, None), (False, None)
		yield 'c', Ushort, (0, None), (False, None)
		yield 'consts', Array, (0, None, (3,), Uint), (False, None)
