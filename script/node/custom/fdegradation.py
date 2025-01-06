from bpy.props import ( BoolProperty, FloatProperty, EnumProperty, IntProperty, StringProperty, FloatVectorProperty )

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

class FDegrade_Blend(GMICBaseNode):
    """Blend"""

    bl_idname = "GMIC_FDegrade_Blend"
    bl_label = "Blend"
    bl_width_default = 165

    node_props = ["ratio", "blend_type"]
    
    ratio: FloatProperty(name="Ratio", default=0.5, min=0.0, max=1.0) # type: ignore
    blend_type: EnumProperty(
        name="Blend Type",
        items=[
            ("multiply", "Multiply", "Multiply the two images"),
            ("overlay", "Overlay", "Combine images using overlay mode"),
            ("add", "Addition", "Add the pixel values of the two images"),
            ("subtract", "Subtract", "Subtract the second image from the first"),
            ("screen", "Screen", "Blend images using screen mode"),
            ("difference", "Difference", "Calculate the absolute difference"),
            ("softlight", "Soft Light", "Apply soft light blending"),
            ("hardlight", "Hard Light", "Apply hard light blending"),
        ],
        default="multiply"
    ) # type: ignore

    def init(self, context):
        super().init(context)
        self.inputs.new("NodeSocketString", "Image")
        self.inputs["Image"].hide_value = True

    def create_command(self):
        image = self.get_input_value("Image")
        blend_mode = self.blend_type
        blend_ratio = self.ratio
        return f"{image} -blend {blend_mode},{blend_ratio}"
    
    def finalize_command(self):
        temp_cmd = self.get_input_value("in")
        temp_cmd += " " + self.create_command()
        return temp_cmd


class FDegrade_Fill(GMICBaseNode):
    """Fill"""

    bl_idname = "GMIC_FDegrade_Fill"
    bl_label = "Fill"
    bl_width_default = 165

    node_props = ["color", "alpha", "index"]
    
    color: FloatVectorProperty(
        name="Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    alpha: FloatProperty(
        name="Alpha",
        default=1.0,
        min=0.0, 
        max=1.0,
    ) # type: ignore

    def create_command(self):
        return f"fill_color {self.color[0]*255},{self.color[1]*255},{self.color[2]*255},{self.alpha*255}"


node_classes = [
    FDegrade_Blur,
    FDegrade_Resize,
    FDegrade_ResizePercentage,
    FDegrade_Blend,
    FDegrade_Fill
]