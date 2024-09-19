bl_info = {
    "name": "Simple Sidebar Panel",
    "blender": (2, 80, 0), 
    "category": "3D View", 
}

import bpy

def init_properties():
    bpy.types.Scene.my_text = bpy.props.StringProperty(
        name="Masukkan Text",
        description="Enter some text"
    )
    bpy.types.Scene.font_size = bpy.props.IntProperty(
        name="Font Size",
        description="Choose font size",
        default=12,
        min=8,
        max=72
    )

def clear_properties():
    del bpy.types.Scene.my_text
    del bpy.types.Scene.font_size


class OBJECT_PT_my_panel(bpy.types.Panel):
    bl_label = "DUAR PANEL"  
    bl_idname = "OBJECT_PT_my_panel"  
    bl_space_type = 'VIEW_3D'  
    bl_region_type = 'UI'  
    bl_category = "Tool"  

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Silahkan Masukkan Teks Dibawah") 
        layout.prop(scene, "my_text") 
        layout.prop(scene, "font_size")  
        layout.operator("object.simple_operator")  

class OBJECT_OT_simple_operator(bpy.types.Operator):
    bl_label = "Buat"
    bl_idname = "object.simple_operator"

    def execute(self, context):
        self.report({'INFO'}, "Operator executed")
        return {'FINISHED'}

def register():
    init_properties()
    bpy.utils.register_class(OBJECT_PT_my_panel)
    bpy.utils.register_class(OBJECT_OT_simple_operator)

def unregister():
    clear_properties()
    bpy.utils.unregister_class(OBJECT_PT_my_panel)
    bpy.utils.unregister_class(OBJECT_OT_simple_operator)

if __name__ == "__main__":
    register()
