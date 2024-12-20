from ..base.node import GMICBaseNode, create_enum
from nodeitems_utils import NodeItem
from bpy.props import ( BoolProperty, FloatProperty, EnumProperty )

class FAT_ArrayMirrored(GMICBaseNode):
    """Filter Array Mirrored Node"""
    bl_idname = "GMIC_FAT_ArrayMirrored"
    bl_label = "Array Mirrored"
    bl_icon = "NODE"
    
    node_props = ["iteration", "xOffset", "yOffset", "arrayMode", "initilization", "crop"]

    iteration: FloatProperty(name="Iteration",default=1.0, min=0.0, max=10.0) # type: ignore
    xOffset: FloatProperty(name="X Offset", default=0.0, min=0.0, max=100.0) # type: ignore
    yOffset: FloatProperty(name= "Y Offset",default=0.0, min=0.0, max=100.0) # type: ignore
    arrayMode: EnumProperty(
        name="Array Mode",
        items=create_enum(["X", "Y", "XY", "2XY"]),
        default="2"
    ) # type: ignore
    initilization: EnumProperty(
        name="Initilization",
        items=create_enum(["Original", "Mirror X", "Mirror Y", "Rotate 90", "Rotate 180", "Rotate 270"]),
        default="0"
    ) # type: ignore
    crop: FloatProperty(default=0.0, min=0.0, max=100.0) # type: ignore

    def execute(self):
        node_command = "-fx_array_mirror {0},{1},{2},{3},{4},{5},{6}".format(
            self.iteration,
            self.xOffset,
            self.yOffset,
            int(self.arrayMode),
            int(self.initilization),
            0,
            self.crop
        )
        return self.create_command(node_command)



classes = [
    FAT_ArrayMirrored
]