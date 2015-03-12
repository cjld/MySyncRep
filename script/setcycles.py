import bpy

bpy.data.scenes['Scene'].render.engine = 'CYCLES'
bpy.data.scenes['Scene'].render.filepath = r'//output/'
bpy.data.scenes['Scene'].frame_end = 1
