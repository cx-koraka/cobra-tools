import bpy
import mathutils
import math
import time


def find_modifier_for_particle_system(object, particle_system):
	for modifier in object.modifiers:
		if modifier.type != "PARTICLE_SYSTEM":
			continue
		if modifier.particle_system == particle_system:
			return modifier
	return None


def mesh_to_hair(depsgraph, mesh_object, ob, particle_system):
	particle_modifier = find_modifier_for_particle_system(ob, particle_system)

	ob_eval = ob.evaluated_get(depsgraph)
	particle_modifier_eval = ob_eval.modifiers[particle_modifier.name]
	particle_system_eval = particle_modifier_eval.particle_system

	mesh = mesh_object.data
	vertices = mesh.vertices

	num_particles = len(particle_system.particles)
	vertex_index = 0
	for particle_index in range(num_particles):
		particle = particle_system.particles[particle_index]
		particle_eval = particle_system_eval.particles[particle_index]
		num_hair_keys = len(particle_eval.hair_keys)
		print(num_hair_keys)
		for hair_key_index in range(num_hair_keys):
			co = vertices[vertex_index].co
			hair_key = particle.hair_keys[hair_key_index]
			hair_key.co_object_set(ob_eval, particle_modifier_eval, particle_eval, co)
			vertex_index += 1


def test_hair(depsgraph, ob, particle_system):
	particle_modifier = find_modifier_for_particle_system(ob, particle_system)

	ob_eval = ob.evaluated_get(depsgraph)
	particle_modifier_eval = ob_eval.modifiers[particle_modifier.name]
	particle_system_eval = particle_modifier_eval.particle_system
	#
	# mesh = mesh_object.data
	# vertices = mesh.vertices

	num_particles = len(particle_system.particles)
	vertex_index = 0
	for particle_index in range(num_particles):
		particle = particle_system.particles[particle_index]
		particle_eval = particle_system_eval.particles[particle_index]
		num_hair_keys = len(particle_eval.hair_keys)
		print(num_hair_keys)
		for hair_key_index in range(num_hair_keys):
			# co = vertices[vertex_index].co
			hair_key = particle.hair_keys[hair_key_index]
			hair_key.co_object_set(ob_eval, particle_modifier_eval, particle_eval, (0,0,hair_key_index))
			vertex_index += 1


def mesh_to_hair_test():
	context = bpy.context
	ob = bpy.data.objects["Plane"]
	particle_system = ob.particle_systems["ParticleSettings"]
	mesh_object = bpy.data.objects["Plane-ParticleSettings"]

	depsgraph = context.evaluated_depsgraph_get()

	mesh_object_eval = mesh_object.evaluated_get(depsgraph)

	mesh_to_hair(depsgraph, mesh_object_eval, ob, particle_system)


# mesh_to_hair_test()


def add_psys(ob):
	name = "hair"
	ps_mod = ob.modifiers.new(name, 'PARTICLE_SYSTEM')
	psys = ob.particle_systems[ps_mod.name]
	psys.settings.count = len(ob.data.vertices)
	psys.settings.type = 'HAIR'
	psys.settings.emit_from = 'VERT'
	psys.settings.use_emit_random = False
	psys.settings.hair_length = 1.0
	psys.vertex_group_length = "fur_length"
	psys.settings.hair_step = 1
	psys.settings.display_step = 1


def mesh_from_data(name, verts, faces, wireframe=True):
	me = bpy.data.meshes.new(name)
	start_time = time.time()
	me.from_pydata(verts, [], faces)
	print(f"from_pydata() took {time.time() - start_time:.2f} seconds for {len(verts)} verts")
	me.update()
	ob = create_ob(name, me)
	# if wireframe:
	# 	ob.draw_type = 'WIRE'
	return ob, me


def create_ob(ob_name, ob_data):
	ob = bpy.data.objects.new(ob_name, ob_data)
	bpy.context.scene.collection.objects.link(ob)
	bpy.context.view_layer.objects.active = ob
	return ob


def unpack_swizzle(vec):
	# swizzle to avoid a matrix multiplication for global axis correction
	return -vec[0], -vec[2], vec[1]


def vcol_to_comb():

	msgs = ["Calculating...", ]

	context = bpy.context
	ob = context.object
	# particle edit mode has to be entered so that hair strands are generated
	# otherwise the non-eval ob's particle count is 0
	bpy.ops.object.mode_set(mode='PARTICLE_EDIT')
	bpy.ops.object.mode_set(mode='OBJECT')
	depsgraph = context.evaluated_depsgraph_get()
	ob_eval = ob.evaluated_get(depsgraph)
	me = ob.data
	if not ob:
		return msgs
	particle_system = ob.particle_systems[0]
	particle_modifier = find_modifier_for_particle_system(ob, particle_system)
	particle_modifier_eval = ob_eval.modifiers[particle_modifier.name]
	particle_system_eval = ob_eval.particle_systems[0]

	vertices = me.vertices
	num_particles = len(particle_system.particles)
	num_particles2 = len(particle_system_eval.particles)

	assert(len(vertices) == num_particles == num_particles2)

	# tangents have to be pre-calculated
	# this will also calculate loop normal
	me.calc_tangents()

	# loop faces
	for i, face in enumerate(me.polygons):
		# loop over face loop
		for loop_index in face.loop_indices:
			vert = me.loops[loop_index]
			vertex = me.vertices[vert.vertex_index]
			tangent_space_mat = get_tangent_space_mat(vert)
			vcol_layer = me.vertex_colors[0]
			vcol = vcol_layer.data[loop_index].color
			a = vcol[0] - 0.5
			# this is like uv, so we do 1-v
			b = -vcol[2] + 0.5
			# not sure what this does, kinda random
			c = vcol[3]
			# calculate third component for unit vector
			z = math.sqrt(-(a * a) - (b * b) + 1)
			# d = math.sqrt((a * a + b * b + z * z))
			# print("normalized", d)
			# this is the raw vector, in tangent space
			vec = mathutils.Vector((a, b, z))

			# convert to object space
			hair_direction = tangent_space_mat @ vec
			# print("t+v+d", tangent, vec, dir)
			# print("dir",dir, vec)

			# calculate root and tip of the hair
			root = vertex.co
			tip = vertex.co + hair_direction

			particle = particle_system.particles[vert.vertex_index]
			particle_eval = particle_system_eval.particles[vert.vertex_index]
			num_hair_keys = len(particle_eval.hair_keys)
			for hair_key_index in range(num_hair_keys):
				hair_key = particle.hair_keys[hair_key_index]
				hair_key.co_object_set(ob_eval, particle_modifier_eval, particle_eval, root.lerp(tip, hair_key_index/(num_hair_keys-1)))

	# ob, m = mesh_from_data("asd", verts, faces, wireframe=True)
	return msgs


def comb_to_vcol():

	msgs = ["Calculating...", ]

	context = bpy.context
	ob = context.object
	# particle edit mode has to be entered so that hair strands are generated
	# otherwise the non-eval ob's particle count is 0
	bpy.ops.object.mode_set(mode='PARTICLE_EDIT')
	bpy.ops.object.mode_set(mode='OBJECT')
	depsgraph = context.evaluated_depsgraph_get()
	ob_eval = ob.evaluated_get(depsgraph)
	me = ob.data
	if not ob:
		return msgs
	particle_system = ob.particle_systems[0]
	particle_modifier = find_modifier_for_particle_system(ob, particle_system)
	particle_modifier_eval = ob_eval.modifiers[particle_modifier.name]
	particle_system_eval = ob_eval.particle_systems[0]

	vertices = me.vertices
	num_particles = len(particle_system.particles)
	num_particles2 = len(particle_system_eval.particles)

	assert(len(vertices) == num_particles == num_particles2)

	# tangents have to be pre-calculated
	# this will also calculate loop normal
	me.calc_tangents()

	# loop faces
	for i, face in enumerate(me.polygons):
		# loop over face loop
		for loop_index in face.loop_indices:
			vert = me.loops[loop_index]
			tangent_space_mat = get_tangent_space_mat(vert)

			particle = particle_system.particles[vert.vertex_index]
			particle_eval = particle_system_eval.particles[vert.vertex_index]
			num_hair_keys = len(particle_eval.hair_keys)

			root = particle.hair_keys[0].co_object(ob_eval, particle_modifier_eval, particle_eval)
			tip = particle.hair_keys[num_hair_keys - 1].co_object(ob_eval, particle_modifier_eval, particle_eval)

			hair_direction = (tip - root).normalized()
			vec = tangent_space_mat.inverted() @ hair_direction
			vcol_layer = me.vertex_colors[0]
			vcol = vcol_layer.data[loop_index].color
			vcol[0] = vec.x + 0.5
			vcol[2] = -vec.y + 0.5

	return msgs


def get_tangent_space_mat(vert):
	tangent = vert.tangent
	normal = vert.normal
	bitangent = vert.bitangent_sign * normal.cross(tangent)
	tangent_space_mat = mathutils.Matrix((tangent, bitangent, normal)).transposed()
	# print(tangent_space_mat)
	# print(normal, tangent, bitangent)
	return tangent_space_mat
