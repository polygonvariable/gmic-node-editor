import bpy
from bpy.props import ( BoolProperty, FloatProperty, EnumProperty, StringProperty, IntProperty, PointerProperty, FloatVectorProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum

class SCRIPT_CustomCode(GMICBaseNode):
    """Custom Code"""

    bl_idname = "GMIC_SCRIPT_CustomCode"
    bl_label = "Custom Code"

    node_props = ["code"]
    
    code: StringProperty(
        name="Code",
        default="",
    ) # type: ignore

    def create_command(self):
        return f"fx_custom_code \\\"{self.code}\\\",0,0,0,2,0,50,50"

class SCRIPT_BackgroundColor(GMICBaseNode):
    """Alpha Background Color"""

    bl_idname = "GMIC_SCRIPT_BackgroundColor"
    bl_label = "Background Color"

    node_props = ["color"]
    
    color: FloatVectorProperty(
        name="Color",
        default=(0.0,0.0,0.0),
        min=0.0,
        max=1.0,
        subtype="COLOR"
    ) # type: ignore
    alpha: FloatProperty(
        name="Alpha",
        default=1.0,
        min=0.0,
        max=1.0
    ) # type: ignore

    def create_command(self):

        color = self.color
        code = f"+to_rgba -fill_color[0] {color[0]*255},{color[1]*255},{color[2]*255},{self.alpha*255} +channels[-1] 100% +image[0] [1],0%,0%,0,0,1,[2],255 -rm[0] -rm[0] -rm[0]"
        return "fx_custom_code \\\"foreach { " + code + " }\\\",0,0,0,2,0,50,50"
    

node_classes = [
    SCRIPT_CustomCode,
    SCRIPT_BackgroundColor
]