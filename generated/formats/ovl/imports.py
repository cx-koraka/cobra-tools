from importlib import import_module


type_module_name_map = {
	'Byte': 'generated.formats.base.basic',
	'Ubyte': 'generated.formats.base.basic',
	'Uint64': 'generated.formats.base.basic',
	'Int64': 'generated.formats.base.basic',
	'Uint': 'generated.formats.base.basic',
	'Ushort': 'generated.formats.base.basic',
	'Int': 'generated.formats.base.basic',
	'Short': 'generated.formats.base.basic',
	'Char': 'generated.formats.base.basic',
	'Normshort': 'generated.formats.base.basic',
	'Float': 'generated.formats.base.basic',
	'Double': 'generated.formats.base.basic',
	'Hfloat': 'generated.formats.base.basic',
	'ZString': 'generated.formats.base.basic',
	'ZStringBuffer': 'generated.formats.base.compounds.ZStringBuffer',
	'PadAlign': 'generated.formats.base.compounds.PadAlign',
	'FixedString': 'generated.formats.base.compounds.FixedString',
	'Bool': 'generated.formats.ovl_base.basic',
	'OffsetString': 'generated.formats.ovl_base.basic',
	'Compression': 'generated.formats.ovl_base.enums.Compression',
	'VersionInfo': 'generated.formats.ovl_base.bitfields.VersionInfo',
	'Pointer': 'generated.formats.ovl_base.compounds.Pointer',
	'ArrayPointer': 'generated.formats.ovl_base.compounds.ArrayPointer',
	'ForEachPointer': 'generated.formats.ovl_base.compounds.ForEachPointer',
	'MemStruct': 'generated.formats.ovl_base.compounds.MemStruct',
	'SmartPadding': 'generated.formats.ovl_base.compounds.SmartPadding',
	'ZStringObfuscated': 'generated.formats.ovl_base.basic',
	'GenericHeader': 'generated.formats.ovl_base.compounds.GenericHeader',
	'Empty': 'generated.formats.ovl_base.compounds.Empty',
	'MimeEntry': 'generated.formats.ovl.compounds.MimeEntry',
	'Triplet': 'generated.formats.ovl.compounds.Triplet',
	'FileEntry': 'generated.formats.ovl.compounds.FileEntry',
	'ArchiveEntry': 'generated.formats.ovl.compounds.ArchiveEntry',
	'IncludedOvl': 'generated.formats.ovl.compounds.IncludedOvl',
	'HeaderPointer': 'generated.formats.ovl.compounds.HeaderPointer',
	'DependencyEntry': 'generated.formats.ovl.compounds.DependencyEntry',
	'AuxEntry': 'generated.formats.ovl.compounds.AuxEntry',
	'StreamEntry': 'generated.formats.ovl.compounds.StreamEntry',
	'ArchiveMeta': 'generated.formats.ovl.compounds.ArchiveMeta',
	'Header': 'generated.formats.ovl.compounds.Header',
	'NamedEntry': 'generated.formats.ovl.compounds.NamedEntry',
	'PoolGroup': 'generated.formats.ovl.compounds.PoolGroup',
	'MemPool': 'generated.formats.ovl.compounds.MemPool',
	'DataEntry': 'generated.formats.ovl.compounds.DataEntry',
	'BufferEntry': 'generated.formats.ovl.compounds.BufferEntry',
	'BufferGroup': 'generated.formats.ovl.compounds.BufferGroup',
	'RootEntry': 'generated.formats.ovl.compounds.RootEntry',
	'Fragment': 'generated.formats.ovl.compounds.Fragment',
	'SetEntry': 'generated.formats.ovl.compounds.SetEntry',
	'AssetEntry': 'generated.formats.ovl.compounds.AssetEntry',
	'SetHeader': 'generated.formats.ovl.compounds.SetHeader',
	'OvsHeader': 'generated.formats.ovl.compounds.OvsHeader',
}

name_type_map = {}
for type_name, module in type_module_name_map.items():
	name_type_map[type_name] = getattr(import_module(module), type_name)
for class_object in type_module_name_map.values():
	if callable(getattr(class_object, 'init_attributes', None)):
		class_object.init_attributes()