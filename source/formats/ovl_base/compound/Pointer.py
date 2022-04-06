from generated.context import ContextReference
# from generated.formats.ovl_base.compound.MemStruct import MemStruct


class Pointer:

	"""
	a pointer in an ovl memory layout
	"""

	context = ContextReference()

# START_CLASS

	def __init__(self, context, arg=0, template=None, set_default=True):
		self.name = ''
		self._context = context
		self.arg = arg
		self.template = template
		self.io_size = 0
		self.io_start = 0
		self.offset = 0
		self.data = None
		self.frag = None
		# # todo - test if it is better to already create the template here, or on demand from MemStruct
		# self.data = template(context, arg=0, template=None)
		if set_default:
			self.set_defaults()

	def get_info_str(self):
		return f'Pointer [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self):
		s = ''
		s += f'\n	* offset = {self.offset.__repr__()}'
		s += f'\n	* data = {self.data.__repr__()}'
		return s

	def read_ptr(self, ovs, ref_ptr, io_start, sized_str_entry):
		"""Looks up the address of the pointer, checks if a frag points to pointer and reads the data at its address as
		the specified template."""
		# calculate offset specified to relative io_start
		rel_offset = self.io_start - io_start
		# print(f"handle_ptr dtype: {ptr.template.__name__} io_ref: {io_start} relative: {rel_offset} count: {ptr.arg}")
		# get a fragment whose ptr[0] lands on ref_ptr + rel_offset
		self.frag = ovs.frag_at_pointer(ref_ptr, offset=rel_offset)
		# ptr may be a nullptr, so ignore
		if not self.frag:
			# print("is a nullptr")
			return
		# store valid frag to be able to delete it later
		sized_str_entry.fragments.append(self.frag)
		# now read an instance of template class at the offset
		if self.template:
			self.data = self.template.from_stream(self.frag.pointers[1].stream, self.context, self.arg)

	def __repr__(self):
		s = self.get_info_str()
		s += self.get_fields_str()
		s += '\n'
		return s
