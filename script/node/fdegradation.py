from nodeitems_utils import NodeItem
from bpy.props import ( BoolProperty, FloatProperty, EnumProperty )

from ..base.node import GMICBaseNode, create_enum

class FDegrade_Blur(GMICBaseNode):
    """Blur"""

    bl_idname = "GMIC_FDegrade_Blur"
    bl_label = "Blur"

    node_props = ["amount"]

    amount: FloatProperty(name="Amount", default=1.0, min=0.0, max=100.0) # type: ignore

    def create_command(self):
        return "blur {0}".format(self.amount)

classes = [
    FDegrade_Blur
]