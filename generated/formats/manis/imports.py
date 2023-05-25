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
	'Rangeshort': 'generated.formats.base.basic',
	'Float': 'generated.formats.base.basic',
	'Double': 'generated.formats.base.basic',
	'Hfloat': 'generated.formats.base.basic',
	'ZString': 'generated.formats.base.basic',
	'ZStringBuffer': 'generated.formats.base.compounds.ZStringBuffer',
	'PadAlign': 'generated.formats.base.compounds.PadAlign',
	'FixedString': 'generated.formats.base.compounds.FixedString',
	'Vector3': 'generated.formats.base.compounds.Vector3',
	'Bool': 'generated.formats.ovl_base.basic',
	'OffsetString': 'generated.formats.ovl_base.basic',
	'Compression': 'generated.formats.ovl_base.enums.Compression',
	'VersionInfo': 'generated.formats.ovl_base.bitfields.VersionInfo',
	'Pointer': 'generated.formats.ovl_base.compounds.Pointer',
	'LookupPointer': 'generated.formats.ovl_base.compounds.LookupPointer',
	'ArrayPointer': 'generated.formats.ovl_base.compounds.ArrayPointer',
	'CondPointer': 'generated.formats.ovl_base.compounds.CondPointer',
	'ForEachPointer': 'generated.formats.ovl_base.compounds.ForEachPointer',
	'MemStruct': 'generated.formats.ovl_base.compounds.MemStruct',
	'SmartPadding': 'generated.formats.ovl_base.compounds.SmartPadding',
	'ZStringObfuscated': 'generated.formats.ovl_base.basic',
	'GenericHeader': 'generated.formats.ovl_base.compounds.GenericHeader',
	'Empty': 'generated.formats.ovl_base.compounds.Empty',
	'ZStringList': 'generated.formats.ovl_base.compounds.ZStringList',
	'ChannelName': 'generated.formats.manis.basic',
	'Int48': 'generated.formats.manis.basic',
	'ManisDtype': 'generated.formats.manis.bitfields.ManisDtype',
	'SegmentInfo': 'generated.formats.manis.bitfields.SegmentInfo',
	'ChannelSize': 'generated.formats.manis.bitfields.ChannelSize',
	'PosBaseKey': 'generated.formats.manis.bitfields.PosBaseKey',
	'Key94': 'generated.formats.manis.bitfields.Key94',
	'Key94B': 'generated.formats.manis.bitfields.Key94B',
	'Key94C': 'generated.formats.manis.bitfields.Key94C',
	'ManisRoot': 'generated.formats.manis.compounds.ManisRoot',
	'ManiInfo': 'generated.formats.manis.compounds.ManiInfo',
	'Buffer1': 'generated.formats.manis.compounds.Buffer1',
	'KeysReader': 'generated.formats.manis.compounds.KeysReader',
	'InfoHeader': 'generated.formats.manis.compounds.InfoHeader',
	'Vector4H': 'generated.formats.manis.compounds.Vector4H',
	'Vector3H': 'generated.formats.manis.compounds.Vector3H',
	'Vector2': 'generated.formats.manis.compounds.Vector2',
	'FloatsGrabber': 'generated.formats.manis.compounds.FloatsGrabber',
	'Segment': 'generated.formats.manis.compounds.Segment',
	'String32': 'generated.formats.manis.compounds.String32',
	'CompressedManiData': 'generated.formats.manis.compounds.CompressedManiData',
	'ManiBlock': 'generated.formats.manis.compounds.ManiBlock',
	'SegmentsReader': 'generated.formats.manis.compounds.SegmentsReader',
	'ChunkSizes': 'generated.formats.manis.compounds.ChunkSizes',
	'SubChunkReader': 'generated.formats.manis.compounds.SubChunkReader',
	'UnkChunkList': 'generated.formats.manis.compounds.UnkChunkList',
	'WeirdElementOne': 'generated.formats.manis.compounds.WeirdElementOne',
	'WeirdElementTwoReader': 'generated.formats.manis.compounds.WeirdElementTwoReader',
	'SubChunk': 'generated.formats.manis.compounds.SubChunk',
	'WeirdElementTwo': 'generated.formats.manis.compounds.WeirdElementTwo',
}

name_type_map = {}
for type_name, module in type_module_name_map.items():
	name_type_map[type_name] = getattr(import_module(module), type_name)
for class_object in name_type_map.values():
	if callable(getattr(class_object, 'init_attributes', None)):
		class_object.init_attributes()
