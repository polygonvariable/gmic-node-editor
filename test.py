import os
import subprocess
import threading
import math
import tempfile
import bpy
from nodeitems_utils import NodeCategory, NodeItem, register_node_categories, unregister_node_categories
from bpy.props import (StringProperty,BoolProperty,IntProperty,FloatProperty,EnumProperty)

class GMICNodeTree(bpy.types.NodeTree):
    """G'MIC Node Editor"""
    bl_idname = "GMIC_NodeTree"
    bl_label = "G'MIC Node Editor"
    bl_icon = "NODETREE"
    

class GMICNode(bpy.types.Node):
    """GMIC Node"""
    bl_idname = "GMICNode"
    bl_label = "GMIC Node"
    bl_icon = "NODE"

    def default_in(self):
        self.inputs.new("NodeSocketString", "in")
        self.inputs["in"].hide_value = True

    def default_out(self):
        self.outputs.new("NodeSocketString", "out")

    def get_input_value(self, input_name):
        input_socket = self.inputs.get(input_name)
        if input_socket and input_socket.is_linked:
            from_node = input_socket.links[0].from_node
            if hasattr(from_node, "execute"):
                return from_node.execute()
        else:
            return self.inputs[input_name].default_value
        return ""
    

class CommandNode(GMICNode):
    """Command Node"""
    bl_idname = "GMICCommandNode"
    bl_label = "Command Node"
    bl_icon = "NODE"

    def init(self, context):
        self.inputs.new("NodeSocketString", "Command")
        self.default_in()
        self.default_out()

    def execute(self):
        temp_cmd = self.get_input_value("in")
        temp_cmd += " " + self.get_input_value("Command")
        return temp_cmd
    
class FilterLineNode(GMICNode):
    """Filter Line Node"""
    bl_idname = "GMICFilterLineNode"
    bl_label = "Filter Line"
    bl_icon = "NODE"

    thinning: FloatProperty(default=3.0, min=0.0, max=10.0)
    recovery: FloatProperty(default=1.5, min=0.0, max=4.0)
    brightness: FloatProperty(default=1.0, min=0.0, max=4.0)
    details: FloatProperty(default=1.0, min=0.0, max=4.0)

    def init(self, context):
        self.default_in()
        self.default_out()

    def draw_buttons(self, context, layout):
        layout.prop(self, "thinning", text="Thinning")
        layout.prop(self, "recovery", text="Recovery")
        layout.prop(self, "brightness", text="Brightness")
        layout.prop(self, "details", text="Details")

    def execute(self):
        temp_cmd = self.get_input_value("in")
        temp_cmd += " -afre_edge 0," + str(self.thinning) + "," + str(self.recovery) + "," + str(self.brightness) + "," + str(self.details)
        return temp_cmd
    
class FilterBlurNode(GMICNode):
    """Filter Blur Node"""
    bl_idname = "GMICFilterBlurNode"
    bl_label = "Filter Blur"
    bl_icon = "NODE"

    amount: FloatProperty(default=3.0, min=0.0, max=100.0)

    def init(self, context):
        self.default_in()
        self.default_out()

    def draw_buttons(self, context, layout):
        layout.prop(self, "amount", text="Amount")

    def execute(self):
        temp_cmd = self.get_input_value("in")
        temp_cmd += " -blur " + str(math.floor(self.amount))
        return temp_cmd
    
class OutputNode(GMICNode):
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

        #temp_path = os.path.join(tempfile.gettempdir(), temp_name + ".png")
        temp_path = os.path.join("d:/temp.png")
        print(f"Output Node: Saving image to {temp_path}")

        if(temp_image.name == "Render Result"):
            temp_image.save_render(temp_path)
        else:
            temp_image.name = temp_name
            temp_image.save(filepath=temp_path)

        threading.Thread(target=self.gmic_execute, args=(temp_command, temp_path, os.path.join("d:/temps.png"))).start()
        
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


classes = [
    GMICNodeTree, CommandNode, OutputNode, NODE_OT_ExecuteOutputNode, FilterBlurNode, FilterLineNode
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

    bpy.data.node_groups.new("Node Tree", "GMIC_NodeTree")
    node_tree = bpy.data.node_groups["Node Tree"]

    value_node1 = node_tree.nodes.new("GMICCommandNode")
    value_node1.location = (0, 200)
    value_node1.value = 5.0

    execute_node1 = node_tree.nodes.new("GMICOutputNode")
    execute_node1.location = (150, 200)

    blur_node1 = node_tree.nodes.new("GMICFilterBlurNode")
    blur_node1.location = (200, 150)

    line_node1 = node_tree.nodes.new("GMICFilterLineNode")
    line_node1.location = (200, 250)