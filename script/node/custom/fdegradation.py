from bpy.props import ( BoolProperty, FloatProperty, EnumProperty, IntProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum

class FDegrade_Blur(GMICBaseNode):
    """Blur"""

    bl_idname = "GMIC_FDegrade_Blur"
    bl_label = "Blur"
    bl_width_default = 150

    node_props = ["amount"]

    amount: FloatProperty(name="Amount", default=1.0, min=0.0, max=100.0) # type: ignore

    def create_command(self):
        return "blur {0}".format(self.amount)

class FDegrade_Resize(GMICBaseNode):
    """Resize"""

    bl_idname = "GMIC_FDegrade_Resize"
    bl_label = "Resize"
    bl_width_default = 165

    node_props = ["width", "height"]

    width: IntProperty(name="Width", default=512, min=1) # type: ignore
    height: IntProperty(name="Height", default=512, min=1) # type: ignore

    def create_command(self):
        return "resize {0},{1}".format(
            self.width,
            self.height
        )
    
class FDegrade_ResizePercentage(GMICBaseNode):
    """Resize Percentage"""

    bl_idname = "GMIC_FDegrade_ResizePercentage"
    bl_label = "Resize Percentage"
    bl_width_default = 165

    node_props = ["amount"]

    amount: FloatProperty(name="Amount", default=50.0, min=10.0, max=100.0) # type: ignore

    def create_command(self):
        return "resize {0}%,{1}%".format(
            self.amount,
            self.amount
        )


node_classes = [
    FDegrade_Blur,
    FDegrade_Resize,
    FDegrade_ResizePercentage
]