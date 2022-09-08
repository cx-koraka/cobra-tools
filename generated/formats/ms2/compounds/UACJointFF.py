import numpy
from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Int
from generated.formats.base.basic import Uint


class UACJointFF(BaseStruct):

	__name__ = 'UACJointFF'

	_import_path = 'generated.formats.ms2.compounds.UACJointFF'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# must be 11
		self.eleven = 0

		# bunch of -1's, and constants
		self.f_fs = Array(self.context, 0, None, (0,), Int)
		self.name_offset = 0
		self.hitcheck_count = 0

		# 12 bytes of zeros
		self.zeros = Array(self.context, 0, None, (0,), Uint)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.eleven = 0
		self.f_fs = numpy.zeros((4,), dtype=numpy.dtype('int32'))
		self.name_offset = 0
		self.hitcheck_count = 0
		self.zeros = numpy.zeros((3,), dtype=numpy.dtype('uint32'))

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'eleven', Uint, (0, None), (False, None)
		yield 'f_fs', Array, (0, None, (4,), Int), (False, None)
		yield 'name_offset', Uint, (0, None), (False, None)
		yield 'hitcheck_count', Uint, (0, None), (False, None)
		yield 'zeros', Array, (0, None, (3,), Uint), (False, None)

	def get_info_str(self, indent=0):
		return f'UACJointFF [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
