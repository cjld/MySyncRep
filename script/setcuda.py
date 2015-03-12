import bpy

system = bpy.context.user_preferences.system
system.compute_device_type = 'CUDA'

try:
    system.compute_device = 'CUDA_MULTI_0'
except Exception as e:
    print(e)
    print("Warning: unable to find CUDA_MULTI_0")
    print("Using CUDA_0")
    system.compute_device = 'CUDA_0'

bpy.ops.wm.save_userpref()
