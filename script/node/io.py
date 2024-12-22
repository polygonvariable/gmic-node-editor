import os
import subprocess
import threading
import tempfile
import bpy
from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, StringProperty, PointerProperty )

from ..base.library import ( get_preference_path )
from ..base.node import GMICBaseNode

class OutputNode(GMICBaseNode):
    """Output Node"""
    
    bl_idname = "GMIC_OutputNode"
    bl_label = "Output"
    bl_icon = "OUTPUT"

    name: StringProperty(name="Name", default="Output") # type: ignore
    image: PointerProperty(name="Target", type=bpy.types.Image) # type: ignore
    fast_composition: BoolProperty(name="Fast Composition", default=True) # type: ignore

    def init(self, context):
        self.default_in()

    def draw_buttons(self, context, layout):
        layout.prop(self, "name")
        layout.prop(self, "image")
        layout.prop(self, "fast_composition")
        layout.operator("node.execute_output_node", text="Execute")

    def execute(self):

        temp_name = self.name
        temp_image = self.image
        temp_command = self.get_input_value("in")

        if isinstance(temp_image, bpy.types.Image):
            if(temp_image.is_dirty):
                temp_image.reload()
        else:
            print("Output Node: Invalid input image.")
            return None

        temp_path = os.path.join(tempfile.gettempdir(), temp_name + ".png")
        print(f"Output Node: Saving image to {temp_path}")

        if(temp_image.name == "Render Result"):
            temp_image.save_render(filepath=temp_path)
        else:
            temp_image.name = temp_name
            temp_image.save(filepath=temp_path)

        threading.Thread(target=self.gmic_execute, args=(temp_command, temp_path, temp_path)).start()
        
        return None

    def gmic_execute(self, command, input_path, output_path):

        gmic_path = get_preference_path()
        gmic_optimization = self.fast_composition and "-resize 45%,45%" or ""
        gmic_command = f"{gmic_path} {input_path} {gmic_optimization} {command} -o {output_path}"

        print(f"GMIC command: {gmic_command}")

        try:
            subprocess.run(gmic_command, shell=True, check=True)

        except subprocess.CalledProcessError as e:
            print(f"GMIC command failed: {e}")
            return None
        
        if os.path.exists(output_path):
            try:
                output_image = bpy.data.images.load(output_path, check_existing=True)
                print(f"Output image loaded: {output_image.name}")
                output_image.reload()
                return output_image
            except:
                print("Failed to load output image")
                return None


class NODE_OT_ExecuteOutputNode(bpy.types.Operator):
    """Execute Output Node"""
    bl_idname = "node.execute_output_node"
    bl_label = "Execute Output Node"

    def execute(self, context):
        node = context.active_node
        if node and node.bl_idname == "GMIC_OutputNode":
            result = node.execute()
            self.report({'INFO'}, f"Output Node Result: {result}")
        else:
            self.report({'WARNING'}, "Active node is not an Output Node")
        return {'FINISHED'}


classes = [
    OutputNode,
    NODE_OT_ExecuteOutputNode
]