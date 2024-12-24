from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FBNW_bwstencil(GMICBaseNode):
    """B&W Stencil by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_stencilbw

    bl_idname = "FBNW_bwstencil"
    bl_label = "B&W Stencil"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Threshold",
        default=10.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=10.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Hue",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Saturation",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_stencilbw {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FBNW_blackwhite(GMICBaseNode):
    """Black & White by Author: David Tschumperlé. Latest Update: 2013/20/02."""
    # fx_blackandwhite

    bl_idname = "FBNW_blackwhite"
    bl_label = "Black & White"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop20", "var_prop21", "var_prop22", "var_prop24", "var_prop25", "var_prop27"]

    var_prop0: FloatProperty(
        name="Red Level",
        default=0.299,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Red Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Green Level",
        default=0.587,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Green Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Blue Level",
        default=0.114,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Blue Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
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
    var_prop13: FloatProperty(
        name="Grain (Shadows)",
        default=0.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Grain (Midtones)",
        default=0.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Grain (Highlights)",
        default=0.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Grain Tone Fading",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Grain Scale",
        default=0.0,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop18: EnumProperty(
        name="Grain Type",
        default="0",
        items=create_enum(["Gaussian", "Uniform", "Salt and Pepper", "Poisson"]),
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Local Contrast",
        default=0.0,
        min=0.0, 
        max=60.0, 
    ) # type: ignore
    var_prop21: IntProperty(
        name="Radius",
        default=16,
        min=1, 
        max=512, 
    ) # type: ignore
    var_prop22: FloatProperty(
        name="Contrast Smoothness",
        default=4.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop24: IntProperty(
        name="Pseudo-Gray Dithering",
        default=0,
        min=0, 
        max=5, 
    ) # type: ignore
    var_prop25: BoolProperty(
        name="Use Maximum Tones",
        default=0,
    ) # type: ignore
    var_prop27: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_blackandwhite {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18},{self.var_prop20},{self.var_prop21},{self.var_prop22},{self.var_prop24},{int(self.var_prop25)},{self.var_prop27},50,50"

################################################################################
################################################################################

class GMIC_FBNW_charcoal(GMICBaseNode):
    """Charcoal by Author: David Tschumperlé. Latest Update: 2011/17/03."""
    # fx_charcoal

    bl_idname = "FBNW_charcoal"
    bl_label = "Charcoal"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop12"]

    var_prop0: IntProperty(
        name="Granularity",
        default=65,
        min=0, 
        max=800, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Lowlights Crossover Point",
        default=70,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Highlights Crossover Point",
        default=170,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Boost Contrast",
        default=0,
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Resize Image for Optimum Effect",
        default=1,
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Add Chalk Highlights",
        default=0,
    ) # type: ignore
    var_prop6: IntProperty(
        name="Minimal Highlights",
        default=50,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Maximal Highlights",
        default=70,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop8: FloatVectorProperty(
        name="Background Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop9: FloatVectorProperty(
        name="Foreground Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop10: BoolProperty(
        name="Invert Background / Foreground",
        default=0,
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_charcoal {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{int(self.var_prop4)},{int(self.var_prop5)},{self.var_prop6},{self.var_prop7},{self.var_prop8[0]*255},{self.var_prop8[1]*255},{self.var_prop8[2]*255},255,{self.var_prop9[0]*255},{self.var_prop9[1]*255},{self.var_prop9[2]*255},255,{int(self.var_prop10)},{self.var_prop12},50,50"

################################################################################
################################################################################

class GMIC_FBNW_colorizephotographs(GMICBaseNode):
    """Colorize [Photographs] by Author: David Tschumperlé. Latest Update: 2013/16/01."""
    # fx_recolorize

    bl_idname = "FBNW_colorizephotographs"
    bl_label = "Colorize [Photographs]"

    node_props = ["var_prop0", "var_prop1", "var_prop2"]

    var_prop0: IntProperty(
        name="Smoothness",
        default=2,
        min=0, 
        max=6, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Anisotropy",
        default=0.2,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Output Mode",
        default="0",
        items=create_enum(["Merge Brightness / Colors", "Split Brightness / Colors"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_recolorize {self.var_prop0},{self.var_prop1},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FBNW_colorizewithcolormap(GMICBaseNode):
    """Colorize [with Colormap] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_bwrecolorize

    bl_idname = "FBNW_colorizewithcolormap"
    bl_label = "Colorize [with Colormap]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop7", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop20"]

    var_prop0: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Gamma (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Normalize Input",
        default=0,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Gradient Preset",
        default="0",
        items=create_enum(["User-Defined", "Black to White", "White to Black", "Sepia", "Solarize"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Interpolation Type",
        default="1",
        items=create_enum(["Nearest", "Linear", "Cubic", "Lanczos"]),
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Preserve Initial Brightness",
        default=0,
    ) # type: ignore
    var_prop10: IntProperty(
        name="Number of Tones",
        default=5,
        min=2, 
        max=8, 
    ) # type: ignore
    var_prop11: FloatVectorProperty(
        name="1st Tone",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop12: FloatVectorProperty(
        name="2nd Tone",
        default=(0.16862745098039217,0.09803921568627451,0.21568627450980393),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop13: FloatVectorProperty(
        name="3rd Tone",
        default=(0.6196078431372549,0.5372549019607843,0.7411764705882353),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop14: FloatVectorProperty(
        name="4th Tone",
        default=(0.8784313725490196,0.7490196078431373,0.8941176470588236),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop15: FloatVectorProperty(
        name="5th Tone",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop16: FloatVectorProperty(
        name="6th Tone",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop17: FloatVectorProperty(
        name="7th Tone",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop18: FloatVectorProperty(
        name="8th Tone",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop20: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_bwrecolorize {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{self.var_prop5},{self.var_prop6},{int(self.var_prop7)},{self.var_prop10},{self.var_prop11[0]*255},{self.var_prop11[1]*255},{self.var_prop11[2]*255},255,{self.var_prop12[0]*255},{self.var_prop12[1]*255},{self.var_prop12[2]*255},255,{self.var_prop13[0]*255},{self.var_prop13[1]*255},{self.var_prop13[2]*255},255,{self.var_prop14[0]*255},{self.var_prop14[1]*255},{self.var_prop14[2]*255},255,{self.var_prop15[0]*255},{self.var_prop15[1]*255},{self.var_prop15[2]*255},255,{self.var_prop16[0]*255},{self.var_prop16[1]*255},{self.var_prop16[2]*255},255,{self.var_prop17[0]*255},{self.var_prop17[1]*255},{self.var_prop17[2]*255},255,{self.var_prop18[0]*255},{self.var_prop18[1]*255},{self.var_prop18[2]*255},255,{self.var_prop20},50,50"

################################################################################
################################################################################

class GMIC_FBNW_colorizelineartautofill(GMICBaseNode):
    """Colorize Lineart [Auto-Fill] by Author: David Tschumperlé. Latest Update: 2016/12/11."""
    # fx_autofill_lineart

    bl_idname = "FBNW_colorizelineartautofill"
    bl_label = "Colorize Lineart [Auto-Fill]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: FloatProperty(
        name="Contour Threshold (%)",
        default=90.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: BoolProperty(
        name="Contour Normalization",
        default=1,
    ) # type: ignore
    var_prop2: IntProperty(
        name="Minimal Region Area",
        default=8,
        min=0, 
        max=256, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Tolerance to Gaps",
        default=0,
        min=0, 
        max=10, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Lineart + Colors", "Colors Only"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_autofill_lineart {self.var_prop0},{int(self.var_prop1)},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FBNW_colorizelineartsmartcoloring(GMICBaseNode):
    """Colorize Lineart [Smart Coloring] by Authors: David Tschumperlé, Sébastien Fourey and David Revoy. Latest Update: 2018/11/09."""
    # fx_colorize_lineart_smart

    bl_idname = "FBNW_colorizelineartsmartcoloring"
    bl_label = "Colorize Lineart [Smart Coloring]"

    node_props = ["var_prop0", "var_prop3", "var_prop4", "var_prop6", "var_prop9", "var_prop10", "var_prop11", "var_prop14", "var_prop17", "var_prop18", "var_prop19", "var_prop20", "var_prop21", "var_prop22", "var_prop23", "var_prop24", "var_prop26"]

    var_prop0: EnumProperty(
        name="Colorize Mode",
        default="0",
        items=create_enum(["Generate Random-Colors Layer", "Extrapolate Color Spots on Transparent Top Layer", "Auto-Clean Bottom Color Layer"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Contour Detection (%)",
        default=95.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Discard Contour Guides",
        default=0,
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Output Region Delimiters",
        default=0,
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Make Hue Depends on Region Size",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop10: IntProperty(
        name="Maximal Color Saturation",
        default=24,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop11: IntProperty(
        name="Minimal Color Intensity",
        default=200,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop14: IntProperty(
        name="Color Shading (%)",
        default=0,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="End Point Rate (%)",
        default=75.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop18: IntProperty(
        name="End Point Connectivity",
        default=2,
        min=1, 
        max=5, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Spline Max Length (px)",
        default=60.0,
        min=0.0, 
        max=256.0, 
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Segment Max Length (px)",
        default=20.0,
        min=0.0, 
        max=256.0, 
    ) # type: ignore
    var_prop21: FloatProperty(
        name="Spline Max Angle (deg)",
        default=90.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop22: FloatProperty(
        name="Spline Roundness",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop23: FloatProperty(
        name="Minimal Region Area",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop24: BoolProperty(
        name="Allow Self Intersections",
        default=1,
    ) # type: ignore
    var_prop26: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Colored geometry", "Colored regions", "Colored lineart"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_colorize_lineart_smart {self.var_prop0},{self.var_prop3},{int(self.var_prop4)},{int(self.var_prop6)},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop14},{self.var_prop17},{self.var_prop18},{self.var_prop19},{self.var_prop20},{self.var_prop21},{self.var_prop22},{self.var_prop23},{int(self.var_prop24)},{self.var_prop26}"

################################################################################
################################################################################

class GMIC_FBNW_desaturatenorm(GMICBaseNode):
    """Desaturate Norm by Author : Garagecoder. Latest update : 2016/12/27."""
    # fx_gcd_norm_eq

    bl_idname = "FBNW_desaturatenorm"
    bl_label = "Desaturate Norm"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop2: FloatProperty(
        name="Red",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Blue",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Exp",
        default=2.0,
        min=1.0, 
        max=3.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_gcd_norm_eq {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FBNW_dithering(GMICBaseNode):
    """Dithering by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_ditheredbw

    bl_idname = "FBNW_dithering"
    bl_label = "Dithering"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Gamma (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Hue",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Saturation (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_ditheredbw {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FBNW_emboss(GMICBaseNode):
    """Emboss by Author : Garagecoder. Latest update : 2014/11/11."""
    # gcd_emboss

    bl_idname = "FBNW_emboss"
    bl_label = "Emboss"

    node_props = ["var_prop2", "var_prop4"]

    var_prop2: IntProperty(
        name="Midpoint",
        default=128,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"gcd_emboss {self.var_prop2},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FBNW_engrave(GMICBaseNode):
    """Engrave by Authors: Lyle Kroll and David Tschumperlé. Latest Update: 03/13/2015."""
    # fx_engrave

    bl_idname = "FBNW_engrave"
    bl_label = "Engrave"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop17", "var_prop19"]

    var_prop1: FloatProperty(
        name="Radius",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Density",
        default=50.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Edges",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Coherence",
        default=8.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Threshold (%)",
        default=40.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: IntProperty(
        name="Minimal Area",
        default=0,
        min=-256, 
        max=256, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Flat Regions Removal",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop10: BoolProperty(
        name="Add Color Background",
        default=0,
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Quantization",
        default=10.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop12: IntProperty(
        name="Shading",
        default=1,
        min=0, 
        max=5, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Hue",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Saturation (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Lightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop17: EnumProperty(
        name="Anti-Aliasing",
        default="1",
        items=create_enum(["Disabled", "x1.5", "x2", "x3"]),
    ) # type: ignore
    var_prop19: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_engrave {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{int(self.var_prop10)},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop17},{self.var_prop19},50,50"

################################################################################
################################################################################

class GMIC_FBNW_freakybw(GMICBaseNode):
    """Freaky B&W by Author: David Tschumperlé. Latest Update: 2015/30/09."""
    # fx_freaky_bw

    bl_idname = "FBNW_freakybw"
    bl_label = "Freaky B&W"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Strength (%)",
        default=90.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Oddness (%)",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Gamma (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_freaky_bw {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FBNW_inkwash(GMICBaseNode):
    """Ink Wash by Author: PhotoComiX. Latest Update: 2011/05/04."""
    # fx_ink_wash

    bl_idname = "FBNW_inkwash"
    bl_label = "Ink Wash"

    node_props = ["var_prop1", "var_prop2", "var_prop5", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop15", "var_prop16", "var_prop17", "var_prop18"]

    var_prop1: FloatProperty(
        name="Size",
        default=0.14,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Amplitude",
        default=23.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Skip All Other Steps",
        default=0,
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Smoother Sharpness",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Smoother Edge Protection",
        default=0.54,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Smoother Softness",
        default=2.25,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Stretch Contrast",
        default="0",
        items=create_enum(["None", "Automatic", "Automatic & Contrast Mask", "Manual Controls"]),
    ) # type: ignore
    var_prop15: FloatProperty(
        name="LN Amplitude",
        default=2.0,
        min=0.0, 
        max=60.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="LN Size",
        default=6.0,
        min=0.0, 
        max=64.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="LN Neightborhood-Smoothness",
        default=5.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="LN Average-Smoothness",
        default=20.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_ink_wash {self.var_prop1},{self.var_prop2},{int(self.var_prop5)},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop12},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18}"

################################################################################
################################################################################

class GMIC_FBNW_pencil(GMICBaseNode):
    """Pencil by Author: David Tschumperlé. Latest Update: 2013/05/03."""
    # fx_pencilbw

    bl_idname = "FBNW_pencil"
    bl_label = "Pencil"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Size",
        default=0.3,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Amplitude",
        default=60.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Hue",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Saturation",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_pencilbw {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FBNW_pencilportrait(GMICBaseNode):
    """Pencil Portrait by Authors: Jamac4k and David Tschumperlé. Latest Update: 2015/29/06."""
    # fx_pencil_portraitbw

    bl_idname = "FBNW_pencilportrait"
    bl_label = "Pencil Portrait"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Stroke Length",
        default=30.0,
        min=0.0, 
        max=500.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Stroke Angle",
        default=120.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Contour Threshold",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Opacity",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatVectorProperty(
        name="Color",
        default=(0.5647058823529412,0.30980392156862746,0.08235294117647059),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_pencil_portraitbw {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4[0]*255},{self.var_prop4[1]*255},{self.var_prop4[2]*255},255,{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FBNW_stamp(GMICBaseNode):
    """Stamp by Authors: Antaron, Mahvin and David Tschumperlé. Latest Update: 2015/16/03."""
    # fx_stamp

    bl_idname = "FBNW_stamp"
    bl_label = "Stamp"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: BoolProperty(
        name="Auto-Threshold",
        default=1,
    ) # type: ignore
    var_prop1: IntProperty(
        name="Threshold",
        default=50,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Sharpening",
        default=0.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Grain",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Negative",
        default=0,
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Anti-Aliasing",
        default=1,
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_stamp {int(self.var_prop0)},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{int(self.var_prop6)},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FBNW_thresholdetch(GMICBaseNode):
    """Threshold Etch by Author : Garagecoder. Latest update : 2013/02/09."""
    # fx_gcd_etch

    bl_idname = "FBNW_thresholdetch"
    bl_label = "Threshold Etch"

    node_props = ["var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop20", "var_prop21", "var_prop22", "var_prop23", "var_prop25"]

    var_prop3: IntProperty(
        name="Threshold Low",
        default=125,
        min=10, 
        max=255, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Threshold Mid",
        default=153,
        min=10, 
        max=255, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Threshold High",
        default=171,
        min=10, 
        max=255, 
    ) # type: ignore
    var_prop6: IntProperty(
        name="Threshold Max",
        default=185,
        min=10, 
        max=255, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Blur Amount",
        default=0.1,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop10: IntProperty(
        name="Horizontal Amount",
        default=50,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop11: IntProperty(
        name="Cross-Hatch Amount",
        default=80,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop12: IntProperty(
        name="Vertical 1 Amount",
        default=50,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop13: IntProperty(
        name="Vertical 2 Amount",
        default=10,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop15: IntProperty(
        name="Horizontal Length",
        default=15,
        min=0, 
        max=50, 
    ) # type: ignore
    var_prop16: IntProperty(
        name="Vertical 1 Length",
        default=12,
        min=0, 
        max=50, 
    ) # type: ignore
    var_prop17: IntProperty(
        name="Vertical 2 Length",
        default=20,
        min=0, 
        max=50, 
    ) # type: ignore
    var_prop18: BoolProperty(
        name="Flip Cross-Hatch",
        default=0,
    ) # type: ignore
    var_prop20: IntProperty(
        name="Curve Amount",
        default=1,
        min=0, 
        max=20, 
    ) # type: ignore
    var_prop21: FloatProperty(
        name="Gamma",
        default=0.3,
        min=0.01, 
        max=1.0, 
    ) # type: ignore
    var_prop22: BoolProperty(
        name="Fast Resize",
        default=1,
    ) # type: ignore
    var_prop23: BoolProperty(
        name="Color Image",
        default=0,
    ) # type: ignore
    var_prop25: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_gcd_etch {self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop15},{self.var_prop16},{self.var_prop17},{int(self.var_prop18)},{self.var_prop20},{self.var_prop21},{int(self.var_prop22)},{int(self.var_prop23)},{self.var_prop25}"

################################################################################
################################################################################

node_classes = [
    GMIC_FBNW_bwstencil, GMIC_FBNW_blackwhite, GMIC_FBNW_charcoal, GMIC_FBNW_colorizephotographs, GMIC_FBNW_colorizewithcolormap, GMIC_FBNW_colorizelineartautofill, GMIC_FBNW_colorizelineartsmartcoloring, GMIC_FBNW_desaturatenorm, GMIC_FBNW_dithering, GMIC_FBNW_emboss, GMIC_FBNW_engrave,
    GMIC_FBNW_freakybw, GMIC_FBNW_inkwash, GMIC_FBNW_pencil, GMIC_FBNW_pencilportrait, GMIC_FBNW_stamp, GMIC_FBNW_thresholdetch
]

################################################################################