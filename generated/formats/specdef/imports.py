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
	'SpecdefDtype': 'generated.formats.specdef.enums.SpecdefDtype',
	'SpecdefRoot': 'generated.formats.specdef.compounds.SpecdefRoot',
	'PtrList': 'generated.formats.specdef.compounds.PtrList',
	'Spec': 'generated.formats.specdef.compounds.Spec',
	'NamePtr': 'generated.formats.specdef.compounds.NamePtr',
	'DataPtr': 'generated.formats.specdef.compounds.DataPtr',
	'BooleanData': 'generated.formats.specdef.compounds.BooleanData',
	'Int8Data': 'generated.formats.specdef.compounds.Int8Data',
	'Int16Data': 'generated.formats.specdef.compounds.Int16Data',
	'Int32Data': 'generated.formats.specdef.compounds.Int32Data',
	'Int64Data': 'generated.formats.specdef.compounds.Int64Data',
	'Uint8Data': 'generated.formats.specdef.compounds.Uint8Data',
	'Uint16Data': 'generated.formats.specdef.compounds.Uint16Data',
	'Uint32Data': 'generated.formats.specdef.compounds.Uint32Data',
	'Uint64Data': 'generated.formats.specdef.compounds.Uint64Data',
	'FloatData': 'generated.formats.specdef.compounds.FloatData',
	'StringData': 'generated.formats.specdef.compounds.StringData',
	'Vector2': 'generated.formats.specdef.compounds.Vector2',
	'Vector3': 'generated.formats.specdef.compounds.Vector3',
	'ArrayData': 'generated.formats.specdef.compounds.ArrayData',
	'ChildSpecData': 'generated.formats.specdef.compounds.ChildSpecData',
	'ReferenceToObjectData': 'generated.formats.specdef.compounds.ReferenceToObjectData',
	'Data': 'generated.formats.specdef.compounds.Data',
}

name_type_map = {}
for type_name, module in type_module_name_map.items():
	name_type_map[type_name] = getattr(import_module(module), type_name)
for class_object in type_module_name_map.values():
	if callable(getattr(class_object, 'init_attributes', None)):
		class_object.init_attributes()