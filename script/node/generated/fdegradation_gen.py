from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FDegrade_addgrain(GMICBaseNode):
    """Add Grain by Author: David Tschumperlé. Latest Update: 2016/02/08."""
    # fx_simulate_grain

    bl_idname = "FDegrade_addgrain"
    bl_label = "Add Grain"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop13", "var_prop14"]

    var_prop0: EnumProperty(
        name="Preset",
        default="0",
        items=create_enum(["Orwo NP20-GDR", "Kodak TMAX 400", "Kodak TMAX 3200", "Kodak TRI-X 1600", "Unknown"]),
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Blend Mode",
        default="1",
        items=create_enum(["Alpha", "Grain Merge", "Hard Light", "Overlay", "Soft Light", "Grain Only"]),
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Opacity",
        default=0.2,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Scale",
        default=100.0,
        min=30.0, 
        max=800.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Sharpness",
        default=0.0,
        min=0.0, 
        max=512.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Colored Grain",
        default=0,
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Gamma (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Hue (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Saturation (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore
    var_prop14: BoolProperty(
        name="Preview Grain Alone",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_simulate_grain {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop13},{int(self.var_prop14)}"

################################################################################
################################################################################

class GMIC_FDegrade_blurangular(GMICBaseNode):
    """Blur [Angular] by Author: David Tschumperlé. Latest Update: 2015/16/01."""
    # fx_blur_angular

    bl_idname = "FDegrade_blurangular"
    bl_label = "Blur [Angular]"

    node_props = ["var_prop0", "var_prop1_x", "var_prop1_y", "var_prop2", "var_prop3", "var_prop5", "var_prop6"]

    var_prop0: FloatProperty(
        name="Amplitude (%)",
        default=2.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Sharpness",
        default=0.0,
        min=0.0, 
        max=500.0, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Preview Guides",
        default=1,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="7",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_blur_angular {self.var_prop0},{self.var_prop1_x},{self.var_prop1_y},{self.var_prop2},{int(self.var_prop3)},{self.var_prop5},{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FDegrade_blurbloom(GMICBaseNode):
    """Blur [Bloom] by Author: David Tschumperlé. Latest Update: 2015/03/02."""
    # fx_blur_bloom

    bl_idname = "FDegrade_blurbloom"
    bl_label = "Blur [Bloom]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop10", "var_prop12"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Ratio",
        default=2.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Iterations",
        default=5,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Operator",
        default="0",
        items=create_enum(["Add", "Max", "Min"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Kernel",
        default="1",
        items=create_enum(["Deriche", "Gaussian", "Box", "Triangle", "Quadratic"]),
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Normalize Scales",
        default=0,
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Anisotropy",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Angle",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Channel(s)",
        default="7",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_blur_bloom {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{self.var_prop6},{self.var_prop7},{self.var_prop10},{self.var_prop12},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_blurdepthoffield(GMICBaseNode):
    """Blur [Depth-of-Field] by Author: David Tschumperlé. Latest Update: 2014/25/02."""
    # fx_blur_dof

    bl_idname = "FDegrade_blurdepthoffield"
    bl_label = "Blur [Depth-of-Field]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop14"]

    var_prop0: FloatProperty(
        name="Blur Amplitude",
        default=3.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Blur Precision",
        default=16,
        min=2, 
        max=64, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Depth-of-Field Type",
        default="0",
        items=create_enum(["Gaussian", "User-Defined (Bottom Layer)"]),
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Invert Blur",
        default=0,
    ) # type: ignore
    var_prop7: FloatProperty(
        name="First Radius",
        default=30.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Second Radius",
        default=30.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Sharpness",
        default=1.0,
        min=0.0, 
        max=8.0, 
    ) # type: ignore
    var_prop11: BoolProperty(
        name="Preview Guides",
        default=1,
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Gamma",
        default=0.0,
        min=-2.0, 
        max=2.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_blur_dof {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},50,50,{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{int(self.var_prop11)},{self.var_prop14}"

################################################################################
################################################################################

class GMIC_FDegrade_blurgaussian(GMICBaseNode):
    """Blur [Gaussian] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_gaussian_blur

    bl_idname = "FDegrade_blurgaussian"
    bl_label = "Blur [Gaussian]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="XY-Amplitude",
        default=3.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="X-Amplitude",
        default=0.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Y-Amplitude",
        default=0.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Boundary",
        default="1",
        items=create_enum(["Black", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_gaussian_blur {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop6},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_blurglow(GMICBaseNode):
    """Blur [Glow] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_glow

    bl_idname = "FDegrade_blurglow"
    bl_label = "Blur [Glow]"

    node_props = ["var_prop0", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=6.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Channel(s)",
        default="7",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_glow {self.var_prop0},{self.var_prop2},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_blurlinear(GMICBaseNode):
    """Blur [Linear] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_blur_linear

    bl_idname = "FDegrade_blurlinear"
    bl_label = "Blur [Linear]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop7", "var_prop9"]

    var_prop0: FloatProperty(
        name="Tangent Radius (%)",
        default=10.0,
        min=0.0, 
        max=25.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Orthogonal Radius (%)",
        default=0.5,
        min=0.0, 
        max=25.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Sharpness",
        default=0.0,
        min=0.0, 
        max=500.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Boundary",
        default="1",
        items=create_enum(["Black", "Nearest"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channel(s)",
        default="7",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_blur_linear {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},{self.var_prop7},{self.var_prop9},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_blurmultidirectional(GMICBaseNode):
    """Blur [Multidirectional] by Author: David Tschumperlé. Latest Update: 2020/09/11."""
    # fx_blur_multidirectional

    bl_idname = "FDegrade_blurmultidirectional"
    bl_label = "Blur [Multidirectional]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop11", "var_prop13"]

    var_prop0: IntProperty(
        name="Number of Orientations",
        default=5,
        min=1, 
        max=16, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Reference Angle (deg.)",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Angle Range (deg.)",
        default=360.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness",
        default=150.0,
        min=0.0, 
        max=1024.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Kernel type",
        default="0",
        items=create_enum(["Mono-Directional", "Bi-Directional"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Boundary conditions",
        default="1",
        items=create_enum(["Dirichlet", "Neumann", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Sharpness",
        default=0.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Blend Mode",
        default="2",
        items=create_enum(["Min", "Max", "Average", "Edges-0.5 (beware: memory-consuming!)", "Edges-1 (beware: memory-consuming!)", "Edges-2 (beware: memory-consuming!)", "Median (beware: memory-consuming!)"]),
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Boost Contrast",
        default=2.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Channel(s)",
        default="7",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_blur_multidirectional {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop11},{self.var_prop13},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_blurradial(GMICBaseNode):
    """Blur [Radial] by Author: David Tschumperlé. Latest Update: 2015/16/01."""
    # fx_blur_radial

    bl_idname = "FDegrade_blurradial"
    bl_label = "Blur [Radial]"

    node_props = ["var_prop0", "var_prop1_x", "var_prop1_y", "var_prop2", "var_prop3", "var_prop5", "var_prop6"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=3.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Sharpness",
        default=0.0,
        min=0.0, 
        max=500.0, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Preview Guides",
        default=1,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="7",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_blur_radial {self.var_prop0},{self.var_prop1_x},{self.var_prop1_y},{self.var_prop2},{int(self.var_prop3)},{self.var_prop5},{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FDegrade_blursplinter(GMICBaseNode):
    """Blur [Splinter] by Author: Reptorian. Latest Update: 2020/9/10."""
    # fx_rep_blur_splinter

    bl_idname = "FDegrade_blursplinter"
    bl_label = "Blur [Splinter]"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop11"]

    var_prop2: FloatProperty(
        name="Half Image-Diagonal(%)",
        default=20.0,
        min=0.1, 
        max=100.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Duplicates",
        default=3,
        min=3, 
        max=100, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Angle",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Thickness(%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Contrast(%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Balance(%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["None", "Neumann", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop9: BoolProperty(
        name="Use Bi-sided Convolution?",
        default=0,
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_rep_blur_splinter {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{int(self.var_prop9)},{self.var_prop11},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_chromaticaberrations(GMICBaseNode):
    """Chromatic Aberrations by Author: David Tschumperlé. Latest Update: 2021/08/10."""
    # fx_chromatic_aberrations

    bl_idname = "FDegrade_chromaticaberrations"
    bl_label = "Chromatic Aberrations"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop16"]

    var_prop0: FloatVectorProperty(
        name="Primary Color",
        default=(1.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Deformation Type",
        default="0",
        items=create_enum(["Shift", "Radial", "Angular", "Random"]),
    ) # type: ignore
    var_prop2: FloatProperty(
        name="X-Amplitude",
        default=2.0,
        min=-32.0, 
        max=32.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Y-Amplitude",
        default=2.0,
        min=-32.0, 
        max=32.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Attenuation Near Center (%)",
        default=50.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Attenuation Decay",
        default=1.0,
        min=0.0, 
        max=8.0, 
    ) # type: ignore
    var_prop8: FloatVectorProperty(
        name="Secondary Color",
        default=(0.0,1.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Deformation Type",
        default="0",
        items=create_enum(["Shift", "Radial", "Angular", "Random"]),
    ) # type: ignore
    var_prop10: FloatProperty(
        name="X-Amplitude",
        default=0.0,
        min=-32.0, 
        max=32.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Y-Amplitude",
        default=0.0,
        min=-32.0, 
        max=32.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Attenuation Near Center (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Attenuation Decay",
        default=1.0,
        min=0.0, 
        max=8.0, 
    ) # type: ignore
    var_prop16: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_chromatic_aberrations {self.var_prop0[0]*255},{self.var_prop0[1]*255},{self.var_prop0[2]*255},255,{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8[0]*255},{self.var_prop8[1]*255},{self.var_prop8[2]*255},255,{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop16},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_crtsubpixels(GMICBaseNode):
    """CRT Sub-Pixels by Author : Garagecoder. Latest update : 2014/12/11."""
    # fx_gcd_crt

    bl_idname = "FDegrade_crtsubpixels"
    bl_label = "CRT Sub-Pixels"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop5"]

    var_prop2: FloatProperty(
        name="Horizontal Blur",
        default=1.8,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Vertical Blur",
        default=1.8,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Screen Border",
        default=0,
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Equalize",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_gcd_crt {self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{int(self.var_prop5)}"

################################################################################
################################################################################

class GMIC_FDegrade_dirty(GMICBaseNode):
    """Dirty by Author: David Tschumperlé. Latest Update: 2014/24/11."""
    # fx_dirty

    bl_idname = "FDegrade_dirty"
    bl_label = "Dirty"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: BoolProperty(
        name="Monochrome",
        default=1,
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_dirty {self.var_prop0},{int(self.var_prop1)},{self.var_prop3},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_fliprotateblocks(GMICBaseNode):
    """Flip & Rotate Blocks by Author: David Tschumperlé. Latest Update: 2016/01/09."""
    # fx_flip_blocks

    bl_idname = "FDegrade_fliprotateblocks"
    bl_label = "Flip & Rotate Blocks"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop7"]

    var_prop0: IntProperty(
        name="X-Size (px)",
        default=4,
        min=1, 
        max=128, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Y-Size (px)",
        default=4,
        min=1, 
        max=128, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Flip",
        default="3",
        items=create_enum(["None", "X-axis", "Y-axis", "XY-axes"]),
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Rotate",
        default="1",
        items=create_enum(["-90 deg.", "0 deg.", "90 deg."]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_flip_blocks {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_fragmentblur(GMICBaseNode):
    """Fragment Blur by Author : Reptorian Latest update: 2019/9/26."""
    # gui_rep_frblur

    bl_idname = "FDegrade_fragmentblur"
    bl_label = "Fragment Blur"

    node_props = ["var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop10", "var_prop11", "var_prop13"]

    var_prop3: EnumProperty(
        name="Color Space",
        default="0",
        items=create_enum(["RGB", "sRGB", "RYB", "CMYK", "HCY", "HSI", "HSL", "HSV", "LAB", "LCH"]),
    ) # type: ignore
    var_prop4: IntProperty(
        name="Additional Duplicates Count",
        default=10,
        min=2, 
        max=100, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Half Image-Diagonal (%)",
        default=5.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Angle",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Superimpose with Original?",
        default=0,
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Boundary",
        default="1",
        items=create_enum(["None", "Neumann", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop11: BoolProperty(
        name="Shift Linear Interpolation?",
        default=0,
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"gui_rep_frblur {self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{int(self.var_prop7)},{self.var_prop10},{int(self.var_prop11)},{self.var_prop13},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_huffmanglitches(GMICBaseNode):
    """Huffman Glitches by Author: David Tschumperlé. Latest Update: 2023/04/26."""
    # fx_huffman_glitches

    bl_idname = "FDegrade_huffmanglitches"
    bl_label = "Huffman Glitches"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop8", "var_prop10"]

    var_prop0: FloatProperty(
        name="Noise Level (%)",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Split Mode",
        default="0",
        items=create_enum(["None", "Horizontal Blocs", "Vertical Blocs", "Patches"]),
    ) # type: ignore
    var_prop2: IntProperty(
        name="Bloc Size (%)",
        default=25,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Patch Overlap (%)",
        default=0.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Color Space",
        default="0",
        items=create_enum(["RGB", "CMYK", "HCY", "HSI", "HSL", "HSV", "Jzazbz", "Lab", "Lch", "OKLab", "YCbCr", "YIQ"]),
    ) # type: ignore
    var_prop5: IntProperty(
        name="Quantization",
        default=0,
        min=0, 
        max=64, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Random Seed",
        default=0,
        min=0, 
        max=65536, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_huffman_glitches {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop8},{self.var_prop10},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_jpegartefacts(GMICBaseNode):
    """JPEG Artefacts by Author: David Tschumperlé. Latest Update: 2024/02/21."""
    # fx_jpeg_artefacts

    bl_idname = "FDegrade_jpegartefacts"
    bl_label = "JPEG Artefacts"

    node_props = ["var_prop1", "var_prop3"]

    var_prop1: IntProperty(
        name="Quality (%)",
        default=50,
        min=1, 
        max=100, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_jpeg_artefacts {self.var_prop1},{self.var_prop3},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_lomo(GMICBaseNode):
    """Lomo by Authors: Jérome Boulanger and David Tschumperlé. Latest Update: 2012/06/06."""
    # fx_lomo

    bl_idname = "FDegrade_lomo"
    bl_label = "Lomo"

    node_props = ["var_prop0", "var_prop2"]

    var_prop0: FloatProperty(
        name="Vignette Size",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_lomo {self.var_prop0},{self.var_prop2},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_messwithbits(GMICBaseNode):
    """Mess with Bits by Author: David Tschumperlé. Latest Update: 2019/01/16."""
    # fx_mess_with_bits

    bl_idname = "FDegrade_messwithbits"
    bl_label = "Mess with Bits"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop11", "var_prop13"]

    var_prop1: BoolProperty(
        name="Pre-Normalize",
        default=1,
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness (%)",
        default=15.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Multiplier",
        default=1,
        min=1, 
        max=256, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Reversing",
        default="1",
        items=create_enum(["None", "Reverse bits", "Reverse bytes"]),
    ) # type: ignore
    var_prop7: IntProperty(
        name="Bit Masking (Start)",
        default=0,
        min=0, 
        max=15, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Bit Masking (End)",
        default=15,
        min=0, 
        max=15, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Opacity (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_mess_with_bits {int(self.var_prop1)},{self.var_prop2},{self.var_prop3},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop11},{self.var_prop13},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_noiseadditive(GMICBaseNode):
    """Noise [Additive] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_noise

    bl_idname = "FDegrade_noiseadditive"
    bl_label = "Noise [Additive]"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=10.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Noise Type",
        default="0",
        items=create_enum(["Gaussian", "Uniform", "Salt and Pepper", "Poisson"]),
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Value Action",
        default="1",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_noise {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_noiseperlin(GMICBaseNode):
    """Noise [Perlin] by Author: David Tschumperlé. Latest Update: 2019/01/24."""
    # fx_noise_perlin

    bl_idname = "FDegrade_noiseperlin"
    bl_label = "Noise [Perlin]"

    node_props = ["var_prop0", "var_prop3", "var_prop4", "var_prop5", "var_prop8", "var_prop9", "var_prop10", "var_prop13", "var_prop14", "var_prop15", "var_prop18", "var_prop19", "var_prop20", "var_prop22", "var_prop24"]

    var_prop0: IntProperty(
        name="Random Seed",
        default=0,
        min=0, 
        max=65536, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Amplitude",
        default=100.0,
        min=0.0, 
        max=512.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Scale (%)",
        default=8.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="X/Y-Ratio",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Amplitude",
        default=0.0,
        min=0.0, 
        max=512.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Scale (%)",
        default=4.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="X/Y-Ratio",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Amplitude",
        default=0.0,
        min=0.0, 
        max=512.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Scale (%)",
        default=2.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="X/Y-Ratio",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Amplitude",
        default=0.0,
        min=0.0, 
        max=512.0, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Scale (%)",
        default=1.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop20: FloatProperty(
        name="X/Y-Ratio",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop22: EnumProperty(
        name="Channel(s)",
        default="2",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]"]),
    ) # type: ignore
    var_prop24: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_noise_perlin {self.var_prop0},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop18},{self.var_prop19},{self.var_prop20},{self.var_prop22},{self.var_prop24},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_noisespread(GMICBaseNode):
    """Noise [Spread] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_spread

    bl_idname = "FDegrade_noisespread"
    bl_label = "Noise [Spread]"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="X-Variations",
        default=4.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Y-Variations",
        default=4.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_spread {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_oldmoviestripes(GMICBaseNode):
    """Old-Movie Stripes by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_stripes_y

    bl_idname = "FDegrade_oldmoviestripes"
    bl_label = "Old-Movie Stripes"

    node_props = ["var_prop0", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Frequency",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_stripes_y {self.var_prop0},{self.var_prop2},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_oldschool8bits(GMICBaseNode):
    """Oldschool 8bits by Author: David Tschumperlé. Latest Update: 2011/02/11."""
    # fx_8bits

    bl_idname = "FDegrade_oldschool8bits"
    bl_label = "Oldschool 8bits"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: FloatProperty(
        name="Scale",
        default=25.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Dithering",
        default=800.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Levels",
        default=16,
        min=2, 
        max=256, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_8bits {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_pixelsort(GMICBaseNode):
    """Pixel Sort by Author: David Tschumperlé. Latest Update: 2021/10/29."""
    # fx_pixelsort

    bl_idname = "FDegrade_pixelsort"
    bl_label = "Pixel Sort"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11"]

    var_prop1: EnumProperty(
        name="Order",
        default="1",
        items=create_enum(["Decreasing", "Increasing"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Axis",
        default="0",
        items=create_enum(["X-axis", "Y-axis", "X-axis Then Y-axis", "Y-axis Then X-axis"]),
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Sorting Criterion",
        default="0",
        items=create_enum(["Red", "Green", "Blue", "Intensity", "Luminance", "Lightness", "Hue", "Saturation", "Minimum", "Maximum", "Random"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Mask By",
        default="1",
        items=create_enum(["Bottom Layer", "Criterion", "Contours", "Random"]),
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Lower Mask Threshold (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Higher Mask Threshold (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Mask Smoothness (%)",
        default=0.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop10: BoolProperty(
        name="Invert Mask",
        default=0,
    ) # type: ignore
    var_prop11: BoolProperty(
        name="Preview Mask",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_pixelsort {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{int(self.var_prop10)},{int(self.var_prop11)}"

################################################################################
################################################################################

class GMIC_FDegrade_rainsnow(GMICBaseNode):
    """Rain & Snow by Author: David Tschumperlé. Latest Update: 2024/02/21."""
    # fx_rain

    bl_idname = "FDegrade_rainsnow"
    bl_label = "Rain & Snow"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Angle",
        default=65.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Speed",
        default=10.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Density (%)",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Radius",
        default=0.1,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Gamma",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Opacity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_rain {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_randomshadestripes(GMICBaseNode):
    """Random Shade Stripes by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_shade_stripes

    bl_idname = "FDegrade_randomshadestripes"
    bl_label = "Random Shade Stripes"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="Frequency",
        default=30.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Orientation",
        default="1",
        items=create_enum(["Horizontal", "Vertical"]),
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Darkness",
        default=0.8,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Lightness",
        default=1.3,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_shade_stripes {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop6},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_rebuildfromsimilarblocks(GMICBaseNode):
    """Rebuild From Similar Blocks by Author: David Tschumperlé. Latest Update: 2020/09/17."""
    # fx_rebuild_from_similar_blocks

    bl_idname = "FDegrade_rebuildfromsimilarblocks"
    bl_label = "Rebuild From Similar Blocks"

    node_props = ["var_prop0", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: FloatProperty(
        name="Block Size (%)",
        default=5.0,
        min=2.0, 
        max=50.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Regularization factor",
        default=10.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Luminance factor",
        default=0.75,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Norm type",
        default="1",
        items=create_enum(["L1", "L2"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_rebuild_from_similar_blocks {self.var_prop0},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FDegrade_scanlines(GMICBaseNode):
    """Scanlines by Author: David Tschumperlé. Latest Update: 2014/19/11."""
    # fx_scanlines

    bl_idname = "FDegrade_scanlines"
    bl_label = "Scanlines"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop7", "var_prop9"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=60.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Bandwidth",
        default=2.0,
        min=1.0, 
        max=300.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Shape",
        default="0",
        items=create_enum(["Block", "Triangle", "Sine", "Sine+", "Random"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Offset",
        default=0.0,
        min=0.0, 
        max=500.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_scanlines {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},{self.var_prop7},{self.var_prop9},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_selfglitching(GMICBaseNode):
    """Self Glitching by Author: David Tschumperlé. Latest Update: 2018/08/19."""
    # fx_self_glitching

    bl_idname = "FDegrade_selfglitching"
    bl_label = "Self Glitching"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4_x", "var_prop4_y", "var_prop5", "var_prop7", "var_prop9"]

    var_prop0: FloatProperty(
        name="Multiplier",
        default=0.0,
        min=-5.0, 
        max=5.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Bias",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Negate",
        default=0,
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Operator",
        default="0",
        items=create_enum(["Add", "Mul", "And", "Or", "Xor", "Pow", "Reverse Pow", "Mod", "Reverse Mod"]),
    ) # type: ignore
    var_prop4_x: FloatProperty(
        name="Shift Point X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4_y: FloatProperty(
        name="Shift Point Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Zero", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_self_glitching {self.var_prop0},{self.var_prop1},{int(self.var_prop2)},{self.var_prop3},{self.var_prop4_x},{self.var_prop4_y},{self.var_prop5},{self.var_prop7},{self.var_prop9},50,50"

################################################################################
################################################################################

class GMIC_FDegrade_streak(GMICBaseNode):
    """Streak by Author: David Tschumperlé. Latest Update: 2017/12/22."""
    # fx_streak

    bl_idname = "FDegrade_streak"
    bl_label = "Streak"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3"]

    var_prop0: FloatVectorProperty(
        name="Mask Color",
        default=(1.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Step (%)",
        default=0.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Propagation",
        default="3",
        items=create_enum(["Backward", "Forward", "Bidirectional [Sharp]", "Bidirectional [Smooth]"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_streak {self.var_prop0[0]*255},{self.var_prop0[1]*255},{self.var_prop0[2]*255},255,{self.var_prop1},{self.var_prop2},{self.var_prop3}"

################################################################################
################################################################################

class GMIC_FDegrade_visiblewatermark(GMICBaseNode):
    """Visible Watermark by Author: David Tschumperlé. Latest Update: 2023/09/16."""
    # fx_watermark_visible

    bl_idname = "FDegrade_visiblewatermark"
    bl_label = "Visible Watermark"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7"]

    var_prop0: StringProperty(
        name="Text",
        default="\251 G&#x27;MIC",
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Opacity",
        default=0.4,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Font",
        default="27",
        items=create_enum(["Acme", "Arial", "Arial Black", "Black Ops One", "Black Chancery", "Cabin Sketch", "Caprasimo", "Carnevalee Freakshow", "Cheese Burger", "Cheque", "Cheque Black", "Chlorinar", "Comic Sans MS", "Courier New", "Creepster", "Georgia", "Hidayatullah", "Impact", "Jaro", "Lobster", "Luckiest Guy", "Macondo", "Medieval Sharp", "Odin Rounded", "Oswald", "Palatino Linotype", "Playfair Display", "Roboto", "Satisfy", "Sofia", "Sunday Milk", "Tex Gyre Adventor", "Times New Roman", "Titan One", "Typewriter", "Verdana"]),
    ) # type: ignore
    var_prop3: IntProperty(
        name="Size",
        default=50,
        min=13, 
        max=512, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Bold Face",
        default=0,
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Angle",
        default=25.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Lightness",
        default="1",
        items=create_enum(["Darker", "Brighter"]),
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_watermark_visible \\\"{self.var_prop0}\\\",{self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop5},{self.var_prop6},{self.var_prop7}"

################################################################################
################################################################################

class GMIC_FDegrade_warpbyintensity(GMICBaseNode):
    """Warp by Intensity by Author: David Tschumperlé. Latest Update: 2016/02/09."""
    # fx_warp_by_intensity

    bl_idname = "FDegrade_warpbyintensity"
    bl_label = "Warp by Intensity"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop6", "var_prop7", "var_prop8", "var_prop10", "var_prop12"]

    var_prop0: FloatProperty(
        name="X-Factor",
        default=0.04,
        min=-6.0, 
        max=6.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Y-Factor",
        default=0.04,
        min=-6.0, 
        max=6.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="X-Offset",
        default=128.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Y-Offset",
        default=128.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Correlated Channels",
        default=0,
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Interpolation",
        default="1",
        items=create_enum(["Nearest Neighbor", "Linear"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_warp_by_intensity {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop4},{int(self.var_prop6)},{self.var_prop7},{self.var_prop8},{self.var_prop10},{self.var_prop12},50,50"

################################################################################
################################################################################

node_classes = [
    GMIC_FDegrade_addgrain, GMIC_FDegrade_blurangular, GMIC_FDegrade_blurbloom, GMIC_FDegrade_blurdepthoffield, GMIC_FDegrade_blurgaussian, GMIC_FDegrade_blurglow, GMIC_FDegrade_blurlinear, GMIC_FDegrade_blurmultidirectional, GMIC_FDegrade_blurradial, GMIC_FDegrade_blursplinter, GMIC_FDegrade_chromaticaberrations, GMIC_FDegrade_crtsubpixels, GMIC_FDegrade_dirty, GMIC_FDegrade_fliprotateblocks, GMIC_FDegrade_fragmentblur, GMIC_FDegrade_huffmanglitches, GMIC_FDegrade_jpegartefacts, GMIC_FDegrade_lomo, GMIC_FDegrade_messwithbits, GMIC_FDegrade_noiseadditive, GMIC_FDegrade_noiseperlin, GMIC_FDegrade_noisespread, GMIC_FDegrade_oldmoviestripes, GMIC_FDegrade_oldschool8bits, GMIC_FDegrade_pixelsort, GMIC_FDegrade_rainsnow, GMIC_FDegrade_randomshadestripes, GMIC_FDegrade_rebuildfromsimilarblocks, GMIC_FDegrade_scanlines, GMIC_FDegrade_selfglitching, GMIC_FDegrade_streak, GMIC_FDegrade_visiblewatermark, GMIC_FDegrade_warpbyintensity
]

################################################################################