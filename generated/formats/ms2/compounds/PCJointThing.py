import numpy
from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Short


class PCJointThing(BaseStruct):

	"""
	8 bytes
	"""

	__name__ = 'PCJointThing'

	_import_path = 'generated.formats.ms2.compounds.PCJointThing'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# -1
		self.shorts = Array(self.context, 0, None, (0,), Short)
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.shorts = numpy.zeros((4,), dtype=numpy.dtype('int16'))

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.shorts = Array.from_stream(stream, instance.context, 0, None, (4,), Short)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		Array.to_stream(stream, instance.shorts, instance.context, 0, None, (4,), Short)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'shorts', Array, (0, None, (4,), Short), (False, None)

	def get_info_str(self, indent=0):
		return f'PCJointThing [Size: {self.io_size}, Address: {self.io_start}] {self.name}'
