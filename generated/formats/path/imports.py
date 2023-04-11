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
	'Vector2': 'generated.formats.path.compounds.Vector2',
	'Vector3': 'generated.formats.path.compounds.Vector3',
	'Vector4': 'generated.formats.path.compounds.Vector4',
	'PathExtrusion': 'generated.formats.path.compounds.PathExtrusion',
	'PathMaterial': 'generated.formats.path.compounds.PathMaterial',
	'PathMaterialData': 'generated.formats.path.compounds.PathMaterialData',
	'PathResource': 'generated.formats.path.compounds.PathResource',
	'PathJoinPartResourceRoot': 'generated.formats.path.compounds.PathJoinPartResourceRoot',
	'PathJoinPartResource': 'generated.formats.path.compounds.PathJoinPartResource',
	'PathJoinPartResourceList': 'generated.formats.path.compounds.PathJoinPartResourceList',
	'PointsList': 'generated.formats.path.compounds.PointsList',
	'PathSupport': 'generated.formats.path.compounds.PathSupport',
	'PathType': 'generated.formats.path.compounds.PathType',
	'SupportSetRoot': 'generated.formats.path.compounds.SupportSetRoot',
	'SubBraceStruct': 'generated.formats.path.compounds.SubBraceStruct',
	'BrokeStruct': 'generated.formats.path.compounds.BrokeStruct',
	'Connector': 'generated.formats.path.compounds.Connector',
	'ConnectorMultiJoint': 'generated.formats.path.compounds.ConnectorMultiJoint',
	'Joint': 'generated.formats.path.compounds.Joint',
	'Pillar': 'generated.formats.path.compounds.Pillar',
	'Footer': 'generated.formats.path.compounds.Footer',
	'SupportSetData': 'generated.formats.path.compounds.SupportSetData',
}

name_type_map = {}
for type_name, module in type_module_name_map.items():
	name_type_map[type_name] = getattr(import_module(module), type_name)
for class_object in name_type_map.values():
	if callable(getattr(class_object, 'init_attributes', None)):
		class_object.init_attributes()