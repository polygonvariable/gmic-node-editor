import os
import tempfile

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
    image: PointerProperty(name="Target", type=bpy.types.Image) # type: ignore
    downscale: BoolProperty(name="Downscale", default=True) # type: ignore

    def init(self, context):
        self.default_in()

    def draw_buttons(self, context, layout):
        layout.prop(self, "name")
        layout.prop(self, "image")
        layout.prop(self, "downscale")
        layout.operator(OP_ExecuteRunGMIC.bl_idname, text="Execute")
        layout.operator(OP_ExecuteRenderLayer.bl_idname, text="Render Layers")

    def execute(self):
        try:

            temp_name = self.name
            temp_image = self.image
            temp_command = self.get_input_value("in")

            if not save_image(image=temp_image, name=temp_name):
                raise Exception("Failed to save image")

            if not run_gmic(command=temp_command, name=temp_name, downscale=self.downscale):
                raise Exception("Failed to execute GMIC command")

            return True

        except:
            print("Failed to execute Output Node")
            return False


node_classes = [
    IO_Output
]