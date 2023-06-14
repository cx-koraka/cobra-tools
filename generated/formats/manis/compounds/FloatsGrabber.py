import logging

from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.base.basic import Float
from generated.formats.base.compounds.Vector3 import Vector3
from generated.formats.manis.compounds.LocBound import LocBound
import numpy as np

from generated.base_struct import BaseStruct


class FloatsGrabber(BaseStruct):

	__name__ = 'FloatsGrabber'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)

	@classmethod
	def read_fields(cls, stream, instance):
		instance.io_start = stream.tell()
		num_bounds = np.max(instance.arg) + 1
		instance.mins = Array.from_stream(stream, instance.context, 0, None, (num_bounds, 3), Float)
		instance.scales = Array.from_stream(stream, instance.context, 0, None, (num_bounds, 3), Float)
		logging.debug(f"Compressed keys data ends at {stream.tell()}")
		instance.io_size = stream.tell() - instance.io_start

	@classmethod
	def write_fields(cls, stream, instance):
		instance.io_start = stream.tell()
		for bound in instance.bounds:
			LocBound.to_stream(bound, stream, instance.context)
		instance.io_size = stream.tell() - instance.io_start

	@classmethod
	def get_fields_str(cls, instance, indent=0):
		return f"\nMins:\n{instance.mins}, \nScales:\n{instance.scales}"


