import os
import tempfile
import random

import bpy
from bpy.props import ( BoolProperty, FloatProperty, EnumProperty, StringProperty, IntProperty, PointerProperty )

from ...base.node import GMICBaseNode
from ...base.library import save_image, run_gmic
from ...operator.exec_rungmic import OP_ExecuteRunGMIC
from ...operator.exec_render import OP_ExecuteRenderLayer

class IO_Output(GMICBaseNode):
    """Output Node"""
    
    bl_idname = "GMIC_IO_OutputNode"
    bl_label = "Output"
    bl_icon = "OUTPUT"

    name: StringProperty(name="Name", default="Output") # type: ignore
    upscale: BoolProperty(name="Upscale", default=True) # type: ignore

    def init(self, context):
        self.default_in()

    def draw_buttons(self, context, layout):
        layout.prop(self, "name")
        layout.prop(self, "upscale")
        layout.operator(OP_ExecuteRunGMIC.bl_idname, text="Execute")

    def execute(self):
        try:

            temp_name = self.name
            temp_upscale = self.upscale and "-resize 250%,250%" or ""
            temp_command = self.get_input_value("in") + f" {temp_upscale}"

            if not run_gmic(command=temp_command, name=temp_name):
                raise Exception("Failed to execute GMIC command")

            return True

        except:
            print("Failed to execute Output Node")
            return False

class IO_Input(GMICBaseNode):
    """Input Node"""
    
    bl_idname = "GMIC_IO_InputNode"
    bl_label = "Input"
    bl_icon = "OUTPUT"

    rand_name = f"Input_{random.randint(0, 100)}"

    name: StringProperty(name="Name", default=rand_name) # type: ignore
    image: PointerProperty(name="Target", type=bpy.types.Image) # type: ignore
    downscale: BoolProperty(name="Downscale", default=True) # type: ignore

    def init(self, context):
        self.default_out()
        name = f"Input_{random.randint(0, 100)}"

    def draw_buttons(self, context, layout):
        layout.prop(self, "name")
        layout.prop(self, "image")
        layout.prop(self, "downscale")
        layout.operator(OP_ExecuteRenderLayer.bl_idname, text="Render Layers")

    def execute(self):
        try:

            path = save_image(image=self.image, name=self.name)
            gmic_downscale = self.downscale and "-resize 40%,40%" or ""

            return f"{path} {gmic_downscale}"
        
        except:
            print("Failed to execute Input Node")
            return None

class IO_AppendIndex(GMICBaseNode):
    """Append Index to previous node"""

    bl_idname = "GMIC_IO_AppendIndex"
    bl_label = "Append Index"
    bl_width_default = 165

    node_props = ["index"]
    
    index: IntProperty(
        name="Index",
        default=0,
        min=0, 
        max=100,
    ) # type: ignore

    def create_command(self):
        return f"[{self.index}]"

    def finalize_command(self):
        temp_cmd = self.get_input_value("in")

        all_cmd = temp_cmd.split("-")
        if len(all_cmd) < 2:
            return temp_cmd

        last_cmd = all_cmd[-1]

        last_cmd_name = last_cmd.split(" ")[0]
        last_cmd_value = last_cmd.replace(last_cmd_name, "")

        last_cmd_new = last_cmd_name + self.create_command() + last_cmd_value

        return temp_cmd.replace(last_cmd, last_cmd_new)
    
node_classes = [
    IO_Output,
    IO_Input,
    IO_AppendIndex
]