import logging
import math
import numpy as np

import bpy
import bmesh
import mathutils
from mathutils import Vector, Matrix, Quaternion

import plugin.utils.object
from plugin.utils.hair import get_tangent_space_mat, vcol_2_vec, MID

# changed to avoid clamping bug and squares on fins
X_START = -15.9993
Y_START = 0.999756
FUR_FIN = "_fur_fin"
FUR = "_fur"
FUR_SHELL = "_fur_shell"


def get_ob_count(lod_collections):
	return sum(len(coll.objects) for coll in lod_collections)


def create_lods():
	"""Automatic LOD generator by NDP. Generates LOD objects and automatically decimates them for LOD0-LOD5"""
	msgs = []
	logging.info(f"Generating LOD objects")

	# Get active scene and root collection
	scn = bpy.context.scene
	col = scn.collection
	col_list = bpy.types.Collection(col).children

	# enforce inclusion of all lod_collections [tick box] and their objects to avoid error
	view_layer = bpy.context.view_layer
	for layer_collection in view_layer.layer_collection.children:
		layer_collection.exclude = False

	# Make list of all LOD collections
	lod_collections = [col for col in col_list if col.name[:-1].endswith("LOD")]
	# Setup default lod ratio values
	lod_ratios = np.linspace(1.0, 0.05, num=len(lod_collections))

	# Deleting old LODs
	for lod_coll in lod_collections[1:]:
		for ob in lod_coll.objects:
			# delete old target
			bpy.data.objects.remove(ob, do_unlink=True)

	shape_keyed = []
	decimated = []
	for lod_index, (lod_coll, ratio) in enumerate(zip(lod_collections, lod_ratios)):
		if lod_index > 0:
			for ob_index, ob in enumerate(lod_collections[0].objects):
				# additional skip condition for JWE2, as shell is separate from base fur here
				if ob.data.cobra.mesh_format != "NONE":
					if is_shell(ob) and lod_index > 1:
						continue
				# check if we want to copy this one
				if is_fin(ob) and lod_index > 1:
					continue
				obj1 = copy_ob(ob, f"{scn.name}_LOD{lod_index}")
				obj1.name = f"{scn.name}_lod{lod_index}_ob{ob_index}"
				b_me = obj1.data

				# Can't create automatic LODs for models that have shape keys
				if ob.data.shape_keys:
					shape_keyed.append(ob)
				else:
					decimated.append(ob)
					if len(b_me.polygons) > 3:
						# Decimating duplicated object
						decimate = obj1.modifiers.new("Decimate", 'DECIMATE')
						decimate.ratio = ratio

				# remove additional shell material from LODs after LOD1
				if is_shell(ob) and lod_index > 1:
					# todo - actually toggle the flag on the bitfield to maintain the other bits
					b_me["flag"] = 565
					# remove shell material
					b_me.materials.pop(index=1)
	if decimated:
		msgs.append(f"{len(decimated)} LOD objects generated successfully")
	if shape_keyed:
		msgs.append(f"Can't create automatic LODs for {len(shape_keyed)} models with shape keys. Decimate those manually")
	return msgs


def vectorisclose(vector1,vector2,tolerance=0.0001):
    #Determine if the inputs are correctly utilized. 
    if not isinstance(vector1,Vector) or not isinstance(vector2,Vector) or not isinstance(tolerance,float):
        raise TypeError("Input 1 must be a vector. Input 2 must be a vector. Input 3 must be a float.")
    #Compare the components of the vectors.
    if len(vector1) != len(vector2):
        raise TypeError("Both vectors must have the same amount of components")
    #Compare components
    for component in range(0,len(vector1)):
        if not abs(vector1[component] - vector2[component]) < abs(tolerance):
            return False
    return True


def generate_rig_edit():
    """Automatic rig edit generator by NDP. Detects posed bones and automatically generates nodes and offsets them."""
    msgs = []
    logging.info(f"generating rig edit from pose")
    
    #Check if selected object is a valid armature
    if bpy.context.active_object.type != 'ARMATURE':
        #Object is not an armature. Cancelling.
        msgs.append(f"No armature selected.")
        return msgs
    
    #Store current mode
    original_mode = bpy.context.mode
    #For some reason it doesn't recognize edit_armature as a valid mode to switch to so we change it to just edit. weird.
    if original_mode == 'EDIT_ARMATURE':
        original_mode = 'EDIT'
    
    #Store number of edits
    editnumber = 0

    #Force Switch to pose mode.
    bpy.ops.object.mode_set(mode='POSE')
    
    #Get the armature
    armature = bpy.context.object
    
    #Initiate list of all posed bones
    posedbones_list = []
    
    #Update position
    bpy.context.view_layer.update()
    
    #We iterate over every pose bone and detetect which ones have been posed, and create  a list of them.
    for p_bone in armature.pose.bones:
        
        #We check if vectors have  miniscule transforms, and just consider them rounding errors and clear them.
        if vectorisclose(p_bone.location,Vector((0,0,0)),0.0001) and p_bone.location != Vector((0,0,0)):
            #Warn the user
            logging.info(f"{p_bone.name} had miniscule location transforms, assuming it is an error and clearing")
            #Clear transforms
            p_bone.location = Vector((0,0,0))
            
        if vectorisclose(p_bone.scale,Vector((1,1,1)),0.0001) and p_bone.scale != Vector((1,1,1)):
            #Warn the user
            logging.info(f"{p_bone.name} had miniscule scale transforms, assuming it is an error and clearing")
            #Clear scale
            p_bone.scale = Vector((1,1,1))
            
        if vectorisclose(Vector(p_bone.rotation_quaternion),Vector((1,0,0,0)),0.0001) and Vector(p_bone.rotation_quaternion) != Vector((1,0,0,0)):
            #Warn the user
            logging.info(f"{p_bone.name} had miniscule rotation transforms, assuming it is an error and clearing")
            #Clear rotation
            p_bone.rotation_quaternion = Quaternion((1,0,0,0))
            
        #We check if any bones have scale and warn the user, as clearing their scale will significantly alter the result.
        if not vectorisclose(p_bone.scale,Vector((1,1,1)),0.0001):
            logging.info(f"Bone has scale. Value = {repr(p_bone.scale)}, difference: {(p_bone.scale - Vector((1,1,1))).length}")
            msgs.append(f"Warning: {str(p_bone.name)} had scale transforms. Reset scale for all bones and try again.")
            return msgs
        
        #We check for NODE bones with transforms and skip them.
        if (not vectorisclose(p_bone.location,Vector((0,0,0)),0.0001) or not vectorisclose(p_bone.scale,Vector((1,1,1)),0.0001) or not vectorisclose(Vector(p_bone.rotation_quaternion),Vector((1,0,0,0)),0.0001)) and p_bone.name.startswith("NODE_"):
            #Ignore posed NODE bones and proceed to the next, their offsets can be applied directly.
            editnumber = editnumber + 1
            logging.info(f"rig edit number {editnumber}")
            logging.info(f"NODE with offsets detected. Applying offsets directly.")
            continue
        
        #We append any remaining bones that have been posed.
        if (not vectorisclose(p_bone.location,Vector((0,0,0)),0.0001) or not vectorisclose(p_bone.scale,Vector((1,1,1)),0.0001) or not vectorisclose(Vector(p_bone.rotation_quaternion),Vector((1,0,0,0)),0.0001)):
            #Append the bones to the list of posed bones.
            posedbones_list.append(p_bone)
    
    
    #Iterate over every posed bone.
    for p_bone in posedbones_list:
        #Update bone locations
        bpy.context.view_layer.update()
            
        #Debug info
        logging.info(f"rig edit number {editnumber+1}")
        logging.info(f"name: {p_bone.name}")
        logging.info(f"parent: {p_bone.parent.name}")
        
        #Get pose mode position of bonebase
        bonebase_pos_pose = Vector(p_bone.matrix.translation)
        
        #Reset position
        p_bone.location = Vector((0, 0, 0))
        #Update location after moving.
        bpy.context.view_layer.update()
        
        #Get rest mode position of bonebase
        bonebase_pos_rest = Vector(p_bone.matrix.translation)
        
        #Calculate delta offset
        bonebase_pos_delt = Vector(bonebase_pos_pose - bonebase_pos_rest)
        
        #Set back to original position
        p_bone.matrix.translation = Vector(bonebase_pos_pose)
        
        #Log locations
        logging.info(f"bonebase rest position: {bonebase_pos_rest}")
        logging.info(f"bonebase pose position: {bonebase_pos_pose}")
        logging.info(f"bonebase delt position: {bonebase_pos_delt}")

        
        #Creating the nodes            
        #We switch to edit mode to use edit bones, as they do not exist outside of edit mode.
        #Switch to edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        
        #Get edit bones
        bonebase = armature.data.edit_bones.get(p_bone.name)
        boneparent = bonebase.parent
        
        #Creating the node bone
        bonenode = armature.data.edit_bones.new(f"NODE_{p_bone.name}")
        #NOTE: Maybe here we set the bonenode to boneparent if it starts with NODE_ already
        
        #Copy parent length to node
        bonenode.length = boneparent.length
        #Copy parent matrix to node
        bonenode.matrix = boneparent.matrix.copy()
        
        #Set parent of bonenode to boneparent
        bonenode.parent = boneparent
        #Set parent of bonebase to bonenode
        bonebase.parent = bonenode
        #Node creation complete
        
        #Switch to pose mode.
        bpy.ops.object.mode_set(mode='POSE')
        
        
        
        #------------------------------------
        
        #OFFSET NODE LOCATION
        #Applying offsets to bonenode
        #Switch to pose mode
        bpy.ops.object.mode_set(mode='POSE')
        
        #Clear location
        p_bone.location = Vector((0,0,0))
        #Clear rotation
        p_bone.rotation_quaternion = Quaternion((1,0,0,0))
        
        #Offset bonenode location
        p_bone.parent.matrix.translation = p_bone.parent.matrix.translation + bonebase_pos_delt
        
        #------------------------------------
        
        #OFFSET NODE ROTATION
        
        #BUG: local Y rotation seems to get lost but otherwise everything else works.
        #To fix, maybe store local Y and use the origin rotate afterwards to make up for it using the bone's pose vector as the axis.
        
        #Origin of rotation
        origin = p_bone.head
        
        #Store pose position
        vector1 = p_bone.vector.copy()
        #Reset rotation
        p_bone.rotation_quaternion = (1, 0, 0, 0)
        bpy.context.view_layer.update()
        #Store rest position
        vector2 = p_bone.vector.copy()
        
        #Log vectors
        logging.info(f"bonebase pose vector: {vector1}")
        logging.info(f"bonebase rest vector: {vector2}")
        
        #Calculate angle between vectors
        angle_radians = vector1.angle(vector2)
        angle_degrees = math.degrees(angle_radians)
        #log angle
        logging.info(f"angle radians: {angle_radians}")
        logging.info(f"angle degrees: {angle_degrees}")
        
        #Calculate the rotation matrix
        angle = angle_radians
        #Calculate the axis
        axis = vector1.cross(vector2)
        #Log axis
        logging.info(f"axis: {axis}")
        #Create the rotation matrix
        rotation_matrix = Matrix.Rotation(-angle_radians, 4, axis)
        # Apply the final matrix to the pose bone
        p_bone.parent.matrix = Matrix.Translation(+origin) @ rotation_matrix @ Matrix.Translation(+origin).inverted() @ p_bone.parent.matrix
        #------------------------------------
        
        #Node completed. Log number of edits.
        editnumber = editnumber + 1
    
    #CREATING NODE GROUPS
    #Checking for duplicates to merge
    logging.info(f"creating node_groups to merge")
    #Initiate list
    node_list = []
    
    #We create a list of all NODES
    for p_bone in armature.pose.bones:
        if p_bone.name.startswith("NODE_"):
            node_list.append(p_bone)
    
    #Create NODE parent dictionary
    node_groups = {}
    
    #Create and sort NODE groups, we create a dictionary with a tuple of: parent,location,rotation as the key. This way we can group identical nodes.
    for p_bone in node_list:
        keytuple = (p_bone.parent.name,(round(p_bone.location.x,5),round(p_bone.location.y,5),round(p_bone.location.z,5)),(p_bone.rotation_quaternion[0],p_bone.rotation_quaternion[1],p_bone.rotation_quaternion[2],p_bone.rotation_quaternion[3]))
        if keytuple in node_groups:
            node_groups[keytuple].append(p_bone)
        else:
            node_groups[keytuple] = [p_bone]
    

    #Log node groups
    for nodegroup in node_groups:
        logging.info(f"node group: {nodegroup}")
        for node in node_groups[nodegroup]:
            logging.info(f"node: {node.name}")
    
    #store number of deleted nodes
    deletednodes = 0
    
    #Merge node groups
    for nodegroup in node_groups:
        if len(node_groups[nodegroup]) > 1:
            node_groups[nodegroup][0].name = f"NODE_{len(node_groups[nodegroup])}GROUP{node_groups[nodegroup][0].children[0].name}"
        logging.info(f"first node: {node_groups[nodegroup][0].name}")
        logging.info(f"first child: {node_groups[nodegroup][0].children[0].name}")
        for node in node_groups[nodegroup]:
            if node != node_groups[nodegroup][0]:
                logging.info(f"secondary node: {node.name}")
                logging.info(f"secondary child: {node.children[0].name}")
                
                #Switch to edit mode to edit the parents
                bpy.ops.object.mode_set(mode='EDIT')
                
                #Reparent duplicate basebones to the first node
                armature.data.edit_bones.get(node.children[0].name).parent = armature.data.edit_bones.get(node_groups[nodegroup][0].name)
                
                #Delete the duplicate nodes
                deletednodes = deletednodes + 1
                armature.data.edit_bones.remove(armature.data.edit_bones.get(node.name))
                
                #Switch back to pose mode
                bpy.ops.object.mode_set(mode='POSE')
    
    #Report amount of deleted nodes
    if deletednodes > 0:
        logging.info(f"Merged {deletednodes} nodes into node groups")
    
    #NODE GROUPS COMPLETE

        

    #----------------------------------------------------------------------------
    logging.info(f"total number of edits: {editnumber}")
    
    #Apply pose as rest position and finalize the edit.
    bpy.ops.pose.armature_apply()
    
    #Switch back to original mode. 
    bpy.ops.object.mode_set(mode=original_mode)
    
    #Return count of succesfull rig edits
    msgs.append(f"{str(editnumber)} rig edits generated succesfully")
    return msgs


def copy_ob(src_obj, lod_group_name):
	new_obj = src_obj.copy()
	new_obj.data = src_obj.data.copy()
	new_obj.name = src_obj.name + "_copy"
	new_obj.animation_data_clear()
	plugin.utils.object.link_to_collection(bpy.context.scene, new_obj, lod_group_name)
	bpy.context.view_layer.objects.active = new_obj
	return new_obj


def ob_processor_wrapper(func):
	msgs = []
	for lod_i in range(6):
		coll = get_collection_endswith(bpy.context.scene, f"_LOD{lod_i}")
		if coll is None:
			return msgs
		src_obs = [ob for ob in coll.objects if is_shell(ob)]
		trg_obs = [ob for ob in coll.objects if is_fin(ob)]
		if src_obs and trg_obs:
			msgs.append(func(src_obs[0], trg_obs[0]))
	return msgs


def create_fins_wrapper():
	logging.info(f"Creating fins")
	return ob_processor_wrapper(build_fins)


def gauge_uv_scale_wrapper():
	logging.info(f"Gauging UV scales")
	return ob_processor_wrapper(gauge_uv_factors)


def get_collection_endswith(scene, suffix):
	# get collections in scene root collection
	for coll in scene.collection.children:
		if coll.name.endswith(suffix):
			return coll


def get_ob_from_lod_and_flags(coll, flags=(565,)):
	if coll:
		for ob in coll.objects:
			if "flag" in ob and ob.data["flag"] in flags:
				return ob


def build_fins(shell_ob, fin_ob):
	try:
		shell_me = shell_ob.data
		uv_scale_x = shell_me["uv_scale_x"]
		uv_scale_y = shell_me["uv_scale_y"]
	except:
		raise AttributeError(f"{shell_ob.name} has no UV scale properties. Run 'Gauge UV Scales' first!")

	lod_group_name = plugin.utils.object.get_lod(shell_ob)
	ob = copy_ob(shell_ob, lod_group_name)

	me = ob.data
	# data is per loop
	hair_directions, loop_vertices = build_tangent_table(shell_ob.data)
	loop_coord_kd = fill_kd_tree_co(loop_vertices)

	# transfer the material
	me.materials.clear()
	me.materials.append(fin_ob.data.materials[0])
	# rename new object
	trg_name = fin_ob.name
	fin_ob.name += "dummy"
	ob.name = trg_name
	# delete old target
	bpy.data.objects.remove(fin_ob, do_unlink=True)

	# set up copy of normals from src mesh
	mod = ob.modifiers.new('DataTransfer', 'DATA_TRANSFER')
	mod.object = shell_ob
	mod.use_loop_data = True
	mod.data_types_loops = {"CUSTOM_NORMAL", }

	# needed for custom normals
	me.use_auto_smooth = True
	# create uv1 layer for fins
	me.uv_layers.new(name="UV1")
	# Get a BMesh representation
	bm = bmesh.new()  # create an empty BMesh
	bm.from_mesh(me)  # fill it in from a Mesh
	edges_start_a = bm.edges[:]
	faces = bm.faces[:]
	bm.faces.ensure_lookup_table()
	# Extrude and create geometry on side 'b'
	normals = [v.normal for v in bm.verts]
	ret = bmesh.ops.extrude_edge_only(bm, edges=edges_start_a)
	geom_extrude = ret["geom"]
	verts_extrude = [ele for ele in geom_extrude if isinstance(ele, bmesh.types.BMVert)]

	# move each extruded verts out across the surface normal
	for v, n in zip(verts_extrude, normals):
		v.co += (n * 0.00001)

	# now delete all old faces, but only faces
	bmesh.ops.delete(bm, geom=faces, context="FACES_ONLY")

	# build uv1 coords
	build_uv(ob, bm, uv_scale_x, uv_scale_y, loop_coord_kd, hair_directions)

	# Finish up, write the bmesh back to the mesh
	bm.to_mesh(me)
	bm.free()  # free and prevent further access

	# remove fur_length vgroup
	for vg_name in ("fur_length", "fur_width"):
		if vg_name in ob.vertex_groups:
			vg = ob.vertex_groups[vg_name]
			ob.vertex_groups.remove(vg)
	# only change flag for PZ
	if me.cobra.mesh_format == "NONE":
		me["flag"] = 565

	# remove the particle system, since we no longer have a fur length vertex group
	for mod in ob.modifiers:
		if mod.type == "PARTICLE_SYSTEM":
			ob.modifiers.remove(mod)

	return f'Generated fin geometry {trg_name} from {shell_ob.name}'


def get_face_ring(face):
	strip = [face, ]
	for i in range(10):
		# get linked faces
		best_face = get_best_face(strip[-1])
		if best_face:
			strip.append(best_face)
		else:
			break
	return strip


def get_link_faces(bm_face):
	return [f for e in bm_face.edges for f in e.link_faces if not f.tag and f is not bm_face]


def get_best_face(current_face):
	link_faces = get_link_faces(current_face)
	# print(len(link_faces), len(set(link_faces)))
	if link_faces:
		# get the face whose orientation is most similar
		dots = [(abs(current_face.normal.dot(f.normal)), f) for f in link_faces]
		dots.sort(key=lambda x: x[0])
		# dot product = 0 -> vectors are orthogonal
		# we need parallel normals
		best_face = dots[-1][1]
		best_face.tag = True
		return best_face


def get_best_face_dir(current_face, hair_direction):
	link_faces = get_link_faces(current_face)
	# print(len(link_faces), len(set(link_faces)))
	if link_faces:
		# get the face whose orientation is most similar
		dots = [f.edges[0] for f in link_faces]
		# we need parallel normals
		best_face = dots[-1][1]
		best_face.tag = True
		return best_face


def build_uv(ob, bm, uv_scale_x, uv_scale_y, loop_coord_kd, hair_directions):
	# get vertex group index
	# this is stored in the object, not the BMesh
	group_index = ob.vertex_groups["fur_length"].index
	# print(group_index)

	psys_fac = ob.particle_systems[0].settings.hair_length
	uv_skew_fac = 4
	vcol_layer = bm.loops.layers.color["RGBA0"]

	# only ever one deform weight layer
	deform = bm.verts.layers.deform.active

	# get uvs
	uv_0 = bm.loops.layers.uv["UV0"]
	uv_1 = bm.loops.layers.uv["UV1"]

	# basically, the whole UV strip should be oriented so that its hair tilts in the same direction
	# start by looking at the vcol of this face's two base verts in the shell mesh's original tangent space
	# decide with which edge to continue
	# pick the adjoining face whose base edge's direction aligns best with the respective tangent space
	for current_face in bm.faces:
		# this face has not been processed
		if not current_face.tag:
			# current_face.tag = True
			# add tuple face, hair_dir, a/b
			# print("new strip")
			strip = [current_face, ]
			modes = []
			# base_edge corresponds to the original edge before extrusion
			while True:
				current_face = strip[-1]
				current_face.tag = True
				base_edge, edge_a, top_edge, edge_b = current_face.edges
				a, b = get_hair_angles(base_edge, edge_a, edge_b, hair_directions, loop_coord_kd)
				# print(a, b)
				# compare both angles
				if a < b:
					# print("at b")
					# hair direction at a is closer to a->b
					# so the hair points from a to b
					# so find next face at edge_b
					look_at_edge = edge_b
					modes.append(0)
				else:
					# hair direction at b is closer to b->a
					# continue equivalent to for the other case
					look_at_edge = edge_a
					# print("at a")
					modes.append(1)
				if len(strip) == 10:
					break
				next_face = get_best_angled_face(look_at_edge, hair_directions, loop_coord_kd)
				if not next_face:
					break
				strip.append(next_face)

			assert len(strip) == len(modes)
			# print("strip", len(strip), modes)
			# faces should be mapped so that hair direction points to the left in UV space
			# store the x position
			x_pos_dic = {}
			for face, mode in zip(strip, modes):
				# print(f"mode {mode}")
				# todo - may need to handle face according to mode
				# if mode == 0:
				# 	# mode 0 - put this face's edge a to the right, because hair points from a to b
				# 	pass
				# elif mode == 1:
				# 	# mode 1 - put this face's edge b to the right, because hair points from b to a
				# 	pass
				# update X coords
				base_edge, edge_a, top_edge, edge_b = current_face.edges
				length = base_edge.calc_length() * uv_scale_x
				# print(x_pos_dic)
				ind = face.loops[0].vert.index
				# print("ind", ind)
				if ind in x_pos_dic:
					# print("0 in, index", ind)
					left = (0, 3)
					right = (1, 2)
				else:
					# print("1 in, index", ind2)
					left = (1, 2)
					right = (0, 3)
				# fall back to start if top left vertex hasn't been keyed in the dict
				x_0 = x_pos_dic.get(face.loops[left[0]].vert.index, X_START)
				# left edges
				for i in left:
					loop = face.loops[i]
					loop[uv_1].uv.x = x_0
					# print("left", loop.vert.index, x_0)
					x_pos_dic[loop.vert.index] = x_0
				# right edge
				for i in right:
					loop = face.loops[i]
					loop[uv_1].uv.x = x_0 + length
					# print("right", loop.vert.index, x_0 + length)
					x_pos_dic[loop.vert.index] = x_0 + length

				# update Y coords
				# top edge
				# print(len(base_edge.link_loops), list(base_edge.link_loops), face.loops[:2])
				for loop in face.loops[:2]:
					loop[uv_1].uv.y = Y_START
				# lower edge
				uv_0_len = (face.loops[2][uv_0].uv - face.loops[3][uv_0].uv).length
				for loop in face.loops[2:]:
					uv_0_ratio = uv_0_len / base_edge.calc_length()
					dvert = loop.vert[deform]
					if group_index in dvert:
						hair_len_fac = dvert[group_index] * psys_fac
						loop[uv_1].uv.y = Y_START - (hair_len_fac * uv_scale_y)
						vcol = loop[vcol_layer]
						r = (vcol[0] - MID)
						b = (vcol[2] - MID)
						# make shift proportional to relative UV scale of edge
						loop[uv_0].uv.x -= (r * uv_0_ratio * hair_len_fac * uv_skew_fac)
						loop[uv_0].uv.y += (b * uv_0_ratio * hair_len_fac * uv_skew_fac)
	logging.info("Finished UV generation")


def get_best_angled_face(edge_b, hair_directions, loop_coord_kd):
	link_faces = [f for f in edge_b.link_faces if not f.tag]
	if not link_faces:
		return
	results = []
	for face in link_faces:
		f_base_edge, f_edge_a, f_top_edge, f_edge_b = face.edges
		a, b = get_hair_angles(f_base_edge, f_edge_a, f_edge_b, hair_directions, loop_coord_kd)
		results.append((a, b))
	# pick the faces with the lowest angle
	# 0 = a, 1 = b
	face_ind, mode = np.unravel_index(np.argmin(results, axis=None), (len(results), 2))
	# angle should be smaller than 90° to be considered ok
	best_angle = results[face_ind][mode]
	if best_angle > math.radians(90.0):
		logging.debug(f"Discarded best face with angle {math.degrees(best_angle)}°")
		return
	next_face = link_faces[face_ind]
	return next_face


def get_hair_angles(base_edge, edge_a, edge_b, hair_directions, loop_coord_kd):
	# get the base verts
	base_vert_a = [v for v in edge_a.verts if v in base_edge.verts][0]
	base_vert_b = [v for v in edge_b.verts if v in base_edge.verts][0]
	# check both edges
	a = hair_angle_for_verts(base_vert_a, base_vert_b, hair_directions, loop_coord_kd)
	b = hair_angle_for_verts(base_vert_b, base_vert_a, hair_directions, loop_coord_kd)
	return a, b


def hair_angle_for_verts(ref_vert, other_vert, hair_directions, loop_coord_kd):
	ref_to_other = other_vert.co - ref_vert.co
	# find the closest vertex in the original mesh
	loop_vert_co, loop_vert_i, dist = loop_coord_kd.find(ref_vert.co)
	if dist > 0.0:
		logging.warning(f"Could not find a perfect match in kd find")
	# this vector rests in the original vertex's tangent plane
	hair_direction = hair_directions[loop_vert_i]
	if hair_direction.length == 0.0:
		print(f"hair_direction_a is zero")
	elif ref_to_other.length == 0.0:
		print(f"ref_to_other is zero")
	else:
		angle_a = ref_to_other.angle(hair_direction)
		# print(f"angle {angle_a}")
		return angle_a


def gauge_uv_factors(shell_ob, fin_ob):
	logging.info(f"Gauging UV scale for {fin_ob.name} from {shell_ob.name}")
	hair_length = shell_ob.particle_systems[0].settings.hair_length

	shell_me = shell_ob.data
	fin_me = fin_ob.data
	# populate a KD tree with all verts from the shell mesh
	kd = fill_kd_tree_co(shell_me.vertices)

	uv_lens = []
	v_lens = []
	uv_heights = []
	base_fur_lengths = []
	for i, p in enumerate(fin_me.polygons):
		# print(p)
		base = []
		top = []
		for loop_index in p.loop_indices:
			uvs = [(layer.data[loop_index].uv.x, 1 - layer.data[loop_index].uv.y) for layer in fin_me.uv_layers]
			# print(uvs)
			# reindeer is an edge case and starts slightly lower
			if uvs[1][1] < 0.001:
				base.append(loop_index)
			else:
				top.append(loop_index)

		if len(base) == 2:
			# print(base)
			uv_verts = [fin_me.uv_layers[1].data[loop_index].uv.x for loop_index in base]
			uv_len = abs(uv_verts[1] - uv_verts[0])
			# print(uv_len)
			loops = [fin_me.loops[loop_index] for loop_index in base]
			me_verts = [fin_me.vertices[loop.vertex_index].co for loop in loops]
			v_len = (me_verts[1] - me_verts[0]).length
			# print(v_len)
			# print("Fac", uv_len/v_len)
			uv_lens.append(uv_len)
			v_lens.append(v_len)

		if base and top:
			uv_verts = [fin_me.uv_layers[1].data[loop_index].uv.y for loop_index in (base[0], top[0])]
			uv_height = abs(uv_verts[1] - uv_verts[0])
			# print(uv_height)

			# find the closest vert on base shell mesh
			loop = fin_me.loops[base[0]]
			find_co = fin_me.vertices[loop.vertex_index].co
			co, index, dist = kd.find(find_co)
			vert = shell_me.vertices[index]
			for vertex_group in vert.groups:
				vgroup_name = shell_ob.vertex_groups[vertex_group.group].name
				if vgroup_name == "fur_length":
					base_fur_length = vertex_group.weight * hair_length
					uv_heights.append(uv_height)
					base_fur_lengths.append(base_fur_length)
				# if vgroup_name == "fur_width":
				# 	base_fur_width = vertex_group.weight
		# if i == 20:
		# 	break
	uv_scale_x = np.mean(uv_lens) / np.mean(v_lens)
	uv_scale_y = np.mean(uv_heights) / np.mean(base_fur_lengths)
	# store on mesh for consistency
	shell_me["uv_scale_x"] = uv_scale_x
	shell_me["uv_scale_y"] = uv_scale_y
	# print(base_fur_width, uv_scale_x/base_fur_width)
	return f"Found UV scale for {shell_ob.name} ({uv_scale_x:.2f}, {uv_scale_y:.2f})"


def build_tangent_table(me):
	"""Stores coord & direction"""
	me.calc_tangents()
	vcol_layer = me.vertex_colors[0].data
	hair_directions = []
	vertices = []
	for loop in me.loops:
		vertex = me.vertices[loop.vertex_index]
		vcol = vcol_layer[loop.index].color
		# vec = vcol_2_vec(vcol)
		# this used to be flat? does it matter
		r = (vcol[0] - MID)
		b = (vcol[2] - MID)
		vec = mathutils.Vector((r, -b, 0))
		hair_direction = get_tangent_space_mat(loop) @ vec
		hair_directions.append(hair_direction)
		vertices.append(vertex)
	return hair_directions, vertices


def fill_kd_tree_co(iterable):
	kd = mathutils.kdtree.KDTree(len(iterable))
	for i, v in enumerate(iterable):
		kd.insert(v.co, i)
	kd.balance()
	return kd


def _check_mats(ob, func):
	if not ob.data.materials:
		raise AttributeError(f"{ob.name} has no materials!")
	for b_mat in ob.data.materials:
		if not b_mat:
			raise AttributeError(f"{ob.name} has an empty material slot!")
		if func(b_mat):
			return True


def is_fin_mat(b_mat):
	if b_mat.name.lower().endswith(FUR_FIN):
		return True


def is_shell_mat(b_mat):
	if b_mat.name.lower().endswith(FUR_SHELL):
		return True


def is_fin(ob):
	return _check_mats(ob, is_fin_mat)


def is_shell(ob):
	return _check_mats(ob, is_shell_mat)


def num_fur_as_weights(mat_name):
	mat_name = mat_name.lower()
	# JWE2 uses same suffixes for fur, while feathers act like normal geometry
	if mat_name.endswith(FUR_FIN):
		return 0
	elif mat_name.endswith((FUR, FUR_SHELL)):
		return 1
	return 0
