
import logging
import xml.etree.ElementTree as ET

from generated.array import Array
from generated.formats.ovl_base.compounds.Pointer import Pointer
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer

FOREACH_MARK = "_foreach_"
from generated.formats.ovl_base.compounds.Pointer import Pointer


class ForEachPointer(Pointer):

	"""
	a pointer to an array in an ovl memory layout
	"""

	__name__ = 'ForEachPointer'

	_import_path = 'generated.formats.ovl_base.compounds.ForEachPointer'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)

	def get_info_str(self, indent=0):
		return f'ForEachPointer [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def read_template(self):
		if self.template:
			if isinstance(self.arg, ArrayPointer):
				args = self.arg.data
			else:
				raise AttributeError(f"Unsupported arg {type(self.arg)} for ForEachPointer")
			# context, arg=0, template=None, shape=(), dtype=None, set_default=True
			self.data = Array(self.context, 0, None, (len(args)), self.template, set_default=False)
			stream = self.frag.struct_ptr.stream
			# for i, arg in enumerate(args):
			# 	logging.debug(f"Argument {i} = {arg}, template {self.template}")
			self.data[:] = [self.template.from_stream(stream, self.context, arg) for arg in args]

	# @classmethod
	# def _to_xml(cls, instance, elem, debug):
	# 	"""Assigns data self to xml elem"""
	# 	Array._to_xml(instance.data, elem, debug)

	@classmethod
	def _from_xml(cls, instance, elem):
		# context, arg=0, template=None, shape=(), dtype=None, set_default=True
		instance.data = Array(instance.context, instance.arg.data, None, (len(elem)), instance.template, set_default=False)
		# need set_default to fix dtype according to each member of arg's input array
		instance.data[:] = [instance.template(instance.context, member, instance.template, set_default=True) for member in instance.arg.data]
		for subelem, member in zip(elem, instance.data):
			member._from_xml(member, subelem)
		return instance

	@classmethod
	def to_xml(cls, elem, prop, instance, arguments, debug):
		if instance.data is not None:
			assert FOREACH_MARK in prop
			src_prop = prop.split(FOREACH_MARK)[1]
			sub = elem.find(f'.//{src_prop}')
			for subelem, member in zip(sub, instance.data):
				member._to_xml(member, subelem, debug)

	@classmethod
	def from_xml(cls, target, elem, prop, arguments):
		"""Creates object for parent object 'target', from parent element elem."""
		assert FOREACH_MARK in prop
		src_prop = prop.split(FOREACH_MARK)[1]
		sub = elem.find(f'.//{src_prop}')
		if sub is None:
			logging.warning(f"Missing sub-element '{prop}' on XML element '{elem.tag}'")
			return
		instance = cls(target.context, *arguments, set_default=False)
		cls.pool_type_from_xml(elem, instance)
		cls._from_xml(instance, sub)
		return instance

	# def write_template(self):
	# 	assert self.template is not None
	# 	# Array.to_stream(self.frag.struct_ptr.stream, self.data, (len(self.data),), self.template, self.context, 0, None)
	# 	self.frag.struct_ptr.write_instance(self.template, self.data)

