import logging
import xml.etree.ElementTree as ET

from numpy.core.multiarray import ndarray

from generated.array import Array
from generated.context import ContextReference

# these attributes present on the MemStruct will not be stored on the XML
SKIPS = ("_context", "arg", "name", "io_start", "io_size", "template")
DTYPE = "dtype"
XML_STR = "xml_string"


def indent(e, level=0):
	i = "\n" + level * "	"
	if len(e):
		if not e.text or not e.text.strip():
			e.text = i + "	"
		if not e.tail or not e.tail.strip():
			e.tail = i
		for e in e:
			indent(e, level + 1)
		if not e.tail or not e.tail.strip():
			e.tail = i
	else:
		if level and (not e.tail or not e.tail.strip()):
			e.tail = i


def str_to_bool(s):
	if s.lower() == 'true':
		return True
	elif s.lower() == 'false':
		return False
	else:
		raise ValueError


class StructBase:

	context = ContextReference()

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0

	def set_defaults(self):
		pass

	def get_fields_str(self, indent=0):
		return ""

	@staticmethod
	def fmt_member(member, indent=0):
		lines = str(member).split("\n")
		lines_new = [lines[0], ] + ["\t" * indent + line for line in lines[1:]]
		return "\n".join(lines_new)

	@classmethod
	def from_xml_file(cls, file_path, context, arg=0, template=None):
		"""Load Struct represented by the xml in 'file_path'"""
		instance = cls(context, arg, template, set_default=False)
		tree = ET.parse(file_path)
		xml = tree.getroot()
		cls._from_xml(instance, xml)
		return instance

	@classmethod
	def from_xml(cls, target, elem, prop, arguments):
		"""Creates object for parent object 'target', from parent element elem."""
		sub = elem.find(f'.//{prop}')
		if sub is None:
			logging.warning(f"Missing sub-element '{prop}' on XML element '{elem.tag}'")
			return
		instance = cls(target.context, *arguments, set_default=False)
		cls._from_xml(instance, sub)
		return instance

	@classmethod
	def _from_xml(cls, instance, elem):
		"""Sets the data from the XML to this struct"""
		# special cases - these are not added to the xml definition, but need to be converted
		for prop in ("name", "game"):
			if prop in elem.attrib:
				setattr(instance, prop, elem.attrib[prop])

		set_fields = set()
		# go over all (active through conditions) fields of this struct
		for prop, field_type, arguments in cls._get_filtered_attribute_list(instance):
			set_fields.add(prop)
			# skip dummy properties
			if prop in SKIPS:
				continue
			setattr(instance, prop, field_type.from_xml(instance, elem, prop, arguments))

		# also add any meta-data that is not directly part of the struct generated by the codegen
		for attr, value in elem.attrib.items():
			if attr not in set_fields:
				logging.debug(f"Adding string metadata '{attr} = {value}' from XML element '{elem.tag}'")
				setattr(instance, attr, value)

	@staticmethod
	def _handle_xml_str(prop):
		return "data" if prop != XML_STR else XML_STR

	@classmethod
	def to_xml_file(cls, instance, file_path, debug=False):
		"""Create an xml elem representing this MemStruct, recursively set its data, indent and save to 'file_path'"""
		xml = ET.Element(cls.__name__)
		cls._to_xml(instance, xml, debug)
		indent(xml)
		with open(file_path, 'wb') as outfile:
			outfile.write(ET.tostring(xml))

	@classmethod
	def to_xml(cls, elem, prop, instance, arguments, debug):
		"""Adds this struct to 'elem', recursively"""
		sub = ET.SubElement(elem, cls.__name__)
		cls._to_xml(instance, sub, debug)

	@classmethod
	def _to_xml(cls, instance, elem, debug):
		# go over all fields of this struct
		for prop, field_type, arguments in cls._get_filtered_attribute_list(instance):
			if prop in SKIPS:
				continue
			field_type.to_xml(elem, prop, getattr(instance, prop), arguments, debug)
		potential_name = getattr(instance, "name", "")
		if potential_name:
			elem.attrib["name"] = potential_name

	@classmethod
	def read_fields(cls, stream, instance):
		pass

	@classmethod
	def write_fields(cls, stream, instance):
		pass

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		pass

	@classmethod
	def from_stream(cls, stream, context, arg=0, template=None):
		instance = cls(context, arg, template, set_default=False)
		instance.io_start = stream.tell()
		cls.read_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance

	@classmethod
	def to_stream(cls, stream, instance):
		instance.io_start = stream.tell()
		cls.write_fields(stream, instance)
		instance.io_size = stream.tell() - instance.io_start
		return instance