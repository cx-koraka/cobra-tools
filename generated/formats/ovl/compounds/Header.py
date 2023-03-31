import numpy
from generated.array import Array
from generated.formats.base.basic import Ubyte
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Ushort
from generated.formats.base.compounds.PadAlign import PadAlign
from generated.formats.base.compounds.ZStringBuffer import ZStringBuffer
from generated.formats.ovl.compounds.ArchiveEntry import ArchiveEntry
from generated.formats.ovl.compounds.ArchiveMeta import ArchiveMeta
from generated.formats.ovl.compounds.AuxEntry import AuxEntry
from generated.formats.ovl.compounds.DependencyEntry import DependencyEntry
from generated.formats.ovl.compounds.FileEntry import FileEntry
from generated.formats.ovl.compounds.IncludedOvl import IncludedOvl
from generated.formats.ovl.compounds.MimeEntry import MimeEntry
from generated.formats.ovl.compounds.StreamEntry import StreamEntry
from generated.formats.ovl.compounds.Triplet import Triplet
from generated.formats.ovl_base.compounds.Empty import Empty
from generated.formats.ovl_base.compounds.GenericHeader import GenericHeader


class Header(GenericHeader):

	"""
	Found at the beginning of every OVL file
	"""

	__name__ = 'Header'

	_import_key = 'ovl.compounds.Header'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# Seems to match the number of LOD models for the file (has more than 1 file)
		self.lod_depth = 0

		# length of the Names block below, including 00 bytes
		self.len_names = 0
		self.zero_2 = 0

		# count of external aux files, ie audio banks
		self.num_aux_entries = 0

		# count of included ovl files that are available to this ovl
		self.num_included_ovls = 0

		# count of file mime types, aka. extensions with metadata
		self.num_mimes = 0
		self.num_files = 0

		# repeat count of files ??
		self.num_files_2 = 0
		self.num_dependencies = 0

		# number of archives
		self.num_archives = 0

		# across all archives
		self.num_pool_groups = 0

		# across all archives
		self.num_pools = 0

		# across all archives
		self.num_datas = 0

		# across all archives
		self.num_buffers = 0

		# number of files in external OVS archives
		self.num_stream_files = 0

		# used in ZTUAC elephants
		self.ztuac_unk_0 = 0

		# used in ZTUAC elephants
		self.ztuac_unk_1 = 0

		# used in ZTUAC elephants
		self.ztuac_unk_2 = 0

		# length of archive names
		self.len_archive_names = 0

		# another Num Files
		self.num_files_3 = 0

		# length of the type names portion inside Names block (usually at the start), not counting 00 bytes
		self.len_type_names = 0

		# used in PZ1.6 for the first time
		self.num_triplets = 0

		# zeros
		self.reserved = Array(self.context, 0, None, (0,), Uint)

		# Name buffer for assets and file mime types.
		self.names = ZStringBuffer(self.context, self.len_names, None)

		# used in DLA
		self.names_pad = Array(self.context, 0, None, (0,), Ubyte)
		self.mimes = Array(self.context, 0, None, (0,), MimeEntry)
		self.triplets_ref = Empty(self.context, 0, None)
		self.triplets = Array(self.context, 0, None, (0,), Triplet)
		self.triplets_pad = PadAlign(self.context, 4, self.triplets_ref)
		self.files = Array(self.context, 0, None, (0,), FileEntry)

		# usually STATIC followed by any external OVS names
		self.archive_names = ZStringBuffer(self.context, self.len_archive_names, None)
		self.archives = Array(self.context, 0, None, (0,), ArchiveEntry)
		self.included_ovls = Array(self.context, 0, None, (0,), IncludedOvl)
		self.dependencies = Array(self.context, 0, None, (0,), DependencyEntry)
		self.aux_entries = Array(self.context, 0, None, (0,), AuxEntry)

		# after aux in ZTUAC and PC
		self.dependencies = Array(self.context, 0, None, (0,), DependencyEntry)
		self.stream_files = Array(self.context, 0, None, (0,), StreamEntry)
		self.archives_meta = Array(self.context, 0, None, (0,), ArchiveMeta)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield ('lod_depth', Uint, (0, None), (False, None), None)
		yield ('len_names', Uint, (0, None), (False, None), None)
		yield ('zero_2', Uint, (0, None), (False, None), None)
		yield ('num_aux_entries', Uint, (0, None), (False, None), None)
		yield ('num_included_ovls', Ushort, (0, None), (False, None), None)
		yield ('num_mimes', Ushort, (0, None), (False, None), None)
		yield ('num_files', Uint, (0, None), (False, None), None)
		yield ('num_files_2', Uint, (0, None), (False, None), None)
		yield ('num_dependencies', Uint, (0, None), (False, None), None)
		yield ('num_archives', Uint, (0, None), (False, None), None)
		yield ('num_pool_groups', Uint, (0, None), (False, None), None)
		yield ('num_pools', Uint, (0, None), (False, None), None)
		yield ('num_datas', Uint, (0, None), (False, None), None)
		yield ('num_buffers', Uint, (0, None), (False, None), None)
		yield ('num_stream_files', Uint, (0, None), (False, None), None)
		yield ('ztuac_unk_0', Uint, (0, None), (False, None), None)
		yield ('ztuac_unk_1', Uint, (0, None), (False, None), None)
		yield ('ztuac_unk_2', Uint, (0, None), (False, None), None)
		yield ('len_archive_names', Uint, (0, None), (False, None), None)
		yield ('num_files_3', Uint, (0, None), (False, None), None)
		yield ('len_type_names', Uint, (0, None), (False, None), None)
		yield ('num_triplets', Uint, (0, None), (False, None), None)
		yield ('reserved', Array, (0, None, (12,), Uint), (False, None), None)
		yield ('names', ZStringBuffer, (None, None), (False, None), None)
		yield ('names_pad', Array, (0, None, (None,), Ubyte), (False, None), True)
		yield ('mimes', Array, (0, None, (None,), MimeEntry), (False, None), None)
		yield ('triplets_ref', Empty, (0, None), (False, None), None)
		yield ('triplets', Array, (0, None, (None,), Triplet), (False, None), True)
		yield ('triplets_pad', PadAlign, (4, None), (False, None), True)
		yield ('files', Array, (0, None, (None,), FileEntry), (False, None), None)
		yield ('archive_names', ZStringBuffer, (None, None), (False, None), None)
		yield ('archives', Array, (0, None, (None,), ArchiveEntry), (False, None), None)
		yield ('included_ovls', Array, (0, None, (None,), IncludedOvl), (False, None), None)
		yield ('dependencies', Array, (0, None, (None,), DependencyEntry), (False, None), True)
		yield ('aux_entries', Array, (0, None, (None,), AuxEntry), (False, None), None)
		yield ('dependencies', Array, (0, None, (None,), DependencyEntry), (False, None), True)
		yield ('stream_files', Array, (0, None, (None,), StreamEntry), (False, None), None)
		yield ('archives_meta', Array, (0, None, (None,), ArchiveMeta), (False, None), None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'lod_depth', Uint, (0, None), (False, None)
		yield 'len_names', Uint, (0, None), (False, None)
		yield 'zero_2', Uint, (0, None), (False, None)
		yield 'num_aux_entries', Uint, (0, None), (False, None)
		yield 'num_included_ovls', Ushort, (0, None), (False, None)
		yield 'num_mimes', Ushort, (0, None), (False, None)
		yield 'num_files', Uint, (0, None), (False, None)
		yield 'num_files_2', Uint, (0, None), (False, None)
		yield 'num_dependencies', Uint, (0, None), (False, None)
		yield 'num_archives', Uint, (0, None), (False, None)
		yield 'num_pool_groups', Uint, (0, None), (False, None)
		yield 'num_pools', Uint, (0, None), (False, None)
		yield 'num_datas', Uint, (0, None), (False, None)
		yield 'num_buffers', Uint, (0, None), (False, None)
		yield 'num_stream_files', Uint, (0, None), (False, None)
		yield 'ztuac_unk_0', Uint, (0, None), (False, None)
		yield 'ztuac_unk_1', Uint, (0, None), (False, None)
		yield 'ztuac_unk_2', Uint, (0, None), (False, None)
		yield 'len_archive_names', Uint, (0, None), (False, None)
		yield 'num_files_3', Uint, (0, None), (False, None)
		yield 'len_type_names', Uint, (0, None), (False, None)
		yield 'num_triplets', Uint, (0, None), (False, None)
		yield 'reserved', Array, (0, None, (12,), Uint), (False, None)
		yield 'names', ZStringBuffer, (instance.len_names, None), (False, None)
		if instance.context.version <= 15:
			yield 'names_pad', Array, (0, None, ((16 - (instance.len_names % 16)) % 16,), Ubyte), (False, None)
		yield 'mimes', Array, (0, None, (instance.num_mimes,), MimeEntry), (False, None)
		yield 'triplets_ref', Empty, (0, None), (False, None)
		if instance.context.version >= 20:
			yield 'triplets', Array, (0, None, (instance.num_triplets,), Triplet), (False, None)
			yield 'triplets_pad', PadAlign, (4, instance.triplets_ref), (False, None)
		yield 'files', Array, (0, None, (instance.num_files,), FileEntry), (False, None)
		yield 'archive_names', ZStringBuffer, (instance.len_archive_names, None), (False, None)
		yield 'archives', Array, (0, None, (instance.num_archives,), ArchiveEntry), (False, None)
		yield 'included_ovls', Array, (0, None, (instance.num_included_ovls,), IncludedOvl), (False, None)
		if instance.context.version >= 19:
			yield 'dependencies', Array, (0, None, (instance.num_dependencies,), DependencyEntry), (False, None)
		yield 'aux_entries', Array, (0, None, (instance.num_aux_entries,), AuxEntry), (False, None)
		if instance.context.version <= 18:
			yield 'dependencies', Array, (0, None, (instance.num_dependencies,), DependencyEntry), (False, None)
		yield 'stream_files', Array, (0, None, (instance.num_stream_files,), StreamEntry), (False, None)
		yield 'archives_meta', Array, (0, None, (instance.num_archives,), ArchiveMeta), (False, None)


Header.init_attributes()
