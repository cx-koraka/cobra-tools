from io import BytesIO
import logging

from generated.formats.base.basic import ZString
from generated.formats.base.compounds.PadAlign import get_padding

ZERO = b"\x00"


from generated.base_struct import BaseStruct


class ZStringBuffer(BaseStruct):

	"""
	Holds a buffer of zero-terminated strings
	"""

	__name__ = 'ZStringBuffer'

	_import_key = 'base.compounds.ZStringBuffer'

	_attribute_list = BaseStruct._attribute_list + [
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.data = b""
		self.strings = []
		self.offset_dic = {}

	def get_str_at(self, pos):
		end = self.data.find(ZERO, pos)
		return self.data[pos:end].decode()

	def update_with(self, list_of_arrays):
		"""Updates this name buffer with a list of (array, attrib) whose elements have
		offset: bytes relative to the start of the name block
		[attrib]: string"""
		logging.debug("Updating name buffer")
		self.strings = []
		self.offset_dic = {}
		with BytesIO() as stream:

			for array, attrib, func in list_of_arrays:
				for item in sorted(array, key=lambda i: getattr(i, attrib)):
					name = getattr(item, attrib)
					# do any processing of the string on the fly
					if func is not None:
						name = func(name)
					if name in self.offset_dic:
						# known string, just get offset
						address = self.offset_dic[name]
					else:
						# new string, store offset and write zstring
						address = stream.tell()
						self.strings.append(name)
						self.offset_dic[name] = address
						ZString.to_stream(name, stream, self.context)
					# store offset on item
					item.offset = address
			# get the actual result buffer
			buffer_bytes = stream.getvalue()
		self.data = buffer_bytes + get_padding(len(buffer_bytes), alignment=8)

	def update_strings(self, list_of_strs):
		"""Updates this name buffer with a list of names"""
		logging.debug("Updating name buffer")
		self.strings = sorted(set(list_of_strs))
		self.offset_dic = {}
		with BytesIO() as stream:
			for name in self.strings:
				# store offset and write zstring
				self.offset_dic[name] = stream.tell()
				ZString.to_stream(name, stream, self.context)
			# get the actual result buffer
			self.data = stream.getvalue()

	def __repr__(self):
		return str(self.strings)

	@classmethod
	def read_fields(cls, stream, instance):
		instance.data = stream.read(instance.arg)
		instance.strings = instance.data.split(ZERO)

	@classmethod
	def write_fields(cls, stream, instance):
		stream.write(instance.data)

	@staticmethod
	def validate_instance(instance, context, arg,  template):
		super().validate_instance(instance, context, arg, template)
		assert len(instance.data) == instance.arg

	@classmethod
	def get_size(cls, instance, context, arg=0, template=None):
		return len(instance.data)

