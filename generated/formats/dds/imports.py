from importlib import import_module


type_module_name_map = {
	'Byte': 'generated.formats.dds.basic',
	'Ubyte': 'generated.formats.dds.basic',
	'Uint64': 'generated.formats.base.basic',
	'Int64': 'generated.formats.base.basic',
	'Uint': 'generated.formats.dds.basic',
	'Ushort': 'generated.formats.dds.basic',
	'Int': 'generated.formats.dds.basic',
	'Short': 'generated.formats.dds.basic',
	'Char': 'generated.formats.dds.basic',
	'Normshort': 'generated.formats.base.basic',
	'Float': 'generated.formats.dds.basic',
	'Double': 'generated.formats.base.basic',
	'Hfloat': 'generated.formats.base.basic',
	'ZString': 'generated.formats.base.basic',
	'ZStringBuffer': 'generated.formats.base.compounds.ZStringBuffer',
	'PadAlign': 'generated.formats.base.compounds.PadAlign',
	'FixedString': 'generated.formats.base.compounds.FixedString',
	'FourCC': 'generated.formats.dds.enums.FourCC',
	'DxgiFormat': 'generated.formats.dds.enums.DxgiFormat',
	'D3D10ResourceDimension': 'generated.formats.dds.enums.D3D10ResourceDimension',
	'HeaderFlags': 'generated.formats.dds.bitstructs.HeaderFlags',
	'PixelFormatFlags': 'generated.formats.dds.bitstructs.PixelFormatFlags',
	'Caps1': 'generated.formats.dds.bitstructs.Caps1',
	'Caps2': 'generated.formats.dds.bitstructs.Caps2',
	'PixelFormat': 'generated.formats.dds.structs.PixelFormat',
	'Dxt10Header': 'generated.formats.dds.structs.Dxt10Header',
	'Header': 'generated.formats.dds.structs.Header',
}

name_type_map = {}
for type_name, module in type_module_name_map.items():
	name_type_map[type_name] = getattr(import_module(module), type_name)
for class_object in name_type_map.values():
	if callable(getattr(class_object, 'init_attributes', None)):
		class_object.init_attributes()
