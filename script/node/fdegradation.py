from ..base.node import GMICBaseNode
from bpy.props import ( BoolProperty, FloatProperty, EnumProperty )

class FBlur(GMICBaseNode):
    """Filter Blur Node"""
    bl_idname = "GMIC_FBlurNode"
    bl_label = "Blur"
    bl_icon = "NODE"

    amount: FloatProperty(default=1.0, min=0.0, max=100.0)

    def init(self, context):
        self.default_in()
        self.default_out()

    def draw_buttons(self, context, layout):
        layout.prop(self, "amount", text="Amount")

    def execute(self):
        return self.create_command("-blur 10")
    
classes = [FBlur]