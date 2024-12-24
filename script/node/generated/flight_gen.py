from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FLight_burn(GMICBaseNode):
    """Burn by Author: David Tschumperlé. Latest Update: 2012/24/11."""
    # fx_burn

    bl_idname = "FLight_burn"
    bl_label = "Burn"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Scale",
        default=30.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_burn {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FLight_contrastswissmask(GMICBaseNode):
    """Contrast Swiss Mask by Author: PhotoComiX. Latest Update: 2011/01/01."""
    # fx_contrast_swm

    bl_idname = "FLight_contrastswissmask"
    bl_label = "Contrast Swiss Mask"

    node_props = ["var_prop1", "var_prop4", "var_prop8"]

    var_prop1: FloatProperty(
        name="Blur the Mask",
        default=2.0,
        min=0.5, 
        max=10.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Skip to Use the Mask to Boost",
        default=0,
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Intensity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_contrast_swm {self.var_prop1},{int(self.var_prop4)},{self.var_prop8}"

################################################################################
################################################################################

class GMIC_FLight_dodgeandburn(GMICBaseNode):
    """Dodge and Burn by Author: Tom Keil. Latest update: 2011/15/02."""
    # fx_dodgeburn

    bl_idname = "FLight_dodgeandburn"
    bl_label = "Dodge and Burn"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop12", "var_prop13", "var_prop14", "var_prop16"]

    var_prop2: FloatProperty(
        name="Highlights Selection",
        default=15.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Highlights Abstraction",
        default=1.5,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Dodge Strength",
        default=25.0,
        min=0.0, 
        max=256.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Dodge Blur",
        default=10.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Shadows Selection",
        default=40.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Shadows Abstraction",
        default=1.5,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Burn Strength",
        default=25.0,
        min=0.0, 
        max=256.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Burn Blur",
        default=10.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop12: BoolProperty(
        name="Keep Layers Separate",
        default=0,
    ) # type: ignore
    var_prop13: BoolProperty(
        name="Keep Original Layer",
        default=0,
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Blur Dodge and Burn Layer",
        default=10.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop16: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_dodgeburn {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{int(self.var_prop12)},{int(self.var_prop13)},{self.var_prop14},{self.var_prop16}"

################################################################################
################################################################################

class GMIC_FLight_dropshadow(GMICBaseNode):
    """Drop Shadow by Author: David Tschumperlé. Latest Update: 2023/09/02."""
    # fx_drop_shadow

    bl_idname = "FLight_dropshadow"
    bl_label = "Drop Shadow"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7"]

    var_prop0: FloatProperty(
        name="X-Offset",
        default=3.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Y-Offset",
        default=3.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=1.8,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="X-Curvature",
        default=0.0,
        min=-2.0, 
        max=2.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Y-curvature",
        default=0.0,
        min=-2.0, 
        max=2.0, 
    ) # type: ignore
    var_prop5: FloatVectorProperty(
        name="Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Expand size",
        default=1,
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Output as separate layers",
        default=1,
    ) # type: ignore

    def create_command(self):
        return f"fx_drop_shadow {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5[0]*255},{self.var_prop5[1]*255},{self.var_prop5[2]*255},255,{int(self.var_prop6)},{int(self.var_prop7)}"

################################################################################
################################################################################

class GMIC_FLight_dropshadow3d(GMICBaseNode):
    """Drop Shadow 3D by Author: David Tschumperlé. Latest Update: 2013/02/07."""
    # fx_drop_shadow3d

    bl_idname = "FLight_dropshadow3d"
    bl_label = "Drop Shadow 3D"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9"]

    var_prop0: FloatProperty(
        name="X-Angle",
        default=0.0,
        min=-90.0, 
        max=90.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Y-Angle",
        default=0.0,
        min=-90.0, 
        max=90.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Z-Angle",
        default=0.0,
        min=-90.0, 
        max=90.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Zoom",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="X-Offset",
        default=1.0,
        min=-50.0, 
        max=50.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Y-Offset",
        default=1.0,
        min=-50.0, 
        max=50.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Perspective",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop8: FloatVectorProperty(
        name="Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop9: BoolProperty(
        name="Preview Only Shadow",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_drop_shadow3d {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8[0]*255},{self.var_prop8[1]*255},{self.var_prop8[2]*255},255,{int(self.var_prop9)}"

################################################################################
################################################################################

class GMIC_FLight_equalizelight(GMICBaseNode):
    """Equalize Light by Author: David Tschumperlé. Latest Update: 2021/03/23."""
    # fx_equalize_light

    bl_idname = "FLight_equalizelight"
    bl_label = "Equalize Light"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: FloatProperty(
        name="Amount (%)",
        default=75.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Mode",
        default="0",
        items=create_enum(["Preserve range", "Preserve covariance"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_equalize_light {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FLight_equalizeshadow(GMICBaseNode):
    """Equalize Shadow by Authors: Francois Grassard and David Tschumperlé. Latest Update: 2021/03/23."""
    # fx_equalize_shadow

    bl_idname = "FLight_equalizeshadow"
    bl_label = "Equalize Shadow"

    node_props = ["var_prop0", "var_prop2"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_equalize_shadow {self.var_prop0},{self.var_prop2},50,50"

################################################################################
################################################################################

class GMIC_FLight_guidedlightrays(GMICBaseNode):
    """Guided Light Rays by Author: David Tschumperlé. Latest Update: 2021/04/06."""
    # fx_guided_lightrays

    bl_idname = "FLight_guidedlightrays"
    bl_label = "Guided Light Rays"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6_x", "var_prop6_y", "var_prop7", "var_prop8", "var_prop9", "var_prop11"]

    var_prop0: FloatProperty(
        name="Amplitude (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Ray Length",
        default=2.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Mode",
        default="0",
        items=create_enum(["Boundary", "Dense"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Density (%)",
        default=80.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness (%)",
        default=0.1,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Threshold (%)",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6_x: FloatProperty(
        name="Light Position X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop6_y: FloatProperty(
        name="Light Position Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop7: FloatVectorProperty(
        name="Light Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Blend Mode",
        default="7",
        items=create_enum(["Add", "Alpha", "Grain Merge", "Hard Light", "Lighten", "Lightness", "Luminance", "Overlay", "Soft Light", "Value"]),
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Opacity (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop11: BoolProperty(
        name="Preview Light Shape",
        default=1,
    ) # type: ignore

    def create_command(self):
        return f"fx_guided_lightrays {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6_x},{self.var_prop6_y},{self.var_prop7[0]*255},{self.var_prop7[1]*255},{self.var_prop7[2]*255},255,{self.var_prop8},{self.var_prop9},{int(self.var_prop11)}"

################################################################################
################################################################################

class GMIC_FLight_lightglow(GMICBaseNode):
    """Light Glow by Author: David Tschumperlé. Latest Update: 2011/21/02."""
    # fx_lightglow

    bl_idname = "FLight_lightglow"
    bl_label = "Light Glow"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Density",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Amplitude",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Mode",
        default="8",
        items=create_enum(["Burn", "Dodge", "Freeze", "Grain Merge", "Hard Light", "Interpolation", "Lighten", "Multiply", "Overlay", "Reflect", "Soft Light", "Stamp", "Value"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Opacity",
        default=0.8,
        min=0.0, 
        max=1.0, 
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
        return f"fx_lightglow {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FLight_lightpatch(GMICBaseNode):
    """Light Patch by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_light_patch

    bl_idname = "FLight_lightpatch"
    bl_label = "Light Patch"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: IntProperty(
        name="Density",
        default=5,
        min=2, 
        max=30, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Darkness",
        default=0.7,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Lightness",
        default=2.5,
        min=1.0, 
        max=4.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_light_patch {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FLight_lightrays(GMICBaseNode):
    """Light Rays by Author: David Tschumperlé. Latest Update: 2023/09/01."""
    # fx_lightrays

    bl_idname = "FLight_lightrays"
    bl_label = "Light Rays"

    node_props = ["var_prop0", "var_prop1_x", "var_prop1_y", "var_prop2", "var_prop3", "var_prop4", "var_prop5"]

    var_prop0: FloatProperty(
        name="Density",
        default=30.0,
        min=0.0, 
        max=100.0, 
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
        name="Length",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Attenuation",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Transparency",
        default=0,
    ) # type: ignore
    var_prop5: FloatVectorProperty(
        name="Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore

    def create_command(self):
        return f"fx_lightrays {self.var_prop0},{self.var_prop1_x},{self.var_prop1_y},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop5[0]*255},{self.var_prop5[1]*255},{self.var_prop5[2]*255},255"

################################################################################
################################################################################

class GMIC_FLight_popshadows(GMICBaseNode):
    """Pop Shadows by Authors: Morgan Hardwood and David Tschumperlé. Latest Update: 2017/03/05."""
    # fx_pop_shadows

    bl_idname = "FLight_popshadows"
    bl_label = "Pop Shadows"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: FloatProperty(
        name="Strength",
        default=0.75,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Scale",
        default=5.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Post-Normalize",
        default=1,
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_pop_shadows {self.var_prop0},{self.var_prop1},{int(self.var_prop2)},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FLight_relieflight(GMICBaseNode):
    """Relief Light by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_light_relief

    bl_idname = "FLight_relieflight"
    bl_label = "Relief Light"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5_x", "var_prop5_y", "var_prop6", "var_prop7", "var_prop8", "var_prop9"]

    var_prop0: FloatProperty(
        name="Ambient Lightness",
        default=0.3,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Specular Lightness",
        default=0.2,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Specular Size",
        default=0.2,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Darkness",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Light Smoothness",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop5_x: FloatProperty(
        name="XY-Light X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop5_y: FloatProperty(
        name="XY-Light Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Z-Light",
        default=5.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Z-Scale",
        default=0.5,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop8: BoolProperty(
        name="Opacity as Heightmap",
        default=0,
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Image Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_light_relief {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5_x},{self.var_prop5_y},{self.var_prop6},{self.var_prop7},{int(self.var_prop8)},{self.var_prop9}"

################################################################################
################################################################################

class GMIC_FLight_shadowpatch(GMICBaseNode):
    """Shadow Patch by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_shadow_patch

    bl_idname = "FLight_shadowpatch"
    bl_label = "Shadow Patch"

    node_props = ["var_prop0", "var_prop2"]

    var_prop0: FloatProperty(
        name="Opacity",
        default=0.7,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_shadow_patch {self.var_prop0},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FLight_sliceluminosity(GMICBaseNode):
    """Slice Luminosity by Author: David Tschumperlé. Latest Update: 2015/22/09."""
    # fx_slice_luminosity

    bl_idname = "FLight_sliceluminosity"
    bl_label = "Slice Luminosity"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop19", "var_prop20", "var_prop21", "var_prop22", "var_prop23", "var_prop26", "var_prop27", "var_prop28", "var_prop29", "var_prop30"]

    var_prop0: EnumProperty(
        name="Luminosity Type",
        default="1",
        items=create_enum(["Average RGB", "Luminance", "Lightness", "Value"]),
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Output As",
        default="1",
        items=create_enum(["Mask", "Masked Image"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Preview Type",
        default="2",
        items=create_enum(["Mask", "Mask + Background", "Image", "Image + Background"]),
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Activate Slice 1",
        default=1,
    ) # type: ignore
    var_prop6: IntProperty(
        name="Starting Value",
        default=0,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Ending Value",
        default=64,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Starting Feathering",
        default=0,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop9: IntProperty(
        name="Ending Feathering",
        default=0,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop12: BoolProperty(
        name="Activate Slice 2",
        default=1,
    ) # type: ignore
    var_prop13: IntProperty(
        name="Starting Value",
        default=64,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop14: IntProperty(
        name="Ending Value",
        default=128,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop15: IntProperty(
        name="Starting Feathering",
        default=0,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop16: IntProperty(
        name="Ending Feathering",
        default=0,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop19: BoolProperty(
        name="Activate Slice 3",
        default=0,
    ) # type: ignore
    var_prop20: IntProperty(
        name="Starting Value",
        default=128,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop21: IntProperty(
        name="Ending Value",
        default=192,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop22: IntProperty(
        name="Starting Feathering",
        default=0,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop23: IntProperty(
        name="Ending Feathering",
        default=0,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop26: BoolProperty(
        name="Activate Slice 4",
        default=0,
    ) # type: ignore
    var_prop27: IntProperty(
        name="Starting Value",
        default=192,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop28: IntProperty(
        name="Ending Value",
        default=255,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop29: FloatProperty(
        name="Starting Feathering",
        default=0.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop30: FloatProperty(
        name="Ending Feathering",
        default=0.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_slice_luminosity {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop5)},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{int(self.var_prop12)},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{int(self.var_prop19)},{self.var_prop20},{self.var_prop21},{self.var_prop22},{self.var_prop23},{int(self.var_prop26)},{self.var_prop27},{self.var_prop28},{self.var_prop29},{self.var_prop30}"

################################################################################
################################################################################

node_classes = [
    GMIC_FLight_burn, GMIC_FLight_contrastswissmask, GMIC_FLight_dodgeandburn, GMIC_FLight_dropshadow, GMIC_FLight_dropshadow3d, GMIC_FLight_equalizelight, GMIC_FLight_equalizeshadow, GMIC_FLight_guidedlightrays, GMIC_FLight_lightglow, GMIC_FLight_lightpatch, GMIC_FLight_lightrays, GMIC_FLight_popshadows, GMIC_FLight_relieflight, GMIC_FLight_shadowpatch, GMIC_FLight_sliceluminosity
]

################################################################################