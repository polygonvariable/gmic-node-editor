from bpy.props import ( BoolProperty, FloatProperty, EnumProperty, StringProperty )

from ..base.node import GMICBaseNode, create_enum
    
class FColor_ApplyExternalCLUT(GMICBaseNode):
    """Apply External CLUT by David Tschumperlé"""
    # fx_apply_haldclut 2,"",100,0,0,0,0,0,0,0,50,50

    bl_idname = "GMIC_FColor_ApplyExternalCLUT"
    bl_label = "Apply External CLUT"

    node_props = ["filename", "strength", "brightness", "constrast", "gamma", "hue", "saturation", "normalize"]

    filename: StringProperty(name="File", default="", subtype="FILE_PATH") # type: ignore
    strength: FloatProperty(name="Strength", default=100.0, min=0.0, max=100.0) # type: ignore
    brightness: FloatProperty(name="Brightness", default=0.0, min=-100.0, max=100.0) # type: ignore
    constrast: FloatProperty(name="Constrast", default=0.0, min=-100.0, max=100.0) # type: ignore
    gamma: FloatProperty(name="Gamma", default=0.0, min=-100.0, max=100.0) # type: ignore
    hue: FloatProperty(name="Hue", default=0.0, min=-100.0, max=100.0) # type: ignore
    saturation: FloatProperty(name="Saturation", default=0.0, min=-100.0, max=100.0) # type: ignore
    normalize: EnumProperty(
        name="Normalize",
        items=create_enum(["None", "Pre", "Post", "Both"]),
        default="0"
    ) # type: ignore

    def create_command(self):
        return "fx_apply_haldclut 2,\"{0}\",{1},{2},{3},{4},{5},{6},{7},0,50,50".format(
            self.filename,
            self.strength,
            self.brightness,
            self.constrast,
            self.gamma,
            self.hue,
            self.saturation,
            self.normalize
        )

class FColor_BasicAdjustments(GMICBaseNode):
    """Basic Adjustments by David Tschumperlé"""
    # fx_adjust_colors 0,0,0,0,0,0,50,50

    bl_idname = "GMIC_FColor_BasicAdjustments"
    bl_label = "Basic Adjustments"

    node_props = ["brightness", "constrast", "gamma", "hue", "saturation"]

    brightness: FloatProperty(name="Brightness", default=0.0, min=-100.0, max=100.0) # type: ignore
    constrast: FloatProperty(name="Constrast", default=0.0, min=-100.0, max=100.0) # type: ignore
    gamma: FloatProperty(name="Gamma", default=0.0, min=-100.0, max=100.0) # type: ignore
    hue: FloatProperty(name="Hue", default=0.0, min=-100.0, max=100.0) # type: ignore
    saturation: FloatProperty(name="Saturation", default=0.0, min=-100.0, max=100.0) # type: ignore

    def create_command(self):
        return "fx_adjust_colors {0},{1},{2},{3},{4},0,50,50".format(
            self.brightness,
            self.constrast,
            self.gamma,
            self.hue,
            self.saturation
        )

class FColor_BoostChromaticity(GMICBaseNode):
    """Boost Chromaticity by David Tschumperlé"""
    # fx_boost_chroma 50,0,0,50,50

    bl_idname = "GMIC_FColor_BoostChromaticity"
    bl_label = "Boost Chromaticity"

    node_props = ["amplitude", "color"]

    amplitude: FloatProperty(name="Amplitude", default=50.0, min=0.0, max=100.0) # type: ignore
    color: EnumProperty(
        name="Color Space",
        items=create_enum(["YCbCr Distinct", "YCbCr Mixed", "Lab Distinct", "Lab Mixed"]),
        default="0"
    ) # type: ignore
    
    def create_command(self):
        return "fx_boost_chroma {0},{1},0,50,50".format(
            self.amplitude,
            self.color
        )

class FColor_BoostFade(GMICBaseNode):
    """Boost Fade by David Tschumperlé"""
    # fx_boost_fade 5,0,0,50,50

    bl_idname = "GMIC_FColor_BoostFade"
    bl_label = "Boost Fade"

    node_props = ["amplitude", "chromaticity"]

    amplitude: FloatProperty(name="Amplitude", default=5.0, min=0.0, max=10.0) # type: ignore
    chromaticity: EnumProperty(
        name="Chromaticity",
        items=create_enum(["YCbCr", "Lab"]),
        default="0"
    ) # type: ignore
    
    def create_command(self):
        return "fx_boost_fade {0},{1},0,50,50".format(
            self.amplitude,
            self.chromaticity
        )

class FColor_Brightness(GMICBaseNode):
    """Brightness by afre"""
    # afre_brightness 50,0

    bl_idname = "GMIC_FColor_Brightness"
    bl_label = "Brightness"

    node_props = ["amount", "smooth"]

    amount: FloatProperty(name="Amount", default=50.0, min=-300.0, max=300.0) # type: ignore
    smooth: FloatProperty(name="Smooth", default=0.0, min=0.0, max=50.0) # type: ignore
    
    def create_command(self):
        return "afre_brightness {0},{1}".format(
            self.amount,
            self.smooth
        )


classes = [
    FColor_ApplyExternalCLUT,
    FColor_BasicAdjustments,
    FColor_BoostChromaticity,
    FColor_BoostFade,
    FColor_Brightness
]