import re
import os
import random
import subprocess
import threading
import tempfile

import bpy
from bpy.props import ( BoolProperty, FloatProperty, EnumProperty, StringProperty, IntProperty, PointerProperty )
from bpy import context

from ...base.node import GMICBaseNode
from ...base.library import save_image, run_gmic, run_gmic_batch
from ...operator.exec_rungmic import OP_ExecuteRunGMIC
from ...operator.exec_render import OP_ExecuteRenderLayer

class IO_Output(GMICBaseNode):
    """Output Node"""
    
    bl_idname = "GMIC_IO_OutputNode"
    bl_label = "Output"
    bl_icon = "OUTPUT"

    name: StringProperty(name="Name", default="Output") # type: ignore
    upscale: BoolProperty(name="Upscale", default=True) # type: ignore
    separate_thread: BoolProperty(name="Separate Thread", default=False) # type: ignore

    def init(self, context):
        self.default_in()

    def draw_buttons(self, context, layout):
        layout.prop(self, "name")
        layout.prop(self, "upscale")
        layout.prop(self, "separate_thread")
        layout.operator(OP_ExecuteRunGMIC.bl_idname, text="Execute")

    def execute(self):
        try:

            temp_name = self.name
            temp_upscale = self.upscale and "-resize 250%,250%" or ""
            temp_command = self.get_input_value("in") + f" {temp_upscale}"

            if "NULL_IMAGE" in temp_command:
                raise Exception("Invalid input image")

            if self.separate_thread:
                thread = threading.Thread(target=run_gmic, args=(temp_command, temp_name))
                thread.start()

            else:
                if not run_gmic(temp_command, temp_name):
                    raise Exception("Failed to execute GMIC command")

            return self.separate_thread and "Process started" or "Image processed"

        except Exception as e:
            return e

class IO_OutputBatch(GMICBaseNode):
    """Output Batch Node"""
    
    bl_idname = "GMIC_IO_OutputBatchNode"
    bl_label = "Output Batch"
    bl_icon = "OUTPUT"

    input_path: StringProperty(name="Input", subtype="DIR_PATH") # type: ignore
    output_path: StringProperty(name="Output", subtype="DIR_PATH") # type: ignore
    separate_thread: BoolProperty(name="Separate Thread", default=False) # type: ignore

    def init(self, context):
        self.default_in()

    def draw_buttons(self, context, layout):
        layout.prop(self, "input_path")
        layout.prop(self, "output_path")
        layout.prop(self, "separate_thread")
        layout.operator(OP_ExecuteRunGMIC.bl_idname, text="Execute")

    def execute(self):
        try:

            input_dir = self.input_path
            output_dir = self.output_path
            chain_command = self.get_input_value("in")

            if self.separate_thread:
                thread = threading.Thread(target=run_gmic_batch, args=(input_dir, output_dir, chain_command))
                thread.start()

            else:
                if not run_gmic_batch(input_dir, output_dir, chain_command):
                    raise Exception("Failed to execute GMIC commands")

            return self.separate_thread and "Batch process started" or "Batch processed"
    
        except Exception as e:
            print(e)
            return e

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

    def draw_buttons(self, context, layout):
        layout.prop(self, "name")
        layout.prop(self, "image")
        layout.prop(self, "downscale")
        layout.operator(OP_ExecuteRenderLayer.bl_idname, text="Render Layers")

    def execute(self):
        try:

            input_path = save_image(image=self.image, name=self.name)
            if not input_path:
                raise Exception("Failed to save image")

            temp_command = self.downscale and "-resize 40%,40%" or ""

            return f"{input_path} {temp_command}"
        
        except:
            return "NULL_IMAGE"

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
        
        string_cmd = re.findall("\\\".*?\\\"", temp_cmd)
        string_cmd_index = 0
        string_cmd_map = {}

        for cmd in string_cmd:
            temp_cmd = temp_cmd.replace(cmd, f"@str{string_cmd_index}")
            string_cmd_map[string_cmd_index] = cmd
            string_cmd_index += 1

        all_cmd = temp_cmd.split("-")
        if len(all_cmd) < 2:
            return temp_cmd

        last_cmd = all_cmd[-1]

        last_cmd_name = last_cmd.split(" ")[0]
        last_cmd_value = last_cmd.replace(last_cmd_name, "")

        last_cmd_new = last_cmd_name + self.create_command() + last_cmd_value

        temp_cmd = temp_cmd.replace(last_cmd, last_cmd_new)

        string_cmd_index = 0
        for cmd in string_cmd_map:
            temp_cmd = temp_cmd.replace(f"@str{string_cmd_index}", string_cmd_map[cmd])
            string_cmd_index += 1

        return temp_cmd

node_classes = [
    IO_Output,
    IO_OutputBatch,
    IO_Input,
    IO_AppendIndex,
]