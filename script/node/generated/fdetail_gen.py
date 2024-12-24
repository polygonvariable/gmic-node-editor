from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FDetail_constrainedsharpen(GMICBaseNode):
    """Constrained Sharpen by Author : Iain Fergusson. release: 2 August 2016 update: 25 August 2018"""
    # iain_constrained_sharpen

    bl_idname = "FDetail_constrainedsharpen"
    bl_label = "Constrained Sharpen"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6"]

    var_prop0: FloatProperty(
        name="Sharpen Radius",
        default=.75,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Amount",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Threshold",
        default=1.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Constraint Radius",
        default=5,
        min=0, 
        max=10, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Overshoot",
        default=0.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [all]", "RGB [all]", "RGB [red]", "RGB [green]", "RGB [blue]", "RGBA [alpha]", "Linear RGB [all]", "Linear RGB [red]", "Linear RGB [green]", "Linear RGB [blue]", "YCbCr [luminance]", "YCbCr [blue-red chrominances]", "YCbCr [blue chrominance]", "YCbCr [red chrominance]", "YCbCr [green chrominance]", "Lab [lightness]", "Lab [ab-chrominances]", "Lab [a-chrominance]", "Lab [b-chrominance]", "Lch [ch-chrominances]", "Lch [c-chrominance]", "Lch [h-chrominance]", "HSV [hue]", "HSV [saturation]", "HSV [value]", "HSI [intensity]", "HSL [lightness]", "CMYK [cyan]", "CMYK [magenta]", "CMYK [yellow]", "CMYK [key]"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Value Action",
        default="1",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore

    def create_command(self):
        return f"iain_constrained_sharpen {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FDetail_dcpdehaze(GMICBaseNode):
    """DCP Dehaze by Dark Channel Prior dehazing.Author : Jérôme Boulanger. Latest update: 2016/08/09."""
    # jeje_dehaze

    bl_idname = "FDetail_dcpdehaze"
    bl_label = "DCP Dehaze"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop9"]

    var_prop0: IntProperty(
        name="Scale",
        default=5,
        min=1, 
        max=20, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Strength",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Min",
        default=.2,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Max",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Brighness",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Contrast",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Gamma",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Transmittance Map",
        default=0,
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_dehaze {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{int(self.var_prop7)},{self.var_prop9}"

################################################################################
################################################################################

class GMIC_FDetail_detailsequalizer(GMICBaseNode):
    """Details Equalizer by Author: Jérome Boulanger and David Tschumperlé. Latest Update: 2015/11/11."""
    # fx_equalize_details

    bl_idname = "FDetail_detailsequalizer"
    bl_label = "Details Equalizer"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop21", "var_prop22", "var_prop23", "var_prop24", "var_prop26", "var_prop27", "var_prop29", "var_prop30", "var_prop32"]

    var_prop0: FloatProperty(
        name="Base Scale",
        default=5.0,
        min=0.0, 
        max=15.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Detail Scale",
        default=0.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Threshold",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Smoothness Type",
        default="2",
        items=create_enum(["Gaussian", "Bilateral", "Diffusion"]),
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Gain",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Threshold",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Smoothness Type",
        default="2",
        items=create_enum(["Gaussian", "Bilateral", "Diffusion"]),
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Gain",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Threshold",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop17: EnumProperty(
        name="Smoothness Type",
        default="2",
        items=create_enum(["Gaussian", "Bilateral", "Diffusion"]),
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Gain",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop21: FloatProperty(
        name="Threshold",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop22: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop23: EnumProperty(
        name="Smoothness Type",
        default="2",
        items=create_enum(["Gaussian", "Bilateral", "Diffusion"]),
    ) # type: ignore
    var_prop24: FloatProperty(
        name="Gain",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop26: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop27: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop29: EnumProperty(
        name="Parallel Processing",
        default="0",
        items=create_enum(["Auto", "One Thread", "Two Threads", "Four Threads", "Eight Threads", "Sixteen Threads"]),
    ) # type: ignore
    var_prop30: IntProperty(
        name="Spatial Overlap",
        default=32,
        min=0, 
        max=256, 
    ) # type: ignore
    var_prop32: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_equalize_details {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18},{self.var_prop21},{self.var_prop22},{self.var_prop23},{self.var_prop24},{self.var_prop26},{self.var_prop27},{self.var_prop29},{self.var_prop30},{self.var_prop32},50,50"

################################################################################
################################################################################

class GMIC_FDetail_dynamicrangeincrease(GMICBaseNode):
    """Dynamic Range Increase by Author: Tom Keil Latest update: 2011/12/04."""
    # fx_tk_dri

    bl_idname = "FDetail_dynamicrangeincrease"
    bl_label = "Dynamic Range Increase"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="Map Tones",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Recover Shadows",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Recover Highlights",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Enhance Details",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Detail Strength",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Map Tones",
        default=1,
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Enhance Details",
        default=1,
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_tk_dri {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{int(self.var_prop6)},{self.var_prop8}"

################################################################################
################################################################################

class GMIC_FDetail_easyskinretouch(GMICBaseNode):
    """Easy Skin Retouch by Author: Iain Fergusson - update 12 May 2013 - now handles alpha channel and some internal changes"""
    # iain_easy_skin_retouch

    bl_idname = "FDetail_easyskinretouch"
    bl_label = "Easy Skin Retouch"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop15"]

    var_prop1: FloatProperty(
        name="Edge Sensitivity",
        default=7.0,
        min=0.0, 
        max=25.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Iterations",
        default=2,
        min=1, 
        max=5, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Low Bias",
        default=.7,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop7: BoolProperty(
        name="On",
        default=1,
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Very Fine",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Fine 2",
        default=.7,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Medium 3",
        default=.6,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Course 4",
        default=.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Very Course 5",
        default=.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Reduce Redness",
        default=.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop15: BoolProperty(
        name="Split Base and Detail Output",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"iain_easy_skin_retouch {self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop7)},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{int(self.var_prop15)}"

################################################################################
################################################################################

class GMIC_FDetail_embossrelief(GMICBaseNode):
    """Emboss-Relief by Author: Reptorian. Latest Update: 2021/12/07."""
    # fx_emboss_relief

    bl_idname = "FDetail_embossrelief"
    bl_label = "Emboss-Relief"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: IntProperty(
        name="Radius",
        default=5,
        min=5, 
        max=100, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Angle",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Sigma",
        default=.5,
        min=.05, 
        max=4.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Value Scale",
        default=2.0,
        min=.5, 
        max=10.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Output",
        default="0",
        items=create_enum(["Emboss", "Relief"]),
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Output Color",
        default=1,
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Preserve Alpha?",
        default=1,
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_emboss_relief {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{int(self.var_prop6)},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FDetail_equalizelocalhistograms(GMICBaseNode):
    """Equalize Local Histograms by Author: David Tschumperlé. Latest Update: 2018/01/31."""
    # fx_equalize_local_histograms

    bl_idname = "FDetail_equalizelocalhistograms"
    bl_label = "Equalize Local Histograms"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7", "var_prop9"]

    var_prop0: FloatProperty(
        name="Strength (%)",
        default=75.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Mode",
        default="2",
        items=create_enum(["Raw", "Hard", "Soft"]),
    ) # type: ignore
    var_prop2: IntProperty(
        name="Radius",
        default=4,
        min=1, 
        max=16, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Sigma",
        default=100.0,
        min=0.0, 
        max=256.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Regularization",
        default=8.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Reduce Halos",
        default=1,
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Channel(s)",
        default="16",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_equalize_local_histograms {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{self.var_prop7},{self.var_prop9},50,50"

################################################################################
################################################################################

class GMIC_FDetail_freakydetails(GMICBaseNode):
    """Freaky Details by Authors: David Tschumperlé and Patrick David. Latest Update: 2013/27/02."""
    # fx_freaky_details

    bl_idname = "FDetail_freakydetails"
    bl_label = "Freaky Details"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop6"]

    var_prop0: IntProperty(
        name="Amplitude",
        default=2,
        min=1, 
        max=5, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Scale",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Iterations",
        default=1,
        min=1, 
        max=4, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_freaky_details {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FDetail_highpass(GMICBaseNode):
    """High Pass by Author : Tom Keil. Latest update: 2011/05/01."""
    # fx_highpass

    bl_idname = "FDetail_highpass"
    bl_label = "High Pass"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Radius",
        default=5.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Contrast",
        default=2.0,
        min=0.0, 
        max=7.0, 
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Inverse",
        default=0,
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Greyscale",
        default=0,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_highpass {self.var_prop0},{self.var_prop1},{int(self.var_prop2)},{int(self.var_prop3)},{self.var_prop5}"

################################################################################
################################################################################

class GMIC_FDetail_localcontrastenhancement(GMICBaseNode):
    """Local Contrast Enhancement by Authors : Arto Huotari, PhotoComiX. Latest update : 2013/03/23."""
    # fx_LCE

    bl_idname = "FDetail_localcontrastenhancement"
    bl_label = "Local Contrast Enhancement"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop8"]

    var_prop1: FloatProperty(
        name="Spatial Radius",
        default=80.0,
        min=30.0, 
        max=200.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Amount",
        default=0.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Darkness Level",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Lightness Level",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [all]", "RGB [all]", "RGB [red]", "RGB [green]", "RGB [blue]", "RGBA [alpha]", "Linear RGB [all]", "Linear RGB [red]", "Linear RGB [green]", "Linear RGB [blue]", "YCbCr [luminance]", "YCbCr [blue-red chrominances]", "YCbCr [blue chrominance]", "YCbCr [red chrominance]", "YCbCr [green chrominance]", "Lab [lightness]", "Lab [ab-chrominances]", "Lab [a-chrominance]", "Lab [b-chrominance]", "Lch [ch-chrominances]", "Lch [c-chrominance]", "Lch [h-chrominance]", "HSV [hue]", "HSV [saturation]", "HSV [value]", "HSI [intensity]", "HSL [lightness]", "CMYK [cyan]", "CMYK [magenta]", "CMYK [yellow]", "CMYK [key]", "YIQ [luma]", "YIQ [chromas]"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_LCE {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},{self.var_prop8}"

################################################################################
################################################################################

class GMIC_FDetail_localnormalization(GMICBaseNode):
    """Local Normalization by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_normalize_local

    bl_idname = "FDetail_localnormalization"
    bl_label = "Local Normalization"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=2.0,
        min=0.0, 
        max=60.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Radius",
        default=6,
        min=1, 
        max=64, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Neighborhood Smoothness",
        default=5.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Average Smoothness",
        default=20.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Constrain Values",
        default=1,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_normalize_local {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop6},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FDetail_localprocessing(GMICBaseNode):
    """Local Processing by Author: David Tschumperlé. Latest Update: 2018/02/28."""
    # fx_local_processing

    bl_idname = "FDetail_localprocessing"
    bl_label = "Local Processing"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7", "var_prop9"]

    var_prop0: EnumProperty(
        name="Action",
        default="0",
        items=create_enum(["Normalize", "Equalize"]),
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Strength (%)",
        default=75.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Neighborhood Size (%)",
        default=10.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Overlap (%)",
        default=50.0,
        min=0.0, 
        max=75.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Regularization (%)",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Process Channels Individually",
        default=0,
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Channel(s)",
        default="7",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_local_processing {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{self.var_prop7},{self.var_prop9},50,50"

################################################################################
################################################################################

class GMIC_FDetail_localvariancenormalization(GMICBaseNode):
    """Local Variance Normalization by Author : Jérôme Boulanger. Latest update: 2013/10/30."""
    # jeje_normalize_local_variance

    bl_idname = "FDetail_localvariancenormalization"
    bl_label = "Local Variance Normalization"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=5.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Threshold",
        default=5.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Repeat",
        default=1,
        min=1, 
        max=4, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [all]", "RGB [all]", "RGB [red]", "RGB [green]", "RGB [blue]", "RGBA [alpha]", "Linear RGB [all]", "Linear RGB [red]", "Linear RGB [green]", "Linear RGB [blue]", "YCbCr [luminance]", "YCbCr [blue-red chrominances]", "YCbCr [blue chrominance]", "YCbCr [red chrominance]", "YCbCr [green chrominance]", "Lab [lightness]", "Lab [ab-chrominances]", "Lab [a-chrominance]", "Lab [b-chrominance]", "Lch [ch-chrominances]", "Lch [c-chrominance]", "Lch [h-chrominance]", "HSV [hue]", "HSV [saturation]", "HSV [value]", "HSI [intensity]", "HSL [lightness]", "CMYK [cyan]", "CMYK [magenta]", "CMYK [yellow]", "CMYK [key]", "YIQ [luma]", "YIQ [chromas]"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_normalize_local_variance {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop7}"

################################################################################
################################################################################

class GMIC_FDetail_magicdetails(GMICBaseNode):
    """Magic Details by Author: David Tschumperlé. Latest Update: 2018/01/10."""
    # fx_magic_details

    bl_idname = "FDetail_magicdetails"
    bl_label = "Magic Details"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=6.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Spatial Scale",
        default=3.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Value Scale",
        default=15.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Edges",
        default=-0.5,
        min=-3.0, 
        max=3.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness",
        default=2.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channel(s)",
        default="27",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_magic_details {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FDetail_makeup(GMICBaseNode):
    """Make Up by Author : Iain Fergusson. - Update: 1 March 2013: Fixed resizing issue, some memory useage improvements, and added more options."""
    # make_up

    bl_idname = "FDetail_makeup"
    bl_label = "Make Up"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Space",
        default=15.0,
        min=1.0, 
        max=40.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Value",
        default=4.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Fast",
        default=0,
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Limit Hue Range",
        default=0,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"make_up {self.var_prop0},{self.var_prop1},{int(self.var_prop2)},{int(self.var_prop3)},{self.var_prop5}"

################################################################################
################################################################################

class GMIC_FDetail_maskcreator(GMICBaseNode):
    """Mask Creator by Author: Tom Keil. Latest update: 2011/11/04."""
    # fx_tk_mask

    bl_idname = "FDetail_maskcreator"
    bl_label = "Mask Creator"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop11"]

    var_prop1: EnumProperty(
        name="Mask Type",
        default="0",
        items=create_enum(["Luminance", "Saturation", "Hue", "LAB-lightness"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Color Channels",
        default="0",
        items=create_enum(["All", "Red", "Green", "Blue", "Yellow", "Magenta", "Cyan", "LAB-A", "LAB-B"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Shadows Threshold",
        default=0.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Highlights Threshold",
        default=255.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Tones Smoothness",
        default=0.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Mask Contrast",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Negative",
        default=0,
    ) # type: ignore
    var_prop8: BoolProperty(
        name="Apply Mask",
        default=0,
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Transparency",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_tk_mask {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{int(self.var_prop7)},{int(self.var_prop8)},{self.var_prop9},{self.var_prop11}"

################################################################################
################################################################################

class GMIC_FDetail_mightydetails(GMICBaseNode):
    """Mighty Details by Author: David Tschumperlé. Latest Update: 2014/08/08."""
    # fx_mighty_details

    bl_idname = "FDetail_mightydetails"
    bl_label = "Mighty Details"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=25.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Details Amount",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Details Scale",
        default=25.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Details Smoothness",
        default=1,
        min=0, 
        max=10, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_mighty_details {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FDetail_portraitretouching(GMICBaseNode):
    """Portrait Retouching by Author: Tom Keil. Latest update: 2012/18/04."""
    # fx_tk_portrait

    bl_idname = "FDetail_portraitretouching"
    bl_label = "Portrait Retouching"

    node_props = ["var_prop1", "var_prop2", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop19", "var_prop20", "var_prop23", "var_prop24", "var_prop25", "var_prop26", "var_prop27", "var_prop28", "var_prop29", "var_prop30", "var_prop31", "var_prop33", "var_prop34"]

    var_prop1: EnumProperty(
        name="Retouching Style",
        default="0",
        items=create_enum(["Standard", "Glamour glow", "Masculine", "High key", "Low Key"]),
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Effect Strength",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Fine Details Smoothness",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Medium Details Smoothness",
        default=5.0,
        min=0.0, 
        max=25.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Areas Smoothness",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Fine Details Threshold",
        default=3.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Medium Details Threshold",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Areas Light Adjustment",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Smoothing Type",
        default="0",
        items=create_enum(["Gaussian", "Bilateral", "Anisotropic", "Median"]),
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Output Mode",
        default="0",
        items=create_enum(["Retouched image", "Composed layers", "All layers and masks"]),
    ) # type: ignore
    var_prop15: BoolProperty(
        name="Apply Skin Tone Mask",
        default=1,
    ) # type: ignore
    var_prop16: EnumProperty(
        name="Similarity Space",
        default="2",
        items=create_enum(["RGB[A]", "RGB", "YCbCr", "Red", "Green", "Blue", "Opacity", "Luminance", "Blue & Red chrominances", "Hue", "Saturation"]),
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Tolerance",
        default=25.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Smoothness",
        default=2.0,
        min=0.0, 
        max=25.0, 
    ) # type: ignore
    var_prop19: FloatVectorProperty(
        name="Selected Color",
        default=(0.9803921568627451,0.7058823529411765,0.5882352941176471),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop20: BoolProperty(
        name="Generic Skin Structure",
        default=0,
    ) # type: ignore
    var_prop23: EnumProperty(
        name="Apply Adjustments On",
        default="0",
        items=create_enum(["Final image", "Retouched areas only", "Sharpened areas only", "Retouched and sharpened areas"]),
    ) # type: ignore
    var_prop24: FloatProperty(
        name="Sharpening Radius",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop25: FloatProperty(
        name="Sharpening Strength",
        default=1.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop26: FloatProperty(
        name="Edge Threshold",
        default=10.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop27: FloatProperty(
        name="Edge Smoothness",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop28: FloatProperty(
        name="Color Temperature",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop29: FloatProperty(
        name="Lightness",
        default=0.0,
        min=-50.0, 
        max=50.0, 
    ) # type: ignore
    var_prop30: FloatProperty(
        name="Contrast",
        default=1.0,
        min=0.5, 
        max=1.5, 
    ) # type: ignore
    var_prop31: FloatProperty(
        name="Saturation",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop33: EnumProperty(
        name="Preview Selection",
        default="0",
        items=create_enum(["Retouched image final", "Retouched image basic", "Retouch layer", "Sharpening layer", "Skin tone mask", "Skin tone colors", "Edge mask", "High frequency layer", "Medium frequency layer", "Low frequency layer"]),
    ) # type: ignore
    var_prop34: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_tk_portrait {self.var_prop1},{self.var_prop2},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{int(self.var_prop15)},{self.var_prop16},{self.var_prop17},{self.var_prop18},{self.var_prop19[0]*255},{self.var_prop19[1]*255},{self.var_prop19[2]*255},255,{int(self.var_prop20)},{self.var_prop23},{self.var_prop24},{self.var_prop25},{self.var_prop26},{self.var_prop27},{self.var_prop28},{self.var_prop29},{self.var_prop30},{self.var_prop31},{self.var_prop33},{self.var_prop34}"

################################################################################
################################################################################

class GMIC_FDetail_pyramidprocessing(GMICBaseNode):
    """Pyramid Processing by  14 June 2017 - First release"""
    # iain_pyramid_processing

    bl_idname = "FDetail_pyramidprocessing"
    bl_label = "Pyramid Processing"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: IntProperty(
        name="1 Levels",
        default=4,
        min=1, 
        max=6, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="2 Noise",
        default=50.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="3 Mix",
        default=.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Type",
        default="0",
        items=create_enum(["Mix", "Add"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Channels",
        default="0",
        items=create_enum(["Lightness", "Luma", "RGB"]),
    ) # type: ignore

    def create_command(self):
        return f"iain_pyramid_processing {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FDetail_quicktonemap(GMICBaseNode):
    """Quick Tonemap by Author : Garagecoder. Latest update : 2018/06/26."""
    # fx_gcd_quicktone

    bl_idname = "FDetail_quicktonemap"
    bl_label = "Quick Tonemap"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7"]

    var_prop2: FloatProperty(
        name="Power",
        default=1.0,
        min=0.5, 
        max=2.5, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Radius",
        default=4.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Range",
        default=20.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Smooth",
        default=0.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channels",
        default="3",
        items=create_enum(["HSI", "HSV", "Lab", "YCbCr"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Values",
        default="1",
        items=create_enum(["cut", "normalize"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_gcd_quicktone {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7}"

################################################################################
################################################################################

class GMIC_FDetail_sharpendeblur(GMICBaseNode):
    """Sharpen [Deblur] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_deblur

    bl_idname = "FDetail_sharpendeblur"
    bl_label = "Sharpen [Deblur]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop8", "var_prop9", "var_prop11"]

    var_prop0: FloatProperty(
        name="Radius",
        default=2.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Iterations",
        default=10,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Time Step",
        default=20.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Smoothness",
        default=0.1,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Regularization",
        default="1",
        items=create_enum(["Tikhonov", "Mean Curvature", "Total Variation"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Parallel Processing",
        default="0",
        items=create_enum(["Auto", "One Thread", "Two Threads", "Four Threads", "Eight Threads", "Sixteen Threads"]),
    ) # type: ignore
    var_prop9: IntProperty(
        name="Spatial Overlap",
        default=24,
        min=0, 
        max=256, 
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_deblur {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop11},50,50"

################################################################################
################################################################################

class GMIC_FDetail_sharpengoldmeinel(GMICBaseNode):
    """Sharpen [Gold-Meinel] by Author: Jérôme Boulanger. Latest Update: 2013/29/03."""
    # fx_unsharp_goldmeinel

    bl_idname = "FDetail_sharpengoldmeinel"
    bl_label = "Sharpen [Gold-Meinel]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop8", "var_prop9", "var_prop11"]

    var_prop0: FloatProperty(
        name="Sigma",
        default=1.0,
        min=0.5, 
        max=10.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Iterations",
        default=5,
        min=1, 
        max=15, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Acceleration",
        default=1.0,
        min=1.0, 
        max=3.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Blur",
        default="1",
        items=create_enum(["Exponential", "Gaussian"]),
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Cut",
        default=1,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Parallel Processing",
        default="0",
        items=create_enum(["Auto", "One Thread", "Two Threads", "Four Threads", "Eight Threads", "Sixteen Threads"]),
    ) # type: ignore
    var_prop9: IntProperty(
        name="Spatial Overlap",
        default=24,
        min=0, 
        max=256, 
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_unsharp_goldmeinel {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop11},50,50"

################################################################################
################################################################################

class GMIC_FDetail_sharpengradient(GMICBaseNode):
    """Sharpen [Gradient] by Author : Garagecoder. Latest update : 2015/09/28."""
    # gcd_sharpen_gradient

    bl_idname = "FDetail_sharpengradient"
    bl_label = "Sharpen [Gradient]"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop2: FloatProperty(
        name="Amount",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Scale",
        default=2.0,
        min=0.1, 
        max=2.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Values",
        default="0",
        items=create_enum(["cut", "normalize luma"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"gcd_sharpen_gradient {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FDetail_sharpenhessian(GMICBaseNode):
    """Sharpen [Hessian] by Author : Jérôme Boulanger. Latest update: 2019/04/30."""
    # jeje_hessian_sharpen

    bl_idname = "FDetail_sharpenhessian"
    bl_label = "Sharpen [Hessian]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: IntProperty(
        name="Number of scales",
        default=3,
        min=2, 
        max=10, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Strength",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Repeat",
        default=1.0,
        min=1.0, 
        max=5.0, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Cut",
        default=0,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_hessian_sharpen {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{self.var_prop5}"

################################################################################
################################################################################

class GMIC_FDetail_sharpeninversediffusion(GMICBaseNode):
    """Sharpen [Inverse Diffusion] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_sharpen_inversediff

    bl_idname = "FDetail_sharpeninversediffusion"
    bl_label = "Sharpen [Inverse Diffusion]"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=50.0,
        min=1.0, 
        max=300.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Iterations",
        default=2,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_sharpen_inversediff {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FDetail_sharpenmultiscale(GMICBaseNode):
    """Sharpen [Multiscale] by Author: David Tschumperlé. Latest Update: 2020/01/14."""
    # fx_sharpen_multiscale

    bl_idname = "FDetail_sharpenmultiscale"
    bl_label = "Sharpen [Multiscale]"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Strength (%)",
        default=15.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Regularity (%)",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_sharpen_multiscale {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FDetail_sharpenoctavesharpening(GMICBaseNode):
    """Sharpen [Octave Sharpening] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_unsharp_octave

    bl_idname = "FDetail_sharpenoctavesharpening"
    bl_label = "Sharpen [Octave Sharpening]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop7", "var_prop8", "var_prop10"]

    var_prop0: IntProperty(
        name="Scales",
        default=4,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Maximal Radius",
        default=5.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Amount",
        default=3.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Threshold",
        default=0.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Parallel Processing",
        default="1",
        items=create_enum(["Auto", "One Thread", "Two Threads", "Four Threads", "Eight Threads", "Sixteen Threads"]),
    ) # type: ignore
    var_prop8: IntProperty(
        name="Spatial Overlap",
        default=24,
        min=0, 
        max=256, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_unsharp_octave {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop7},{self.var_prop8},{self.var_prop10},50,50"

################################################################################
################################################################################

class GMIC_FDetail_sharpenrichardsonlucy(GMICBaseNode):
    """Sharpen [Richardson-Lucy] by Author: Jérôme Boulanger. Latest Update: 2013/29/03."""
    # fx_unsharp_richardsonlucy

    bl_idname = "FDetail_sharpenrichardsonlucy"
    bl_label = "Sharpen [Richardson-Lucy]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Sigma",
        default=1.0,
        min=0.5, 
        max=10.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Iterations",
        default=10,
        min=1, 
        max=100, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Blur",
        default="1",
        items=create_enum(["Exponential", "Gaussian"]),
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Cut",
        default=1,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_unsharp_richardsonlucy {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FDetail_sharpenshockfilters(GMICBaseNode):
    """Sharpen [Shock Filters] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_sharpen_shock

    bl_idname = "FDetail_sharpenshockfilters"
    bl_label = "Sharpen [Shock Filters]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=150.0,
        min=1.0, 
        max=400.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Edge Threshold",
        default=0.1,
        min=0.0, 
        max=0.7, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Gradient Smoothness",
        default=0.8,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Tensor Smoothness",
        default=1.1,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Iterations",
        default=1,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_sharpen_shock {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FDetail_sharpentexture(GMICBaseNode):
    """Sharpen [Texture] by Author: David Tschumperlé. Latest Update: 2016/20/09."""
    # fx_sharpen_texture

    bl_idname = "FDetail_sharpentexture"
    bl_label = "Sharpen [Texture]"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Strength",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Radius",
        default=4.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Channel(s)",
        default="16",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_sharpen_texture {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FDetail_sharpentones(GMICBaseNode):
    """Sharpen [Tones] by Author : Garagecoder. Latest update : 2015/09/28."""
    # gcd_sharpen_tones

    bl_idname = "FDetail_sharpentones"
    bl_label = "Sharpen [Tones]"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop2: FloatProperty(
        name="Amount",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Centre",
        default=128,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Values",
        default="0",
        items=create_enum(["cut", "normalize luma"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"gcd_sharpen_tones {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FDetail_sharpenunsharpmask(GMICBaseNode):
    """Sharpen [Unsharp Mask] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_unsharp

    bl_idname = "FDetail_sharpenunsharpmask"
    bl_label = "Sharpen [Unsharp Mask]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop10", "var_prop12"]

    var_prop0: EnumProperty(
        name="Sharpening Type",
        default="1",
        items=create_enum(["Gaussian", "Bilateral"]),
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Spatial Radius",
        default=1.25,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Bilateral Radius",
        default=10.0,
        min=0.0, 
        max=60.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Amount",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Threshold",
        default=0.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Darkness Level",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Lightness Level",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Iterations",
        default=1,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop8: BoolProperty(
        name="Negative Effect",
        default=0,
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
        return f"fx_unsharp {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{int(self.var_prop8)},{self.var_prop10},{self.var_prop12},50,50"

################################################################################
################################################################################

class GMIC_FDetail_sharpenwhiten(GMICBaseNode):
    """Sharpen [Whiten] by Author : Jérôme Boulanger. Latest update: 2013/06/01."""
    # jeje_whiten_frequency

    bl_idname = "FDetail_sharpenwhiten"
    bl_label = "Sharpen [Whiten]"

    node_props = ["var_prop0", "var_prop1", "var_prop3"]

    var_prop0: FloatProperty(
        name="Alpha",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: BoolProperty(
        name="Cut",
        default=0,
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_whiten_frequency {self.var_prop0},{int(self.var_prop1)},{self.var_prop3}"

################################################################################
################################################################################

class GMIC_FDetail_simplelocalcontrast(GMICBaseNode):
    """Simple Local Contrast by Author: Iain Fergusson - update 18 April 2014 - added parallel processing and luminance mask"""
    # simplelocalcontrast_p

    bl_idname = "FDetail_simplelocalcontrast"
    bl_label = "Simple Local Contrast"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop14"]

    var_prop0: FloatProperty(
        name="Edge Sensitivity",
        default=16.0,
        min=0.0, 
        max=25.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Iterations",
        default=2,
        min=1, 
        max=5, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Paint Effect",
        default=0.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Channels",
        default="1",
        items=create_enum(["Colour", "Luminance Only"]),
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Pre-Gamma",
        default=1.0,
        min=.1, 
        max=5.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Post-Gamma",
        default=1.0,
        min=.1, 
        max=5.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Blacks",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Dark Grey",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Mid Grey",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Light Grey",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Whites",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop14: EnumProperty(
        name="Parallel Processing",
        default="0",
        items=create_enum(["Auto", "None"]),
    ) # type: ignore

    def create_command(self):
        return f"simplelocalcontrast_p {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop14}"

################################################################################
################################################################################

class GMIC_FDetail_spotify(GMICBaseNode):
    """Spotify by Author : Jérôme Boulanger. Latest update: 2013/12/16."""
    # jeje_spotify

    bl_idname = "FDetail_spotify"
    bl_label = "Spotify"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Scale",
        default=1.0,
        min=0.75, 
        max=10.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Iteration",
        default=1,
        min=1, 
        max=50, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Gamma",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Cut",
        default=1,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [all]", "RGB [all]", "RGB [red]", "RGB [green]", "RGB [blue]", "RGBA [alpha]", "Linear RGB [all]", "Linear RGB [red]", "Linear RGB [green]", "Linear RGB [blue]", "YCbCr [luminance]", "YCbCr [blue-red chrominances]", "YCbCr [blue chrominance]", "YCbCr [red chrominance]", "YCbCr [green chrominance]", "Lab [lightness]", "Lab [ab-chrominances]", "Lab [a-chrominance]", "Lab [b-chrominance]", "Lch [ch-chrominances]", "Lch [c-chrominance]", "Lch [h-chrominance]", "HSV [hue]", "HSV [saturation]", "HSV [value]", "HSI [intensity]", "HSL [lightness]", "CMYK [cyan]", "CMYK [magenta]", "CMYK [yellow]", "CMYK [key]", "YIQ [luma]", "YIQ [chromas]"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_spotify {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{self.var_prop5},{self.var_prop7}"

################################################################################
################################################################################

class GMIC_FDetail_texture(GMICBaseNode):
    """Texture by &lt;strong&gt;Enhance texture with detail scales. Filter by &lt;a href&#x3D;&quot;https://discuss.pixls.us/u/afre&quot;&gt;afre&lt;/a&gt; 2020 Aug10-18.&lt;/strong&gt; """
    # afre_texture

    bl_idname = "FDetail_texture"
    bl_label = "Texture"

    node_props = ["var_prop2", "var_prop3", "var_prop4"]

    var_prop2: IntProperty(
        name="Coarse",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Medium",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Fine",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore

    def create_command(self):
        return f"afre_texture {self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FDetail_textureenhance(GMICBaseNode):
    """Texture Enhance by Update: 4 March 2013 - Different halo protection method, added option to reduce noise, faster."""
    # iain_texture_enhance_p

    bl_idname = "FDetail_textureenhance"
    bl_label = "Texture Enhance"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop8"]

    var_prop0: IntProperty(
        name="Radius",
        default=2,
        min=2, 
        max=11, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Strength",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Reduce Halos",
        default=30.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Reduce Noise",
        default=0.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [all]", "RGB [all]", "RGB [red]", "RGB [green]", "RGB [blue]", "RGBA [alpha]", "Linear RGB [all]", "Linear RGB [red]", "Linear RGB [green]", "Linear RGB [blue]", "YCbCr [luminance]", "YCbCr [blue-red chrominances]", "YCbCr [blue chrominance]", "YCbCr [red chrominance]", "YCbCr [green chrominance]", "Lab [lightness]", "Lab [ab-chrominances]", "Lab [a-chrominance]", "Lab [b-chrominance]", "Lch [ch-chrominances]", "Lch [c-chrominance]", "Lch [h-chrominance]", "HSV [hue]", "HSV [saturation]", "HSV [value]", "HSI [intensity]", "HSL [lightness]", "CMYK [cyan]", "CMYK [magenta]", "CMYK [yellow]", "CMYK [key]"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Parallel Processing",
        default="0",
        items=create_enum(["Auto", "Off"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"iain_texture_enhance_p {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},{self.var_prop8}"

################################################################################
################################################################################

class GMIC_FDetail_toneenhance(GMICBaseNode):
    """Tone Enhance by Author : Garagecoder. Latest update : 2017/01/03."""
    # gcd_tone_enhance

    bl_idname = "FDetail_toneenhance"
    bl_label = "Tone Enhance"

    node_props = ["var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop11", "var_prop12", "var_prop13", "var_prop16", "var_prop17", "var_prop20", "var_prop22", "var_prop23", "var_prop24"]

    var_prop3: FloatProperty(
        name="Detail",
        default=0.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Gamma",
        default=1.0,
        min=0.2, 
        max=1.8, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Detail",
        default=0.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Gamma",
        default=1.0,
        min=0.2, 
        max=1.8, 
    ) # type: ignore
    var_prop11: IntProperty(
        name="Centre",
        default=128,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Detail",
        default=0.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Gamma",
        default=1.0,
        min=0.2, 
        max=1.8, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Boost",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Smooth",
        default=0.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop20: IntProperty(
        name="Smooth",
        default=0,
        min=0, 
        max=20, 
    ) # type: ignore
    var_prop22: EnumProperty(
        name="Channels",
        default="4",
        items=create_enum(["HSI", "HSV", "Lab", "Linear RGB", "RGB", "YCbCr"]),
    ) # type: ignore
    var_prop23: EnumProperty(
        name="Values",
        default="0",
        items=create_enum(["cut", "normalize"]),
    ) # type: ignore
    var_prop24: BoolProperty(
        name="Color Median",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"gcd_tone_enhance {self.var_prop3},{self.var_prop4},{self.var_prop7},{self.var_prop8},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop16},{self.var_prop17},{self.var_prop20},{self.var_prop22},{self.var_prop23},{int(self.var_prop24)}"

################################################################################
################################################################################

class GMIC_FDetail_tonemapping(GMICBaseNode):
    """Tone Mapping by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_map_tones

    bl_idname = "FDetail_tonemapping"
    bl_label = "Tone Mapping"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Threshold",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Gamma",
        default=0.7,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=0.1,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Iterations",
        default=30,
        min=0, 
        max=500, 
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
        return f"fx_map_tones {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FDetail_tonemappingfast(GMICBaseNode):
    """Tone Mapping [Fast] by Authors: Paul Nasca and David Tschumperlé. Latest Update: 2011/10/06."""
    # fx_map_tones_fast

    bl_idname = "FDetail_tonemappingfast"
    bl_label = "Tone Mapping [Fast]"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Radius",
        default=3.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Power",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Channel(s)",
        default="11",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_map_tones_fast {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FDetail_yageffect(GMICBaseNode):
    """YAG Effect by Author : Arto Huotari. Latest update : 2013/09/28."""
    # fx_yag_soften

    bl_idname = "FDetail_yageffect"
    bl_label = "YAG Effect"

    node_props = ["var_prop0", "var_prop1", "var_prop3"]

    var_prop0: FloatProperty(
        name="Darken",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Soften",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_yag_soften {self.var_prop0},{self.var_prop1},{self.var_prop3}"

################################################################################
################################################################################

node_classes = [
    GMIC_FDetail_constrainedsharpen, GMIC_FDetail_dcpdehaze, GMIC_FDetail_detailsequalizer, GMIC_FDetail_dynamicrangeincrease, GMIC_FDetail_easyskinretouch, GMIC_FDetail_embossrelief, GMIC_FDetail_equalizelocalhistograms, GMIC_FDetail_freakydetails, GMIC_FDetail_highpass, GMIC_FDetail_localcontrastenhancement, GMIC_FDetail_localnormalization, GMIC_FDetail_localprocessing, GMIC_FDetail_localvariancenormalization, GMIC_FDetail_magicdetails, GMIC_FDetail_makeup, GMIC_FDetail_maskcreator, GMIC_FDetail_mightydetails, GMIC_FDetail_portraitretouching, GMIC_FDetail_pyramidprocessing, GMIC_FDetail_quicktonemap, GMIC_FDetail_sharpendeblur, GMIC_FDetail_sharpengoldmeinel, GMIC_FDetail_sharpengradient, GMIC_FDetail_sharpenhessian, GMIC_FDetail_sharpeninversediffusion, GMIC_FDetail_sharpenmultiscale, GMIC_FDetail_sharpenoctavesharpening, GMIC_FDetail_sharpenrichardsonlucy, GMIC_FDetail_sharpenshockfilters, GMIC_FDetail_sharpentexture, GMIC_FDetail_sharpentones, GMIC_FDetail_sharpenunsharpmask, GMIC_FDetail_sharpenwhiten, GMIC_FDetail_simplelocalcontrast, GMIC_FDetail_spotify, GMIC_FDetail_texture, GMIC_FDetail_textureenhance, GMIC_FDetail_toneenhance, GMIC_FDetail_tonemapping, GMIC_FDetail_tonemappingfast, GMIC_FDetail_yageffect
]

################################################################################