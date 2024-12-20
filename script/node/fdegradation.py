from ..base.node import GMICBaseNode
from nodeitems_utils import NodeItem
from bpy.props import ( BoolProperty, FloatProperty, EnumProperty )

class FDegrade_Blur(GMICBaseNode):
    """Filter Blur Node"""
    bl_idname = "GMIC_FDegrade_Blur"
    bl_label = "Blur"
    bl_icon = "NODE"

    node_props = ["amount"]

    amount: FloatProperty(name="Amount", default=1.0, min=0.0, max=100.0) # type: ignore

    def create_command(self):
        return "blur {0}".format(self.amount)

classes = [
    FDegrade_Blur
]