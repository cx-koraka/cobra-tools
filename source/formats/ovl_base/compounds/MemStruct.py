# START_GLOBALS
import logging

from generated.array import Array
from generated.base_struct import DO_NOT_SERIALIZE, SKIPS
from generated.formats.base.basic import ZString
from generated.formats.ovl_base.compounds.ArrayPointer import ArrayPointer
from generated.formats.ovl_base.compounds.ForEachPointer import ForEachPointer
from generated.formats.ovl_base.compounds.CondPointer import CondPointer
from generated.formats.ovl_base.compounds.Pointer import Pointer
from ovl_util.shared import check_any

DEPENDENCY_TAG = "dependency"


# END_GLOBALS

class MemStruct:
	"""this is a struct that is capable of having pointers"""
	# START_CLASS

	@classmethod
	def is_array_count(cls, f_name, set_fields):
		# logging.info(f"Checking for {f_name}")
		count_markers = ("_count", "num_")
		if check_any(count_markers, f_name):
			# logging.info(f"Found count {f_name}")
			array_name = f_name
			for c in count_markers:
				array_name = array_name.replace(c, "")
			if array_name in set_fields:
				# logging.info(f"Found array {array_name}")
				return array_name

	@classmethod
	def _from_xml(cls, instance, elem):
		"""Sets the data from the XML to this struct"""
		set_fields = cls.get_field_names(instance)
		# go over all (active through conditions) fields of this struct
		# read everything that isn't a pointer to ensure that pointer arguments are valid in the second loop
		for f_name, f_type, arguments, (optional, default) in cls._get_filtered_attribute_list(instance):
			if not issubclass(f_type, Pointer):
				# skip dummy properties
				if f_name in SKIPS:
					continue
				# keep clean XML
				if f_name.startswith(DO_NOT_SERIALIZE) or (optional and not elem.attrib.get(f_name)):
					continue
				array_name = cls.is_array_count(f_name, set_fields)
				# find the xml subelem
				if array_name:
					array = elem.find(f'./{array_name}')
					if array:
						# this does not handle arrays that are nested in a wrapper
						setattr(instance, f_name, len(array))
					else:
						setattr(instance, f_name, 0)
				else:
					setattr(instance, f_name, f_type.from_xml(instance, elem, f_name, *arguments))

		# finally read the pointers
		for f_name, f_type, arguments, (optional, default) in cls._get_filtered_attribute_list(instance):
			if issubclass(f_type, Pointer):
				setattr(instance, f_name, f_type.from_xml(instance, elem, f_name, *arguments))

		# also add any meta-data that is not directly part of the struct generated by the codegen
		for attr, value in elem.attrib.items():
			if attr not in set_fields:
				# logging.debug(f"Adding string metadata '{attr} = {value}' from XML element '{elem.tag}'")
				setattr(instance, attr, value)
		return instance

	def write_ptrs(self, loader, pool):
		"""Process all pointers in the structure and recursively load pointers in the sub-structs."""
		# recursive doesnt get the whole structure - why?
		# could work if the order is good
		pool.offsets.add(self.io_start)
		pool.size_map[self.io_start] = self.io_size
		children = loader.stack[(pool, self.io_start)] = {}
		for ptr, f_name, arguments in MemStruct.get_instances_recursive(self, Pointer):
			ptr.write_ptr_all(self, children, f_name, loader, pool)

	@classmethod
	def get_all_str_pointers(cls, instance):
		for ptr, f_name, arguments in MemStruct.get_instances_recursive(instance, Pointer):
			if ptr.template and issubclass(ptr.template, ZString):
				yield ptr  # , f_name, arguments
			elif isinstance(ptr.data, MemStruct):
				yield from MemStruct.get_all_str_pointers(ptr.data)
			elif isinstance(ptr.data, Array):
				for elem in ptr.data:
					if isinstance(elem, MemStruct):
						yield from MemStruct.get_all_str_pointers(elem)

	@classmethod
	def get_instances_recursive(cls, instance, dtype):
		for s_type, s_inst, (f_name, f_type, arguments, _) in cls.get_condition_attributes_recursive(instance, instance, lambda x: issubclass(x[1], dtype)):
			f_inst = s_type.get_field(s_inst, f_name)
			yield f_inst, f_name, arguments

	def read_ptrs(self, pool, debug=False):
		"""Process all pointers in the structure and recursively load pointers in the sub-structs."""
		offsets_of_ptrs = set()
		# need to recurse here, because we may have substructs that are part of this MemStruct (not via ptrs)
		for ptr, f_name, arguments in MemStruct.get_instances_recursive(self, Pointer):
			# update the pointer's arg, as it is sometimes read after the pointer
			ptr.arg, template = arguments
			if not ptr.template:
				# try the lookup function to get a suitable template for this field
				ptr.template = self.get_ptr_template(f_name)
			offsets_of_ptrs.add(ptr.io_start)
			# locates the read address, attaches the frag entry, and reads the template as ptr.data
			ptr.read_ptr(pool)
			if ptr.target_pool:
				# keep reading pointers in the newly read ptr.data
				for memstruct in self.structs_from_ptr(ptr):
					memstruct.read_ptrs(ptr.target_pool, debug=debug)
		if debug:
			# verify that there is no uncaught pointer
			for l_offset, rel_offset, entry in pool.get_ptrs_in_struct(self.io_start, self.io_size):
				# skip dependencies
				if isinstance(entry, tuple):
					target_pool, target_offset = entry
					if l_offset not in offsets_of_ptrs:
						logging.warning(f"Pointer at {pool.i} | {l_offset} to {target_pool.i} | {target_offset} is missing for {self.__class__.__name__} (rel offset: {rel_offset})")

	@staticmethod
	def structs_from_ptr(ptr):
		"""Get all direct memstruct children of this ptr"""
		if isinstance(ptr.data, MemStruct):
			yield ptr.data
		elif isinstance(ptr.data, Array):
			assert isinstance(ptr, (ArrayPointer, ForEachPointer, CondPointer))
			for member in ptr.data:
				if isinstance(member, MemStruct):
					yield member

	def get_ptr_template(self, prop):
		"""Returns the appropriate template for a pointer named 'prop', if exists.
		Must be overwritten in subclass"""
		return None

