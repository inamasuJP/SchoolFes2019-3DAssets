import bpy

bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.resolution_percentage = 25

#bpy.data.scenes['Scene'].render.engine = 'CYCLES'
path = bpy.context.blend_data.filepath.rstrip(bpy.path.basename(bpy.context.blend_data.filepath)) + "../image/" +  bpy.path.basename(bpy.context.blend_data.filepath).split(".")[0] +".png"
bpy.data.scenes["Scene"].render.filepath = path

bpy.ops.render.render( write_still=True )

#bpy.data.images['Render Result'].save_render(filepath =  '../../'+ bpy.path.basename(bpy.context.blend_data.filepath).split(".")[0]  +'.png')