from ..base.node import GMICBaseNode
from bpy.props import ( BoolProperty, FloatProperty, EnumProperty )

class FArrayMirrored(GMICBaseNode):
    """Filter Array Mirrored Node"""
    bl_idname = "GMIC_FArrayMirroredNode"
    bl_label = "Array Mirrored"
    bl_icon = "NODE"
    
    iteration: FloatProperty(default=1.0, min=0.0, max=10.0)
    xOffset: FloatProperty(default=0.0, min=0.0, max=100.0)
    yOffset: FloatProperty(default=0.0, min=0.0, max=100.0)
    crop: FloatProperty(default=0.0, min=0.0, max=100.0)

    def init(self, context):
        self.default_in()
        self.default_out()

    def draw_buttons(self, context, layout):
        layout.prop(self, "iteration", text="Iteration")
        layout.prop(self, "xOffset", text="X Offset")
        layout.prop(self, "yOffset", text="Y Offset")
        layout.prop(self, "crop", text="Crop")

    def execute(self):
        return self.create_command("-fx_array_mirror 1,0,0,2,0,0,0")
    
classes = [FArrayMirrored]