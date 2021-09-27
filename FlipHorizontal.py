bl_info = {
    "name": "Flip Horizontal",
    "author": "@Gomi_Deer",
    "description": "(Default hotkey: Shift+F) Flips the active scene camera along it's x-axis. Useful to quickly see a composition in a new angle.",
    "version": (1, 0),
    "blender" : (2, 80, 0),
    "category": "Scene"
}

import bpy
import mathutils

def mult(vec1, vec2):
    temp = []
    

class FlipCameraOnLocalX(bpy.types.Operator):
    """Flips the current scene's active camera horizontally."""
    bl_idname = "camera.flip_x"
    bl_label = "Flip Active Camera Horizontally"
    
    def execute(self, context):
        if bpy.context.scene.camera:
            bpy.context.scene.camera.scale = mathutils.Vector(x * y for x, y in zip(bpy.context.scene.camera.scale, mathutils.Vector((-1, 1, 1))))
        else:
            raise TypeError('Scene does not have an active camera.')
        return {'FINISHED'}


addon_keymaps = []


def register():
    bpy.utils.register_class(FlipCameraOnLocalX)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new(FlipCameraOnLocalX.bl_idname, 'F', 'PRESS', shift=True)
        addon_keymaps.append((km, kmi))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    bpy.utils.unregister_class(FlipCameraOnLocalX)
    