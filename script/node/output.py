import os
import subprocess
import threading
import tempfile
import bpy
from nodeitems_utils import NodeCategory, NodeItem, register_node_categories, unregister_node_categories
from bpy.props import ( StringProperty,BoolProperty,IntProperty,FloatProperty,EnumProperty )
from ..base.node import GMICBaseNode

class OutputNode(GMICBaseNode):
    """Output Node"""
    bl_idname = "GMICOutputNode"
    bl_label = "Output"
    bl_icon = "NODE"

    def init(self, context):
        self.inputs.new("NodeSocketString", "Name")
        self.inputs.new("NodeSocketImage", "Target")
        self.inputs["Name"].default_value = "Output"
        self.default_in()

    def draw_buttons(self, context, layout):
        layout.operator("node.execute_output_node", text="Execute")

    def execute(self):

        temp_name = self.inputs["Name"].default_value
        temp_command = self.get_input_value("in")
        temp_image = self.inputs["Target"].default_value
        if isinstance(temp_image, bpy.types.Image):
            if(temp_image.is_dirty):
                temp_image.reload()
        else:
            print("Output Node: Invalid input image.")
            return None

        temp_path = os.path.join(tempfile.gettempdir(), temp_name + ".png")
        print(f"Output Node: Saving image to {temp_path}")

        if(temp_image.name == "Render Result"):
            temp_image.save_render(temp_path)
        else:
            temp_image.name = temp_name
            temp_image.save(filepath=temp_path)

        threading.Thread(target=self.gmic_execute, args=(temp_command, temp_path, temp_path)).start()
        
        return None

    def gmic_execute(self, command, input_path, output_path):

        gmic_path = "D:/Installed/GMIC/gmic.exe"
        gmic_command = f"{gmic_path} {input_path} {command} -o {output_path}"

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
        if node and node.bl_idname == 'GMICOutputNode':
            result = node.execute()
            self.report({'INFO'}, f"Output Node Result: {result}")
        else:
            self.report({'WARNING'}, "Active node is not an Output Node")
        return {'FINISHED'}
