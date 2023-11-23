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
	'Vector2': 'generated.formats.base.compounds.Vector2',
	'Vector3': 'generated.formats.base.compounds.Vector3',
	'Vector4': 'generated.formats.ms2.compounds.Vector4',
	'Bool': 'generated.formats.ovl_base.basic',
	'OffsetString': 'generated.formats.ovl_base.basic',
	'Compression': 'generated.formats.ovl_base.enums.Compression',
	'VersionInfo': 'generated.formats.ovl_base.bitfields.VersionInfo',
	'Pointer': 'generated.formats.ovl_base.compounds.Pointer',
	'Reference': 'generated.formats.ovl_base.compounds.Reference',
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
	'BiosynVersion': 'generated.formats.ms2.basic',
	'MainVersion': 'generated.formats.ms2.basic',
	'BonePointerIndex': 'generated.formats.ms2.basic',
	'Jwe1Collision': 'generated.formats.ms2.enums.Jwe1Collision',
	'Jwe1Surface': 'generated.formats.ms2.enums.Jwe1Surface',
	'RigidBodyFlag': 'generated.formats.ms2.enums.RigidBodyFlag',
	'MeshFormat': 'generated.formats.ms2.enums.MeshFormat',
	'WeightsFlag': 'generated.formats.ms2.bitfields.WeightsFlag',
	'WeightsFlagMalta': 'generated.formats.ms2.bitfields.WeightsFlagMalta',
	'ModelFlag': 'generated.formats.ms2.bitfields.ModelFlag',
	'ChunkedModelFlag': 'generated.formats.ms2.bitfields.ChunkedModelFlag',
	'ModelFlagZT': 'generated.formats.ms2.bitfields.ModelFlagZT',
	'ModelFlagDLA': 'generated.formats.ms2.bitfields.ModelFlagDLA',
	'RenderFlag': 'generated.formats.ms2.bitfields.RenderFlag',
	'CollisionType': 'generated.formats.ms2.enums.CollisionType',
	'Matrix': 'generated.formats.ms2.compounds.Matrix',
	'Matrix44': 'generated.formats.ms2.compounds.Matrix44',
	'Matrix33': 'generated.formats.ms2.compounds.Matrix33',
	'AxisAngle': 'generated.formats.ms2.compounds.AxisAngle',
	'StreamDebugger': 'generated.formats.ms2.compounds.StreamDebugger',
	'Bone': 'generated.formats.ms2.compounds.Bone',
	'Ms2Root': 'generated.formats.ms2.compounds.Ms2Root',
	'BufferPresence': 'generated.formats.ms2.compounds.BufferPresence',
	'MaterialName': 'generated.formats.ms2.compounds.MaterialName',
	'LodInfo': 'generated.formats.ms2.compounds.LodInfo',
	'Object': 'generated.formats.ms2.compounds.Object',
	'MeshData': 'generated.formats.ms2.compounds.MeshData',
	'ChunkedMesh': 'generated.formats.ms2.compounds.ChunkedMesh',
	'NewMeshData': 'generated.formats.ms2.compounds.NewMeshData',
	'PcMeshData': 'generated.formats.ms2.compounds.PcMeshData',
	'ZtMeshData': 'generated.formats.ms2.compounds.ZtMeshData',
	'MeshDataWrap': 'generated.formats.ms2.compounds.MeshDataWrap',
	'ZTPreBones': 'generated.formats.ms2.compounds.ZTPreBones',
	'DLAPreBones': 'generated.formats.ms2.compounds.DLAPreBones',
	'FloatsY': 'generated.formats.ms2.compounds.FloatsY',
	'Model': 'generated.formats.ms2.compounds.Model',
	'ZtTriBlockInfo': 'generated.formats.ms2.compounds.ZtTriBlockInfo',
	'ZtVertBlockInfo': 'generated.formats.ms2.compounds.ZtVertBlockInfo',
	'InfoZTMemPool': 'generated.formats.ms2.compounds.InfoZTMemPool',
	'StreamsZTHeader': 'generated.formats.ms2.compounds.StreamsZTHeader',
	'Buffer0': 'generated.formats.ms2.compounds.Buffer0',
	'BufferInfo': 'generated.formats.ms2.compounds.BufferInfo',
	'ModelInfo': 'generated.formats.ms2.compounds.ModelInfo',
	'ModelReader': 'generated.formats.ms2.compounds.ModelReader',
	'Ms2InfoHeader': 'generated.formats.ms2.compounds.Ms2InfoHeader',
	'TriChunk': 'generated.formats.ms2.compounds.TriChunk',
	'VertChunk': 'generated.formats.ms2.compounds.VertChunk',
	'MinusPadding': 'generated.formats.ms2.compounds.MinusPadding',
	'ZerosPadding': 'generated.formats.ms2.compounds.ZerosPadding',
	'AbstractPointer': 'generated.formats.ms2.compounds.AbstractPointer',
	'BonePointer': 'generated.formats.ms2.compounds.BonePointer',
	'RotationRange': 'generated.formats.ms2.compounds.RotationRange',
	'IKEntryOld': 'generated.formats.ms2.compounds.IKEntryOld',
	'IKEntry': 'generated.formats.ms2.compounds.IKEntry',
	'IKTarget': 'generated.formats.ms2.compounds.IKTarget',
	'IKInfo': 'generated.formats.ms2.compounds.IKInfo',
	'JointTransform': 'generated.formats.ms2.compounds.JointTransform',
	'RigidBody': 'generated.formats.ms2.compounds.RigidBody',
	'JointPointer': 'generated.formats.ms2.compounds.JointPointer',
	'Constraint': 'generated.formats.ms2.compounds.Constraint',
	'PushConstraint': 'generated.formats.ms2.compounds.PushConstraint',
	'StretchConstraint': 'generated.formats.ms2.compounds.StretchConstraint',
	'RagdollConstraint': 'generated.formats.ms2.compounds.RagdollConstraint',
	'Sphere': 'generated.formats.ms2.compounds.Sphere',
	'BoundingBox': 'generated.formats.ms2.compounds.BoundingBox',
	'Capsule': 'generated.formats.ms2.compounds.Capsule',
	'Cylinder': 'generated.formats.ms2.compounds.Cylinder',
	'ConvexHull': 'generated.formats.ms2.compounds.ConvexHull',
	'MeshCollisionIndex': 'generated.formats.ms2.compounds.MeshCollisionIndex',
	'MeshCollisionChunk': 'generated.formats.ms2.compounds.MeshCollisionChunk',
	'MeshCollisionOptimizer': 'generated.formats.ms2.compounds.MeshCollisionOptimizer',
	'MeshCollision': 'generated.formats.ms2.compounds.MeshCollision',
	'HitCheck': 'generated.formats.ms2.compounds.HitCheck',
	'JointInfo': 'generated.formats.ms2.compounds.JointInfo',
	'HitcheckReader': 'generated.formats.ms2.compounds.HitcheckReader',
	'HitcheckPointerReader': 'generated.formats.ms2.compounds.HitcheckPointerReader',
	'JointData': 'generated.formats.ms2.compounds.JointData',
	'BoneInfo': 'generated.formats.ms2.compounds.BoneInfo',
	'MeshCollisionData': 'generated.formats.ms2.compounds.MeshCollisionData',
}

name_type_map = {}
for type_name, module in type_module_name_map.items():
	name_type_map[type_name] = getattr(import_module(module), type_name)
for class_object in name_type_map.values():
	if callable(getattr(class_object, 'init_attributes', None)):
		class_object.init_attributes()
