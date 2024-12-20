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

    def execute(self):
        node_command = "-blur {0}".format(self.amount)
        return self.create_command(node_command)
    
classes = [
    FDegrade_Blur
]