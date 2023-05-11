from generated.base_struct import BaseStruct
from generated.formats.manis.imports import name_type_map


class Vector4H(BaseStruct):

	__name__ = 'Vector4H'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.w = name_type_map['Normshort'](self.context, 0, None)
		self.x = name_type_map['Normshort'](self.context, 0, None)
		self.y = name_type_map['Normshort'](self.context, 0, None)
		self.z = name_type_map['Normshort'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'w', name_type_map['Normshort'], (0, None), (False, None), (None, None)
		yield 'x', name_type_map['Normshort'], (0, None), (False, None), (None, None)
		yield 'y', name_type_map['Normshort'], (0, None), (False, None), (None, None)
		yield 'z', name_type_map['Normshort'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'w', name_type_map['Normshort'], (0, None), (False, None)
		yield 'x', name_type_map['Normshort'], (0, None), (False, None)
		yield 'y', name_type_map['Normshort'], (0, None), (False, None)
		yield 'z', name_type_map['Normshort'], (0, None), (False, None)

	def __repr__(self):
		return f"[ {self.w:6.3f} {self.x:6.3f} {self.y:6.3f} {self.z:6.3f} ]"

