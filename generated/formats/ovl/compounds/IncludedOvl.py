from generated.formats.ovl.compounds.NamedEntry import NamedEntry
from generated.formats.ovl_base.basic import OffsetString


class IncludedOvl(NamedEntry):

	"""
	Description of one included ovl file that is force-loaded by this ovl
	"""

	__name__ = 'IncludedOvl'

	_import_key = 'ovl.compounds.IncludedOvl'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# path is relative to this ovl's directory; usually points to ovl files
		self.basename = 0
		if set_default:
			self.set_defaults()

	_attribute_list = NamedEntry._attribute_list + [
		('basename', OffsetString, (None, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'basename', OffsetString, (instance.context.names, None), (False, None)
