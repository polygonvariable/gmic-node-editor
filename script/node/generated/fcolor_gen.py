from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FColor_channelprocessing(GMICBaseNode):
    """Channel Processing by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_channel_processing

    bl_idname = "FColor_channelprocessing"
    bl_label = "Channel Processing"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop11", "var_prop12", "var_prop14", "var_prop16"]

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
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Cut & Normalize", "Normalize", "Threshold"]),
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Low Value",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="High Value",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Quantization",
        default=256,
        min=1, 
        max=256, 
    ) # type: ignore
    var_prop8: BoolProperty(
        name="Equalization",
        default=0,
    ) # type: ignore
    var_prop9: BoolProperty(
        name="Negation",
        default=0,
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Tones Range",
        default="0",
        items=create_enum(["All tones", "Shadows", "Mid-Tones", "Highlights"]),
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Tones Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop14: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop16: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_channel_processing {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{int(self.var_prop8)},{int(self.var_prop9)},{self.var_prop11},{self.var_prop12},{self.var_prop14},{self.var_prop16},50,50"

################################################################################
################################################################################

class GMIC_FColor_cmyktone(GMICBaseNode):
    """CMYK Tone by Author : Iain Fergusson. Update: 4 March 2014 - Added parallel processing option"""
    # iain_cmyk_tone_p

    bl_idname = "FColor_cmyktone"
    bl_label = "CMYK Tone"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop7", "var_prop9", "var_prop10", "var_prop11", "var_prop13", "var_prop14", "var_prop15", "var_prop18", "var_prop19", "var_prop20", "var_prop22", "var_prop23", "var_prop24", "var_prop26", "var_prop27", "var_prop28", "var_prop30", "var_prop31", "var_prop32", "var_prop35", "var_prop36", "var_prop37", "var_prop39", "var_prop40", "var_prop41", "var_prop43", "var_prop44", "var_prop45", "var_prop47", "var_prop48", "var_prop49", "var_prop52", "var_prop53", "var_prop54", "var_prop56", "var_prop57", "var_prop58", "var_prop60", "var_prop61", "var_prop62", "var_prop64", "var_prop65", "var_prop66", "var_prop69", "var_prop70", "var_prop71", "var_prop72", "var_prop73", "var_prop75", "var_prop77"]

    var_prop1: IntProperty(
        name="A Lot of Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Some Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Little Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="A Lot of Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop6: IntProperty(
        name="Some Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Little Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop9: IntProperty(
        name="A Lot of Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop10: IntProperty(
        name="Some Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop11: IntProperty(
        name="Little Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop13: IntProperty(
        name="A Lot of Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop14: IntProperty(
        name="Some Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop15: IntProperty(
        name="Little Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop18: IntProperty(
        name="A Lot of Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop19: IntProperty(
        name="Some Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop20: IntProperty(
        name="Little Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop22: IntProperty(
        name="A Lot of Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop23: IntProperty(
        name="Some Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop24: IntProperty(
        name="Little Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop26: IntProperty(
        name="A Lot of Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop27: IntProperty(
        name="Some Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop28: IntProperty(
        name="Little Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop30: IntProperty(
        name="A Lot of Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop31: IntProperty(
        name="Some Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop32: IntProperty(
        name="Little Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop35: IntProperty(
        name="A Lot of Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop36: IntProperty(
        name="Some Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop37: IntProperty(
        name="Little Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop39: IntProperty(
        name="A Lot of Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop40: IntProperty(
        name="Some Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop41: IntProperty(
        name="Little Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop43: IntProperty(
        name="A Lot of Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop44: IntProperty(
        name="Some Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop45: IntProperty(
        name="Little Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop47: IntProperty(
        name="A Lot of Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop48: IntProperty(
        name="Some Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop49: IntProperty(
        name="Little Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop52: IntProperty(
        name="A Lot of Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop53: IntProperty(
        name="Some Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop54: IntProperty(
        name="Little Cyan",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop56: IntProperty(
        name="A Lot of Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop57: IntProperty(
        name="Some Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop58: IntProperty(
        name="Little Magenta",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop60: IntProperty(
        name="A Lot of Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop61: IntProperty(
        name="Some Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop62: IntProperty(
        name="Little Yellow",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop64: IntProperty(
        name="A Lot of Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop65: IntProperty(
        name="Some Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop66: IntProperty(
        name="Little Key",
        default=0,
        min=-255, 
        max=255, 
    ) # type: ignore
    var_prop69: IntProperty(
        name="None",
        default=255,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop70: IntProperty(
        name="Little",
        default=255,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop71: IntProperty(
        name="Some",
        default=255,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop72: IntProperty(
        name="Much",
        default=255,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop73: IntProperty(
        name="Most",
        default=255,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop75: EnumProperty(
        name="Output",
        default="0",
        items=create_enum(["Perserve Luminance", "Clip CMYK", "Clip RGB", "Scale CMYK", "Scale RGB"]),
    ) # type: ignore
    var_prop77: EnumProperty(
        name="Parallel Processing",
        default="0",
        items=create_enum(["Auto", "Off"]),
    ) # type: ignore

    def create_command(self):
        return f"iain_cmyk_tone_p {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop18},{self.var_prop19},{self.var_prop20},{self.var_prop22},{self.var_prop23},{self.var_prop24},{self.var_prop26},{self.var_prop27},{self.var_prop28},{self.var_prop30},{self.var_prop31},{self.var_prop32},{self.var_prop35},{self.var_prop36},{self.var_prop37},{self.var_prop39},{self.var_prop40},{self.var_prop41},{self.var_prop43},{self.var_prop44},{self.var_prop45},{self.var_prop47},{self.var_prop48},{self.var_prop49},{self.var_prop52},{self.var_prop53},{self.var_prop54},{self.var_prop56},{self.var_prop57},{self.var_prop58},{self.var_prop60},{self.var_prop61},{self.var_prop62},{self.var_prop64},{self.var_prop65},{self.var_prop66},{self.var_prop69},{self.var_prop70},{self.var_prop71},{self.var_prop72},{self.var_prop73},{self.var_prop75},{self.var_prop77}"

################################################################################
################################################################################

class GMIC_FColor_colorbalance(GMICBaseNode):
    """Color Balance by Author: David Tschumperlé. Latest Update: 2011/01/07."""
    # fx_balance_gamma

    bl_idname = "FColor_colorbalance"
    bl_label = "Color Balance"

    node_props = ["var_prop0", "var_prop1", "var_prop3"]

    var_prop0: FloatVectorProperty(
        name="Neutral Color",
        default=(0.5019607843137255,0.5019607843137255,0.5019607843137255),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop1: BoolProperty(
        name="Stretch Colors",
        default=1,
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_balance_gamma {self.var_prop0[0]*255},{self.var_prop0[1]*255},{self.var_prop0[2]*255},255,{int(self.var_prop1)},{self.var_prop3},50,50"

################################################################################
################################################################################

class GMIC_FColor_colorblindness(GMICBaseNode):
    """Color Blindness by Author: David Tschumperlé. Latest Update: 2016/20/04."""
    # colorblind

    bl_idname = "FColor_colorblindness"
    bl_label = "Color Blindness"

    node_props = ["var_prop0", "var_prop2"]

    var_prop0: EnumProperty(
        name="Blindness Type",
        default="0",
        items=create_enum(["Protanopia", "Protanomaly", "Deuteranopia", "Deuteranomaly", "Tritanopia", "Tritanomaly", "Achromatopsia", "Achromatomaly"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"colorblind {self.var_prop0},{self.var_prop2},50,50"

################################################################################
################################################################################

class GMIC_FColor_colorgrading(GMICBaseNode):
    """Color Grading by Author: John Lakkas. Latest update: 17/03/2015."""
    # jl_colorgrading

    bl_idname = "FColor_colorgrading"
    bl_label = "Color Grading"

    node_props = ["var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop17", "var_prop18", "var_prop20", "var_prop21", "var_prop22", "var_prop23", "var_prop24", "var_prop25", "var_prop26", "var_prop27", "var_prop28", "var_prop29", "var_prop32", "var_prop33", "var_prop34", "var_prop36"]

    var_prop3: FloatProperty(
        name="HDR Effect (Tone Map)",
        default=0.,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Cool / Warm",
        default=0,
        min=-50, 
        max=50, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Saturation",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Saturation Channel Gamma",
        default=1.0,
        min=0.1, 
        max=3.0, 
    ) # type: ignore
    var_prop9: IntProperty(
        name="S-Curve Contrast",
        default=0,
        min=-30, 
        max=30, 
    ) # type: ignore
    var_prop10: IntProperty(
        name="Shadows",
        default=0,
        min=-50, 
        max=50, 
    ) # type: ignore
    var_prop11: IntProperty(
        name="Highlights",
        default=0,
        min=-50, 
        max=50, 
    ) # type: ignore
    var_prop12: IntProperty(
        name="Blacks",
        default=0,
        min=0, 
        max=50, 
    ) # type: ignore
    var_prop13: IntProperty(
        name="Brightness",
        default=0,
        min=-50, 
        max=50, 
    ) # type: ignore
    var_prop14: IntProperty(
        name="Contrast",
        default=0,
        min=-50, 
        max=50, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Gamma",
        default=1.0,
        min=0.1, 
        max=3.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Clarity",
        default=0.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Local Contrast Enhance",
        default=0.0,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop20: BoolProperty(
        name="Color Grading",
        default=0,
    ) # type: ignore
    var_prop21: IntProperty(
        name="Highlights Color Intensity",
        default=70,
        min=0, 
        max=130, 
    ) # type: ignore
    var_prop22: IntProperty(
        name="Highlights Hue",
        default=0,
        min=0, 
        max=360, 
    ) # type: ignore
    var_prop23: IntProperty(
        name="Highlights Brightness",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop24: IntProperty(
        name="Midtones Color Intensity",
        default=0,
        min=0, 
        max=130, 
    ) # type: ignore
    var_prop25: IntProperty(
        name="Midtones Hue",
        default=0,
        min=0, 
        max=360, 
    ) # type: ignore
    var_prop26: IntProperty(
        name="Midtones Brightness",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop27: IntProperty(
        name="Shadows Color Intensity",
        default=70,
        min=0, 
        max=130, 
    ) # type: ignore
    var_prop28: IntProperty(
        name="Shadows Hue Shift",
        default=180,
        min=0, 
        max=360, 
    ) # type: ignore
    var_prop29: IntProperty(
        name="Shadows Brightness",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop32: FloatProperty(
        name="Output Saturation",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop33: FloatProperty(
        name="Output Sharpening",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop34: FloatProperty(
        name="Output Chroma NR",
        default=0.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop36: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jl_colorgrading {self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop17},{self.var_prop18},{int(self.var_prop20)},{self.var_prop21},{self.var_prop22},{self.var_prop23},{self.var_prop24},{self.var_prop25},{self.var_prop26},{self.var_prop27},{self.var_prop28},{self.var_prop29},{self.var_prop32},{self.var_prop33},{self.var_prop34},{self.var_prop36}"

################################################################################
################################################################################

class GMIC_FColor_colorpresets(GMICBaseNode):
    """Color Presets by Author: David Tschumperlé. Latest Update: 2023/06/01."""
    # fx_color_presets

    bl_idname = "FColor_colorpresets"
    bl_label = "Color Presets"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop19", "var_prop20", "var_prop21", "var_prop22", "var_prop23", "var_prop24", "var_prop25", "var_prop26", "var_prop27", "var_prop28", "var_prop29", "var_prop30", "var_prop32", "var_prop33", "var_prop34", "var_prop35", "var_prop36", "var_prop37", "var_prop38", "var_prop40"]

    var_prop0: EnumProperty(
        name="LUTs Pack",
        default="21",
        items=create_enum(["Abigail Gonzalez (21)", "Alex Jordan (81)", "Berat (10)", "Cinematic (8)", "Cinematic Travel (29)", "Creative Pack (33)", "EditingCorp (60)", "Eric Ellerbrock (14)", "FilterGrade Cinematic (8)", "Hollywood Movies (74)", "InAvision (15)", "J.T. Semple (14)", "Kyler Holland (10)", "Lutify.Me (7)", "Michael Ezra (2)", "Moviz (48)", "Ohad Peretz (7)", "Olivio Sarikas (19)", "ON1 Photography (90)", "PictureFX (25)", "Pixelmator (45)", "PIXLS.US (31)", "Purple11 (12)", "RocketStock (35)", "Shamoon Abbasi (25)", "SmallHD Movie Look (7)", "Todd Blankenship (13)", "Youssef Hossam (5)", "Others (69)"]),
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Abigail Gonzalez",
        default="1",
        items=create_enum(["All [Collage]", "None", "Blade Runner", "Blue House", "Blue Ice", "Caribe", "Cinema", "Cinema 2", "Cinema 3", "Cinema 4", "Cinema 5", "Cinema Noir", "Cinematic for Flog", "Day4Nite", "Eterna for Flog", "Filmic", "Fuji HDR", "Golden Gate", "Matrix", "Monochrome 1", "Monochrome 2", "Old West", "Science Fiction"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Alex Jordan",
        default="1",
        items=create_enum(["All [Collage]", "None", "Action Magenta 01", "Action Red 01", "Adventure 1453", "Aggressive Highlights Recovery 5", "Bleech Bypass Green", "Bleech Bypass Yellow 01", "Blue Dark", "Blue Shadows 01", "Bright Green 01", "Brownish", "Colorful 0209", "Conflict 01", "Contrast with Highlights Protection", "Contrasty Afternoon", "Contrasty Green", "Cross Process CP 130", "Cross Process CP 14", "Cross Process CP 15", "Cross Process CP 16", "Cross Process CP 18", "Cross Process CP 3", "Cross Process CP 4", "Cross Process CP 6", "Dark Green 02", "Dark Green 1", "Dark Place 01", "Dream 1", "Dream 85", "Faded Retro 01", "Faded Retro 02", "Film 0987", "Film 9879", "Film Highlight Contrast", "Flat 30", "Green 2025", "Green Action", "Green Afternoon", "Green Conflict", "Green Day 01", "Green Day 02", "Green G09", "Green Indoor", "Green Light", "Harsh Day", "Harsh Sunset", "Highlights Protection", "Indoor Blue", "Low Contrast Blue", "Low Key 01", "Magenta Day", "Magenta Day 01", "Magenta Dream", "Memories", "Moonlight 01", "Mostly Blue", "Muted 01", "Night 01", "Only Red", "Only Red and Blue", "Operation Yellow", "Orange Dark 4", "Orange Dark 7", "Orange Dark Look", "Orange Underexposed", "Protect Highlights 01", "Red Afternoon 01", "Red Day 01", "Red Dream 01", "Retro Brown 01", "Retro Magenta 01", "Retro Yellow 01", "Saturated Blue", "Smart Contrast", "Subtle Blue", "Subtle Green", "Yellow 55B", "Yellow Film 01"]),
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Berat",
        default="1",
        items=create_enum(["All [Collage]", "None", "Brown BM", "Cine Blue", "Cine BM4k", "Golden Time", "Green and Orange", "Monochrome", "Sevsuz", "Sunlight Love", "Western", "Western Lut 2"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Cinematic",
        default="1",
        items=create_enum(["All [Collage]", "None", "Deep", "Dimension", "Enchanted", "Flavin", "Frosted", "Shine", "Ultra Water", "Wipe"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Cinematic Travel",
        default="1",
        items=create_enum(["All [Collage]", "None", "Blue Cold Fade", "Bright Teal Orange", "Bright Warm", "Clear Teal Fade", "Cold Clear Blue", "Cold Clear Blue 1", "Deep Blue", "Deep Dark Warm", "Deep High Contrast", "Deep Teal Fade", "Deep Warm Fade", "Faded Green", "Greenish Contrasty", "Greenish Fade", "Greenish Fade 1", "Hard Teal Orange", "Neutral Teal Orange", "Neutral Warm Fade", "Smooth Clear", "Smooth Green Orange", "Smooth Teal Orange", "Teal Fade", "Very Warm Greenish", "Warm Dark Contrasty", "Warm Fade", "Warm Fade 1", "Warm Neutral", "Warm Sunset Red", "Warm Teal"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Creative Pack",
        default="1",
        items=create_enum(["All [Collage]", "None", "Anime", "Bleach Bypass 1", "Bleach Bypass 2", "Bleach Bypass 3", "Bleach Bypass 4", "Candle Light", "Color Negative", "Crisp Warm", "Crip Winter", "Drop Blues", "Edgy Ember", "Fall Colors", "Foggy Night", "Futuristic Bleak 1", "Futuristic Bleak 2", "Futuristic Bleak 3", "Futuristic Bleak 4", "Horror Blue", "Late Sunset", "Moonlight", "Night From Day", "Red Blue Yellow", "Smokey", "Soft Warming", "Teal Magenta Gold", "Teal Orange", "Teal Orange 1", "Teal Orange 2", "Teal Orange 3", "Tension Green 1", "Tension Green 2", "Tension Green 3", "Tension Green 4"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="EditingCorp",
        default="1",
        items=create_enum(["All [Collage]", "None", "Ampio", "Asistas", "Atusa", "Basuco", "Beati", "Bisogno", "Boyado", "Calidum", "Colore", "Convold", "Cosa", "Culor", "Dimmer", "Ensaya", "Falua", "Farkling", "Fatos", "Fezzle", "Filo", "Foresta", "Huesio", "Husmes", "Huyan", "Ideo", "Jarklin", "Lavark", "Levex", "Litore", "Loro", "Lotta", "Maesky", "Mercato", "Molti", "Motus", "Mucca", "Nigrum", "Onda", "Padre", "Partia", "Perso", "Picola", "Randas", "Satid", "Scala", "Scrittle", "Seges", "Selor", "Sensum", "Sino", "Soldi", "Strano", "Stringa", "Tirare", "Tutto", "Upglow", "Valize", "Valsky", "Vita", "Vubes", "Wavefire"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Eric Ellerbrock",
        default="1",
        items=create_enum(["All [Collage]", "None", "Avalanche", "Black Star", "Helios", "Hydracore", "Hypnosis", "Killstreak", "Nemesis", "Night Blade 4", "Paladin", "Seringe 4", "Serpent", "Terra 4", "Victory", "Yellowstone"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="FilterGrade Cinematic",
        default="1",
        items=create_enum(["All [Collage]", "None", "Cine Basic", "Cine Bright", "Cine Cold", "Cine Drama", "Cine Teal Orange 1", "Cine Teal Orange 2", "Cine Vibrant", "Cine Warm"]),
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Hollywood Movies",
        default="1",
        items=create_enum(["All [Collage]", "None", "12 Years a Slave", "1917", "Ad Astra", "Aladdin", "Ant-Man", "Aquaman", "Avengers Endgame", "Baby Driver", "Bad Boys for Life", "Beauty and the Beast", "Black Panther", "Bohemian Rhapsody", "Bombshell", "Captain Marvel", "City of God", "Creed 2", "Doctor Strange", "Dunkirk", "Fight Club", "Ford v Ferrari", "Green Book", "Greyhound", "Inception", "I Tonya", "Jojo Rabbit", "Joker ", "Jumanji The Next Level", "Jurassic World Fallen Kingdom", "Justice League", "Kingsman The Golden Circle", "Knives Out", "La La Land", "Little Women", "Logan", "Mad Max Fury Road", "Marriage Story", "Moonlight", "Mother!", "No Time to Die", "Once Upon a Time in Hollywood", "Parasite", "Pirates of the Caribbean", "Rocketman", "Separation", "Sicario", "Spider-Man Far From Home", "Spotlight", "Star Wars The Rise of Skywalker", "Sully", "TENET", "The Darkest Hour", "The Dark Knight", "The Gentelmen", "The Grand Budapest Hotel", "The Hurt Locker", "The Irishman", "The Lighthouse", "The Lobster", "The Martian", "The Revenant", "The Shape of Water", "The Social Network", "The Two Popes", "The Way Back", "Thor Ragnarok", "Top Gun Maverick", "Uncut Gems", "Underwater", "Venom", "War for the Planet of the Apes", "Wolf of Wall Street", "Wonder Woman", "X-Men Dark Phoenix", "Zombieland Double Tap"]),
    ) # type: ignore
    var_prop11: EnumProperty(
        name="InAvision",
        default="1",
        items=create_enum(["All [Collage]", "None", "7Drk21", "BC Darkum", "Brown Mobster", "Cold Ice", "Dark Man X", "Film GB-19", "Formula B", "Gremerta", "Hitman", "J. Wick 21", "London Nights", "Louetta", "Nightlife", "VFB 21", "Vintage Mob"]),
    ) # type: ignore
    var_prop12: EnumProperty(
        name="J.T. Semple",
        default="1",
        items=create_enum(["All [Collage]", "None", "Bright Green", "Crisp Romance", "Crushin", "Frosted Beach Picnic", "Just Peachy", "Late Afternoon Wanderlust", "Lush Green Summer", "Magenta Coffee", "Minimalist Caffeination", "Mystic Purple Sunset", "Nostalgia Honey", "Spring Morning", "Toasted Garden", "Winter Lighthouse"]),
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Kyler Holland",
        default="1",
        items=create_enum(["All [Collage]", "None", "KH 1", "KH 2", "KH 3", "KH 4", "KH 5", "KH 6", "KH 7", "KH 8", "KH 9", "KH 10"]),
    ) # type: ignore
    var_prop14: EnumProperty(
        name="Lutify.Me",
        default="1",
        items=create_enum(["All [Collage]", "None", "Hackmanite", "Herderite", "Heulandite", "Hiddenite", "Hilutite", "Howlite", "Hypersthene"]),
    ) # type: ignore
    var_prop15: EnumProperty(
        name="Michael Ezra",
        default="1",
        items=create_enum(["All [Collage]", "None", "Deep Skin Tones 2", "Deep Skin Tones 3"]),
    ) # type: ignore
    var_prop16: EnumProperty(
        name="Moviz",
        default="1",
        items=create_enum(["All [Collage]", "None", "Moviz 1", "Moviz 2", "Moviz 3", "Moviz 4", "Moviz 5", "Moviz 6", "Moviz 7", "Moviz 8", "Moviz 9", "Moviz 10", "Moviz 11", "Moviz 12", "Moviz 13", "Moviz 14", "Moviz 15", "Moviz 16", "Moviz 17", "Moviz 18", "Moviz 19", "Moviz 20", "Moviz 21", "Moviz 22", "Moviz 23", "Moviz 24", "Moviz 25", "Moviz 26", "Moviz 27", "Moviz 28", "Moviz 29", "Moviz 30", "Moviz 31", "Moviz 32", "Moviz 33", "Moviz 34", "Moviz 35", "Moviz 36", "Moviz 37", "Moviz 38", "Moviz 39", "Moviz 40", "Moviz 41", "Moviz 42", "Moviz 43", "Moviz 44", "Moviz 45", "Moviz 46", "Moviz 47", "Moviz 48"]),
    ) # type: ignore
    var_prop17: EnumProperty(
        name="Ohad Peretz",
        default="1",
        items=create_enum(["All [Collage]", "None", "Cold Simplicity 2", "D and O 1", "Retro Summer 3", "Subtle Yellow", "Teal Moonlight", "True Colors 8", "Vintage Warmth 1"]),
    ) # type: ignore
    var_prop18: EnumProperty(
        name="Olivio Sarikas",
        default="1",
        items=create_enum(["All [Collage]", "None", "Analog Film 1", "Atomic Pink", "Beach Aqua Orange", "Beach Faded Analog", "BW but Yellow", "City Dust", "Dark Orange Teal", "Day to Night King&#x27;s Blue", "DuoTone Blue Red", "Faded Pink-ish", "Flat Blue Moon", "Honey Light", "Infrared - Dust Pink", "Neutral Pump", "Shade King&#x27;s Ink", "Sunset Aqua Orange", "Sunset Intense Violet Blue", "Sunset Violet Mood", "Violet Taste"]),
    ) # type: ignore
    var_prop19: EnumProperty(
        name="ON1 Photography",
        default="1",
        items=create_enum(["All [Collage]", "None", "2-Strip Process", "Aqua", "Aqua and Orange Dark", "Berlin Sky", "Blues", "Black & White-1", "Black & White-2", "Black & White-3", "Black & White-4", "Black & White-5", "Black & White-6", "Black & White-7", "Black & White-8", "Black & White-9", "Black & White-10", "Chrome 01", "Cinematic-1", "Cinematic-2", "Cinematic-3", "Cinematic-4", "Cinematic-5", "Cinematic-6", "Cinematic-7", "Cinematic-8", "Cinematic-9", "Cinematic-10", "Classic Teal and Orange", "Earth Tone Boost", "Fade to Green", "Film Print 01", "Film Print 02", "French Comedy", "Green Blues", "Green Yellow", "Landscape-1", "Landscape-2", "Landscape-3", "Landscape-4", "Landscape-5", "Landscape-6", "Landscape-7", "Landscape-8", "Landscape-9", "Landscape-10", "Lifestyle & Commercial-1", "Lifestyle & Commercial-2", "Lifestyle & Commercial-3", "Lifestyle & Commercial-4", "Lifestyle & Commercial-5", "Lifestyle & Commercial-6", "Lifestyle & Commercial-7", "Lifestyle & Commercial-8", "Lifestyle & Commercial-9", "Lifestyle & Commercial-10", "Moody-1", "Moody-2", "Moody-3", "Moody-4", "Moody-5", "Moody-6", "Moody-7", "Moody-8", "Moody-9", "Moody-10", "Nature & Wildlife-1", "Nature & Wildlife-2", "Nature & Wildlife-3", "Nature & Wildlife-4", "Nature & Wildlife-5", "Nature & Wildlife-6", "Nature & Wildlife-7", "Nature & Wildlife-8", "Nature & Wildlife-9", "Nature & Wildlife-10", "Oranges", "Portrait-1", "Portrait-2", "Portrait-3", "Portrait-4", "Portrait-5", "Portrait-6", "Portrait-7", "Portrait-8", "Portrait-9", "Portrait10", "Purple", "Reds", "Reds Oranges Yellows", "Studio Skin Tone Shaper", "Vintage Chrome"]),
    ) # type: ignore
    var_prop20: EnumProperty(
        name="PictureFX",
        default="1",
        items=create_enum(["All [Collage]", "None", "AnalogFX - Anno 1870 Color", "AnalogFX - Old Style I", "AnalogFX - Old Style II", "AnalogFX - Old Style III", "AnalogFX - Sepia Color", "AnalogFX - Soft Sepia I", "AnalogFX - Soft Sepia II", "PictureFX - Faux Infrared B&W1", "PictureFX - Faux Infrared Color P2", "PictureFX - Faux Infrared Color P3", "PictureFX - Faux Infrared R0a", "PictureFX - Faux Infrared R0b", "PictureFX - Faux Infrared YP1", "GoldFX - Bright Spring Breeze", "GoldFX - Bright Summer Heat", "GoldFX - Hot Summer Heat", "GoldFX - Perfect Sunset 01min", "GoldFX - Perfect Sunset 05min", "GoldFX - Perfect Sunset 10min", "GoldFX - Spring Breeze", "GoldFX - Summer Heat", "TechnicalFX - Backlight Filter", "ZilverFX - B&W Solarization", "ZilverFX - InfraRed", "ZilverFX - Vintage B&W"]),
    ) # type: ignore
    var_prop21: EnumProperty(
        name="Pixelmator",
        default="1",
        items=create_enum(["All [Collage]", "None", "Black & White 01", "Black & White 02", "Black & White 03", "Black & White 04", "Black & White 05", "Black & White 06", "Cinematic 01", "Cinematic 02", "Cinematic 03", "Cinematic 04", "Cinematic 05", "Cinematic 06", "Cinematic 07", "Classic Films 01", "Classic Films 02", "Classic Films 03", "Classic Films 04", "Classic Films 05", "Landscape 01", "Landscape 02", "Landscape 03", "Landscape 04", "Landscape 05", "Modern Films 01", "Modern Films 02", "Modern Films 03", "Modern Films 04", "Modern Films 05", "Modern Films 06", "Modern Films 07", "Night 01", "Night 02", "Night 03", "Night 04", "Night 05", "Urban 01", "Urban 02", "Urban 03", "Urban 04", "Urban 05", "Vintage 01", "Vintage 02", "Vintage 03", "Vintage 04", "Vintage 05"]),
    ) # type: ignore
    var_prop22: EnumProperty(
        name="PIXLS.US",
        default="1",
        items=create_enum(["All [Collage]", "None", "Amstragram", "Amstragram+", "Autumn", "Cinematic Lady Bird", "Cinematic Mexico", "Dark Blues in Sunlight", "Delicatessen", "Expired 69", "Faded Look", "Faded Print", "Hypressen", "Magenta Yellow", "Metropolis", "Modern Film", "Newspaper", "Night Spy", "Progressen", "Prussian Blue", "Seventies Magazine", "Street", "Sweet Bubblegum", "Sweet Gelatto", "Taiga", "Tarraco", "Unknown", "Uzbek Bukhara", "Uzbek Marriage", "Uzbek Samarcande", "Velvetia", "Warm Vintage", "Whiter Whites"]),
    ) # type: ignore
    var_prop23: EnumProperty(
        name="Purple11",
        default="1",
        items=create_enum(["All [Collage]", "None", "Going for a Walk", "Good Morning", "Nah", "Once Upon a Time", "Passing By", "Serenity", "Smooth Sailing", "Undeniable", "Undeniable 2", "Urban Cowboy", "We&#x27;ll See", "You Can Do It"]),
    ) # type: ignore
    var_prop24: EnumProperty(
        name="RocketStock",
        default="1",
        items=create_enum(["All [Collage]", "None", "Arabica 12", "Ava 614", "Azrael 93", "Bourbon 64", "Byers 11", "Chemical 168", "Clayton 33", "Clouseau 54", "Cobi 3", "Contrail 35", "Cubicle 99", "Django 25", "Domingo 145", "Faded 47", "Folger 50", "Fusion 88", "Hyla 68", "Korben 214", "Lenox 340", "Lucky 64", "McKinnon 75", "Milo 5", "Neon 770", "Paladin 1875", "Pasadena 21", "Pitaya 15", "Reeve 38", "Remy 24", "Sprocket 231", "Teigen 28", "Trent 18", "Tweed 71", "Vireo 37", "Zed 32", "Zeke 39"]),
    ) # type: ignore
    var_prop25: EnumProperty(
        name="Shamoon Abbasi",
        default="1",
        items=create_enum(["All [Collage]", "None", "City 7", "Coffee 44", "Date 39", "Day for Night", "Denoise Simple 40", "Desert Gold 37", "Directions 23", "Drop Green Tint 14", "Elegance 38", "Golden Night Softner 43", "Golden Sony 37", "Green 15", "Happyness 133", "HLG 1", "Industrial 33", "Morning 6", "Morroco 16", "Night King 141", "Rest 33", "Shadow King 39", "Spy 29", "Thriller 2", "Turkiest 42", "Vintage 163", "Wooden Gold 20"]),
    ) # type: ignore
    var_prop26: EnumProperty(
        name="SmallHD Movie Look",
        default="1",
        items=create_enum(["All [Collage]", "None", "Apocalypse This Very Moment", "B-Boyz 2", "Bob Ford", "Life Giving Tree", "Moonrise", "Saving Private Damon", "The Matrices"]),
    ) # type: ignore
    var_prop27: EnumProperty(
        name="Todd Blankenship",
        default="1",
        items=create_enum(["All [Collage]", "None", "Blue Architecture", "Blue Hour", "Cold Chrome", "Crisp Autumn", "Dark And Somber", "Hard Boost", "Long Beach Morning", "Lush Green", "Magic Hour", "Natural Boost", "Orange And Blue", "Soft Black And White", "Waves"]),
    ) # type: ignore
    var_prop28: EnumProperty(
        name="Youssef Hossam",
        default="1",
        items=create_enum(["All [Collage]", "None", "Cinematic Forest", "City", "Darkness", "Hallowen Dark", "Sea"]),
    ) # type: ignore
    var_prop29: EnumProperty(
        name="Others",
        default="1",
        items=create_enum(["All [Collage]", "None", "60&#x27;s", "60&#x27;s (faded)", "60&#x27;s (faded alt)", "Alien green", "Black & White", "Bleach bypass", "Blue mono", "Cinematic-01", "Cinematic-02", "Cinematic-03", "Color (rich)", "Faded", "Faded (alt)", "Faded (analog)", "Faded (extreme)", "Faded (vivid)", "Expired (fade)", "Expired (polaroid)", "Extreme", "Fade", "Faux infrared", "Golden", "Golden (bright)", "Golden (fade)", "Golden (mono)", "Golden (vibrant)", "Green mono", "Hong Kong", "Instant-C", "K-Tone Vintage Kodachrome", "Light (blown)", "Lomo", "Mono tinted", "Muted fade", "Mute shift", "Natural (vivid)", "Nostalgic", "Orange tone", "Pink fade", "Purple", "Retro", "Rotate (muted)", "Rotate (vibrant)", "Rotated", "Rotated (crush)", "Smooth crome-ish", "Smooth fade", "Soft fade", "Solarize color", "Solarized color2", "Summer", "Summer (alt)", "Sunny", "Sunny (alt)", "Sunny (warm)", "Sunny (rich)", "Super warm", "Super warm (rich)", "Sutro FX", "Vibrant", "Vibrant (alien)", "Vibrant (contrast)", "Vibrant (crome-ish)", "Vintage", "Vintage (alt)", "Vintage (brighter)", "Warm", "Warm (highlight)", "Warm (yellow)"]),
    ) # type: ignore
    var_prop30: IntProperty(
        name="Thumbnail Size",
        default=512,
        min=0, 
        max=1024, 
    ) # type: ignore
    var_prop32: FloatProperty(
        name="Strength (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop33: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop34: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop35: FloatProperty(
        name="Gamma (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop36: FloatProperty(
        name="Hue (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop37: FloatProperty(
        name="Saturation (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop38: EnumProperty(
        name="Normalize Colors",
        default="0",
        items=create_enum(["None", "Pre-Normalize", "Post-Normalize", "Both"]),
    ) # type: ignore
    var_prop40: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_color_presets {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18},{self.var_prop19},{self.var_prop20},{self.var_prop21},{self.var_prop22},{self.var_prop23},{self.var_prop24},{self.var_prop25},{self.var_prop26},{self.var_prop27},{self.var_prop28},{self.var_prop29},{self.var_prop30},{self.var_prop32},{self.var_prop33},{self.var_prop34},{self.var_prop35},{self.var_prop36},{self.var_prop37},{self.var_prop38},{self.var_prop40},50,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"

################################################################################
################################################################################

class GMIC_FColor_colortemperature(GMICBaseNode):
    """Color Temperature by Author: Tom Keil. Latest update: 2012/04/05."""
    # fx_tk_colortemp

    bl_idname = "FColor_colortemperature"
    bl_label = "Color Temperature"

    node_props = ["var_prop0", "var_prop1", "var_prop3"]

    var_prop0: FloatProperty(
        name="Color Temperature",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1: BoolProperty(
        name="Automatic Color Balance",
        default=0,
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_tk_colortemp {self.var_prop0},{int(self.var_prop1)},{self.var_prop3}"

################################################################################
################################################################################

class GMIC_FColor_colormap(GMICBaseNode):
    """Colormap by Author: David Tschumperlé. Latest Update: 2011/27/12."""
    # fx_colormap

    bl_idname = "FColor_colormap"
    bl_label = "Colormap"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop14"]

    var_prop0: EnumProperty(
        name="Colormap",
        default="2",
        items=create_enum(["Adaptive", "Custom", "Standard (256)", "HSV (256)", "Lines (256)", "Hot (256)", "Cool (256)", "Jet (256)", "Flag (256)", "Cube (256)"]),
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Dithering",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Number of Tones",
        default=32,
        min=2, 
        max=256, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Number of Colors",
        default=8,
        min=2, 
        max=8, 
    ) # type: ignore
    var_prop5: FloatVectorProperty(
        name="1st Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop6: FloatVectorProperty(
        name="2nd Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop7: FloatVectorProperty(
        name="3rd Color",
        default=(1.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop8: FloatVectorProperty(
        name="4th Color",
        default=(0.0,1.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop9: FloatVectorProperty(
        name="5th Color",
        default=(0.0,0.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop10: FloatVectorProperty(
        name="6th Color",
        default=(1.0,1.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop11: FloatVectorProperty(
        name="7th Color",
        default=(1.0,0.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop12: FloatVectorProperty(
        name="8th Color",
        default=(0.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop14: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_colormap {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop4},{self.var_prop5[0]*255},{self.var_prop5[1]*255},{self.var_prop5[2]*255},255,{self.var_prop6[0]*255},{self.var_prop6[1]*255},{self.var_prop6[2]*255},255,{self.var_prop7[0]*255},{self.var_prop7[1]*255},{self.var_prop7[2]*255},255,{self.var_prop8[0]*255},{self.var_prop8[1]*255},{self.var_prop8[2]*255},255,{self.var_prop9[0]*255},{self.var_prop9[1]*255},{self.var_prop9[2]*255},255,{self.var_prop10[0]*255},{self.var_prop10[1]*255},{self.var_prop10[2]*255},255,{self.var_prop11[0]*255},{self.var_prop11[1]*255},{self.var_prop11[2]*255},255,{self.var_prop12[0]*255},{self.var_prop12[1]*255},{self.var_prop12[2]*255},255,{self.var_prop14},50,50"

################################################################################
################################################################################

class GMIC_FColor_contrast(GMICBaseNode):
    """Contrast by &lt;strong&gt;Enhance luminance contrast. Filter by &lt;a href&#x3D;&quot;https://discuss.pixls.us/u/afre&quot;&gt;afre&lt;/a&gt; 2020 Jan9.&lt;/strong&gt; """
    # afre_contrast

    bl_idname = "FColor_contrast"
    bl_label = "Contrast"

    node_props = ["var_prop1"]

    var_prop1: IntProperty(
        name="Amount",
        default=50,
        min=-200, 
        max=200, 
    ) # type: ignore

    def create_command(self):
        return f"afre_contrast {self.var_prop1}"

################################################################################
################################################################################

class GMIC_FColor_customizeclut(GMICBaseNode):
    """Customize CLUT by Author: David Tschumperlé. Latest Update: 2016/14/06."""
    # fx_customize_clut

    bl_idname = "FColor_customizeclut"
    bl_label = "Customize CLUT"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop13", "var_prop14", "var_prop17", "var_prop18", "var_prop19", "var_prop21", "var_prop22", "var_prop23", "var_prop25", "var_prop26", "var_prop27", "var_prop29", "var_prop30", "var_prop31", "var_prop33", "var_prop34", "var_prop35", "var_prop37", "var_prop38", "var_prop39", "var_prop41", "var_prop42", "var_prop43", "var_prop45", "var_prop46", "var_prop47", "var_prop49", "var_prop50", "var_prop51", "var_prop53", "var_prop54", "var_prop55", "var_prop57", "var_prop58", "var_prop59", "var_prop61", "var_prop62", "var_prop63", "var_prop65", "var_prop66", "var_prop67", "var_prop69", "var_prop70", "var_prop71", "var_prop73", "var_prop74", "var_prop75", "var_prop77", "var_prop78", "var_prop79", "var_prop81", "var_prop82", "var_prop83", "var_prop85", "var_prop86", "var_prop87", "var_prop89", "var_prop90", "var_prop91", "var_prop93", "var_prop94", "var_prop95", "var_prop97", "var_prop98", "var_prop99", "var_prop101", "var_prop102", "var_prop103", "var_prop105", "var_prop106", "var_prop107", "var_prop109", "var_prop110", "var_prop111"]

    var_prop0: FloatProperty(
        name="Keypoint Influence (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Lock Uniform Sampling",
        default="0",
        items=create_enum(["None", "8 Keypoints (RGB Corners)", "27 Keypoints", "64 Keypoints", "125 Keypoints", "216 Keypoints", "343 Keypoints"]),
    ) # type: ignore
    var_prop2: IntProperty(
        name="Spatial Regularization",
        default=10,
        min=0, 
        max=30, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Gamma (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Hue (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Saturation (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: BoolProperty(
        name="Post-Normalize",
        default=0,
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Output Corresponding CLUT",
        default="0",
        items=create_enum(["Disable", "512x512 Layer", "4096x4096 Layer"]),
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Preview Type",
        default="8",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Horizontal", "Duplicate Vertical", "HaldCLUT", "3D CLUT (Fast)", "3D CLUT (Precise)"]),
    ) # type: ignore
    var_prop14: FloatProperty(
        name="CLUT Opacity",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop17: EnumProperty(
        name="Action #1",
        default="1",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop18: FloatVectorProperty(
        name="Source Color #1",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop19: FloatVectorProperty(
        name="Target Color #1",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop21: EnumProperty(
        name="Action #2",
        default="1",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop22: FloatVectorProperty(
        name="Source Color #2",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop23: FloatVectorProperty(
        name="Target Color #2",
        default=(1.0,0.7686274509803922,0.5019607843137255),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop25: EnumProperty(
        name="Action #3",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop26: FloatVectorProperty(
        name="Source Color #3",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop27: FloatVectorProperty(
        name="Target Color #3",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop29: EnumProperty(
        name="Action #4",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop30: FloatVectorProperty(
        name="Source Color #4",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop31: FloatVectorProperty(
        name="Target Color #4",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop33: EnumProperty(
        name="Action #5",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop34: FloatVectorProperty(
        name="Source Color #5",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop35: FloatVectorProperty(
        name="Target Color #5",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop37: EnumProperty(
        name="Action #6",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop38: FloatVectorProperty(
        name="Source Color #6",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop39: FloatVectorProperty(
        name="Target Color #6",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop41: EnumProperty(
        name="Action #7",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop42: FloatVectorProperty(
        name="Source Color #7",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop43: FloatVectorProperty(
        name="Target Color #7",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop45: EnumProperty(
        name="Action #8",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop46: FloatVectorProperty(
        name="Source Color #8",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop47: FloatVectorProperty(
        name="Target Color #8",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop49: EnumProperty(
        name="Action #9",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop50: FloatVectorProperty(
        name="Source Color #9",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop51: FloatVectorProperty(
        name="Target Color #9",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop53: EnumProperty(
        name="Action #10",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop54: FloatVectorProperty(
        name="Source Color #10",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop55: FloatVectorProperty(
        name="Target Color #10",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop57: EnumProperty(
        name="Action #11",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop58: FloatVectorProperty(
        name="Source Color #11",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop59: FloatVectorProperty(
        name="Target Color #11",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop61: EnumProperty(
        name="Action #12",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop62: FloatVectorProperty(
        name="Source Color #12",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop63: FloatVectorProperty(
        name="Target Color #12",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop65: EnumProperty(
        name="Action #13",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop66: FloatVectorProperty(
        name="Source Color #13",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop67: FloatVectorProperty(
        name="Target Color #13",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop69: EnumProperty(
        name="Action #14",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop70: FloatVectorProperty(
        name="Source Color #14",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop71: FloatVectorProperty(
        name="Target Color #14",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop73: EnumProperty(
        name="Action #15",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop74: FloatVectorProperty(
        name="Source Color #15",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop75: FloatVectorProperty(
        name="Target Color #15",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop77: EnumProperty(
        name="Action #16",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop78: FloatVectorProperty(
        name="Source Color #16",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop79: FloatVectorProperty(
        name="Target Color #16",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop81: EnumProperty(
        name="Action #17",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop82: FloatVectorProperty(
        name="Source Color #17",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop83: FloatVectorProperty(
        name="Target Color #17",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop85: EnumProperty(
        name="Action #18",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop86: FloatVectorProperty(
        name="Source Color #18",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop87: FloatVectorProperty(
        name="Target Color #18",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop89: EnumProperty(
        name="Action #19",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop90: FloatVectorProperty(
        name="Source Color #19",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop91: FloatVectorProperty(
        name="Target Color #19",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop93: EnumProperty(
        name="Action #20",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop94: FloatVectorProperty(
        name="Source Color #20",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop95: FloatVectorProperty(
        name="Target Color #20",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop97: EnumProperty(
        name="Action #21",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop98: FloatVectorProperty(
        name="Source Color #21",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop99: FloatVectorProperty(
        name="Target Color #21",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop101: EnumProperty(
        name="Action #22",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop102: FloatVectorProperty(
        name="Source Color #22",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop103: FloatVectorProperty(
        name="Target Color #22",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop105: EnumProperty(
        name="Action #23",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop106: FloatVectorProperty(
        name="Source Color #23",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop107: FloatVectorProperty(
        name="Target Color #23",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop109: EnumProperty(
        name="Action #24",
        default="0",
        items=create_enum(["Ignore", "Lock Source", "Replace Source by Target"]),
    ) # type: ignore
    var_prop110: FloatVectorProperty(
        name="Source Color #24",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop111: FloatVectorProperty(
        name="Target Color #24",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore

    def create_command(self):
        return f"fx_customize_clut {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{int(self.var_prop10)},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop17},{self.var_prop18[0]*255},{self.var_prop18[1]*255},{self.var_prop18[2]*255},255,{self.var_prop19[0]*255},{self.var_prop19[1]*255},{self.var_prop19[2]*255},255,{self.var_prop21},{self.var_prop22[0]*255},{self.var_prop22[1]*255},{self.var_prop22[2]*255},255,{self.var_prop23[0]*255},{self.var_prop23[1]*255},{self.var_prop23[2]*255},255,{self.var_prop25},{self.var_prop26[0]*255},{self.var_prop26[1]*255},{self.var_prop26[2]*255},255,{self.var_prop27[0]*255},{self.var_prop27[1]*255},{self.var_prop27[2]*255},255,{self.var_prop29},{self.var_prop30[0]*255},{self.var_prop30[1]*255},{self.var_prop30[2]*255},255,{self.var_prop31[0]*255},{self.var_prop31[1]*255},{self.var_prop31[2]*255},255,{self.var_prop33},{self.var_prop34[0]*255},{self.var_prop34[1]*255},{self.var_prop34[2]*255},255,{self.var_prop35[0]*255},{self.var_prop35[1]*255},{self.var_prop35[2]*255},255,{self.var_prop37},{self.var_prop38[0]*255},{self.var_prop38[1]*255},{self.var_prop38[2]*255},255,{self.var_prop39[0]*255},{self.var_prop39[1]*255},{self.var_prop39[2]*255},255,{self.var_prop41},{self.var_prop42[0]*255},{self.var_prop42[1]*255},{self.var_prop42[2]*255},255,{self.var_prop43[0]*255},{self.var_prop43[1]*255},{self.var_prop43[2]*255},255,{self.var_prop45},{self.var_prop46[0]*255},{self.var_prop46[1]*255},{self.var_prop46[2]*255},255,{self.var_prop47[0]*255},{self.var_prop47[1]*255},{self.var_prop47[2]*255},255,{self.var_prop49},{self.var_prop50[0]*255},{self.var_prop50[1]*255},{self.var_prop50[2]*255},255,{self.var_prop51[0]*255},{self.var_prop51[1]*255},{self.var_prop51[2]*255},255,{self.var_prop53},{self.var_prop54[0]*255},{self.var_prop54[1]*255},{self.var_prop54[2]*255},255,{self.var_prop55[0]*255},{self.var_prop55[1]*255},{self.var_prop55[2]*255},255,{self.var_prop57},{self.var_prop58[0]*255},{self.var_prop58[1]*255},{self.var_prop58[2]*255},255,{self.var_prop59[0]*255},{self.var_prop59[1]*255},{self.var_prop59[2]*255},255,{self.var_prop61},{self.var_prop62[0]*255},{self.var_prop62[1]*255},{self.var_prop62[2]*255},255,{self.var_prop63[0]*255},{self.var_prop63[1]*255},{self.var_prop63[2]*255},255,{self.var_prop65},{self.var_prop66[0]*255},{self.var_prop66[1]*255},{self.var_prop66[2]*255},255,{self.var_prop67[0]*255},{self.var_prop67[1]*255},{self.var_prop67[2]*255},255,{self.var_prop69},{self.var_prop70[0]*255},{self.var_prop70[1]*255},{self.var_prop70[2]*255},255,{self.var_prop71[0]*255},{self.var_prop71[1]*255},{self.var_prop71[2]*255},255,{self.var_prop73},{self.var_prop74[0]*255},{self.var_prop74[1]*255},{self.var_prop74[2]*255},255,{self.var_prop75[0]*255},{self.var_prop75[1]*255},{self.var_prop75[2]*255},255,{self.var_prop77},{self.var_prop78[0]*255},{self.var_prop78[1]*255},{self.var_prop78[2]*255},255,{self.var_prop79[0]*255},{self.var_prop79[1]*255},{self.var_prop79[2]*255},255,{self.var_prop81},{self.var_prop82[0]*255},{self.var_prop82[1]*255},{self.var_prop82[2]*255},255,{self.var_prop83[0]*255},{self.var_prop83[1]*255},{self.var_prop83[2]*255},255,{self.var_prop85},{self.var_prop86[0]*255},{self.var_prop86[1]*255},{self.var_prop86[2]*255},255,{self.var_prop87[0]*255},{self.var_prop87[1]*255},{self.var_prop87[2]*255},255,{self.var_prop89},{self.var_prop90[0]*255},{self.var_prop90[1]*255},{self.var_prop90[2]*255},255,{self.var_prop91[0]*255},{self.var_prop91[1]*255},{self.var_prop91[2]*255},255,{self.var_prop93},{self.var_prop94[0]*255},{self.var_prop94[1]*255},{self.var_prop94[2]*255},255,{self.var_prop95[0]*255},{self.var_prop95[1]*255},{self.var_prop95[2]*255},255,{self.var_prop97},{self.var_prop98[0]*255},{self.var_prop98[1]*255},{self.var_prop98[2]*255},255,{self.var_prop99[0]*255},{self.var_prop99[1]*255},{self.var_prop99[2]*255},255,{self.var_prop101},{self.var_prop102[0]*255},{self.var_prop102[1]*255},{self.var_prop102[2]*255},255,{self.var_prop103[0]*255},{self.var_prop103[1]*255},{self.var_prop103[2]*255},255,{self.var_prop105},{self.var_prop106[0]*255},{self.var_prop106[1]*255},{self.var_prop106[2]*255},255,{self.var_prop107[0]*255},{self.var_prop107[1]*255},{self.var_prop107[2]*255},255,{self.var_prop109},{self.var_prop110[0]*255},{self.var_prop110[1]*255},{self.var_prop110[2]*255},255,{self.var_prop111[0]*255},{self.var_prop111[1]*255},{self.var_prop111[2]*255},255"

################################################################################
################################################################################

class GMIC_FColor_darksky(GMICBaseNode):
    """Dark Sky by &lt;strong&gt;Enhance landscape by darkening the sky. Filter by &lt;a href&#x3D;&quot;https://discuss.pixls.us/u/afre&quot;&gt;afre&lt;/a&gt; 2017-2020 Sep9.&lt;/strong&gt; """
    # afre_darksky

    bl_idname = "FColor_darksky"
    bl_label = "Dark Sky"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop1: EnumProperty(
        name="Blend",
        default="0",
        items=create_enum(["Softlight", "Overlay"]),
    ) # type: ignore
    var_prop2: IntProperty(
        name="Contrast",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Smooth",
        default="1",
        items=create_enum(["Fast (approx.)", "Slow (accurate)"]),
    ) # type: ignore
    var_prop4: IntProperty(
        name="Radius",
        default=0,
        min=0, 
        max=3, 
    ) # type: ignore

    def create_command(self):
        return f"afre_darksky {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FColor_detectskin(GMICBaseNode):
    """Detect Skin by Author: David Tschumperlé. Latest Update: 2014/03/01."""
    # fx_detect_skin

    bl_idname = "FColor_detectskin"
    bl_label = "Detect Skin"

    node_props = ["var_prop0", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop14"]

    var_prop0: EnumProperty(
        name="Skin Estimation",
        default="1",
        items=create_enum(["Manual", "Automatic"]),
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Tolerance",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Threshold",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Pre-Normalize Image",
        default=1,
    ) # type: ignore
    var_prop8: FloatProperty(
        name="X-Coordinate",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Y-Coordinate",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Radius",
        default=5.0,
        min=0.0, 
        max=25.0, 
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Output Mode",
        default="1",
        items=create_enum(["Probability Map", "Opaque Skin", "Transparent Skin"]),
    ) # type: ignore
    var_prop14: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_detect_skin {self.var_prop0},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop12},{self.var_prop14},50,50"

################################################################################
################################################################################

class GMIC_FColor_equalizehsihslhsv(GMICBaseNode):
    """Equalize HSI-HSL-HSV by Authors: David Tschumperlé and David Revoy. Latest Update: 2018/01/19."""
    # fx_equalize_hsv

    bl_idname = "FColor_equalizehsihslhsv"
    bl_label = "Equalize HSI-HSL-HSV"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop8", "var_prop9", "var_prop10", "var_prop13", "var_prop14", "var_prop15", "var_prop18", "var_prop19", "var_prop20", "var_prop23", "var_prop24", "var_prop25", "var_prop28", "var_prop29", "var_prop30", "var_prop33", "var_prop34", "var_prop35", "var_prop38", "var_prop39", "var_prop40", "var_prop43", "var_prop44", "var_prop45", "var_prop48", "var_prop49", "var_prop50", "var_prop52"]

    var_prop0: EnumProperty(
        name="Colorspace",
        default="1",
        items=create_enum(["HSI", "HSL", "HSV"]),
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Opacity (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Value Blending",
        default=0.0,
        min=0.0, 
        max=64.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Color Blending",
        default=0.0,
        min=0.0, 
        max=64.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Mapping",
        default="0",
        items=create_enum(["None", "Grey", "Color"]),
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Hue Offset",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Saturation Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Value Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Hue Offset",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Saturation Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Value Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Hue Offset",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Saturation Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Value Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop23: FloatProperty(
        name="Hue Offset",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop24: FloatProperty(
        name="Saturation Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop25: FloatProperty(
        name="Value Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop28: FloatProperty(
        name="Hue Offset",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop29: FloatProperty(
        name="Saturation Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop30: FloatProperty(
        name="Value Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop33: FloatProperty(
        name="Hue Offset",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop34: FloatProperty(
        name="Saturation Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop35: FloatProperty(
        name="Value Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop38: FloatProperty(
        name="Hue Offset",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop39: FloatProperty(
        name="Saturation Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop40: FloatProperty(
        name="Value Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop43: FloatProperty(
        name="Hue Offset",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop44: FloatProperty(
        name="Saturation Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop45: FloatProperty(
        name="Value Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop48: FloatProperty(
        name="Hue Offset",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop49: FloatProperty(
        name="Saturation Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop50: FloatProperty(
        name="Value Offset",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop52: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_equalize_hsv {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop18},{self.var_prop19},{self.var_prop20},{self.var_prop23},{self.var_prop24},{self.var_prop25},{self.var_prop28},{self.var_prop29},{self.var_prop30},{self.var_prop33},{self.var_prop34},{self.var_prop35},{self.var_prop38},{self.var_prop39},{self.var_prop40},{self.var_prop43},{self.var_prop44},{self.var_prop45},{self.var_prop48},{self.var_prop49},{self.var_prop50},{self.var_prop52},50,50"

################################################################################
################################################################################

class GMIC_FColor_equalizehsv(GMICBaseNode):
    """Equalize HSV by Author: Jérome Ferrari. Latest Update: 01/14/2011."""
    # fx_hsv_equalizer

    bl_idname = "FColor_equalizehsv"
    bl_label = "Equalize HSV"

    node_props = ["var_prop0", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop18"]

    var_prop0: BoolProperty(
        name="Preview Bands",
        default=0,
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Hue Band",
        default=180.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Band Width",
        default=40.0,
        min=1.0, 
        max=360.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Hue Shift",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Saturation Correction",
        default=0.0,
        min=-0.99, 
        max=0.99, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Value Correction",
        default=0.0,
        min=-0.99, 
        max=0.99, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Hue Band",
        default=180.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Band Width",
        default=40.0,
        min=1.0, 
        max=360.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Hue Shift",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Saturation Correction",
        default=0.0,
        min=-0.99, 
        max=0.99, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Value Correction",
        default=0.0,
        min=-0.99, 
        max=0.99, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Hue Band",
        default=180.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Band Width",
        default=40.0,
        min=1.0, 
        max=360.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Hue Shift",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Saturation Correction",
        default=0.0,
        min=-0.99, 
        max=0.99, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Value Correction",
        default=0.0,
        min=-0.99, 
        max=0.99, 
    ) # type: ignore

    def create_command(self):
        return f"fx_hsv_equalizer {int(self.var_prop0)},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18}"

################################################################################
################################################################################

class GMIC_FColor_hsladjustment(GMICBaseNode):
    """HSL Adjustment by Author : Garagecoder. Latest update : 2015/05/15."""
    # gcd_hsl

    bl_idname = "FColor_hsladjustment"
    bl_label = "HSL Adjustment"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop9", "var_prop12", "var_prop13", "var_prop15"]

    var_prop2: FloatProperty(
        name="Contrast",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Level",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Auto Reduce Level (Level Slider Is Disabled)",
        default=0,
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Hue",
        default=180.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Amount",
        default=0.2,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop9: BoolProperty(
        name="Auto Set Hue Inverse (Hue Slider Is Disabled)",
        default=0,
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Gamma",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Contrast",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop15: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"gcd_hsl {self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop7},{self.var_prop8},{int(self.var_prop9)},{self.var_prop12},{self.var_prop13},{self.var_prop15}"

################################################################################
################################################################################

class GMIC_FColor_huelightendarken(GMICBaseNode):
    """Hue Lighten-Darken by Author : Iain Fergusson. Update: 4 March 2014 - Added parallel processing option"""
    # iain_hue_light_dark_p

    bl_idname = "FColor_huelightendarken"
    bl_label = "Hue Lighten-Darken"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop19", "var_prop20", "var_prop22", "var_prop23", "var_prop24", "var_prop25", "var_prop27", "var_prop29"]

    var_prop0: FloatProperty(
        name="Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="2",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="3",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Yellow",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="5",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="6",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="8",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Cyan",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="10",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="11",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="13",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="14",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Magenta",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="16",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="17",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="18",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Global",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop20: BoolProperty(
        name="HSL",
        default=0,
    ) # type: ignore
    var_prop22: FloatProperty(
        name="Sat Top",
        default=255.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop23: FloatProperty(
        name="Sat Bottom",
        default=100.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop24: FloatProperty(
        name="Value Top",
        default=255.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop25: FloatProperty(
        name="Value Bottom",
        default=0.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop27: BoolProperty(
        name="B&W",
        default=0,
    ) # type: ignore
    var_prop29: EnumProperty(
        name="Parallel Processing",
        default="0",
        items=create_enum(["Auto", "Off"]),
    ) # type: ignore

    def create_command(self):
        return f"iain_hue_light_dark_p {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop19},{int(self.var_prop20)},{self.var_prop22},{self.var_prop23},{self.var_prop24},{self.var_prop25},{int(self.var_prop27)},{self.var_prop29}"

################################################################################
################################################################################

class GMIC_FColor_lmsadjustment(GMICBaseNode):
    """LMS Adjustment by Author : Garagecoder. Latest update : 2018/09/08."""
    # gcd_balance_lms

    bl_idname = "FColor_lmsadjustment"
    bl_label = "LMS Adjustment"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop7", "var_prop8"]

    var_prop2: FloatProperty(
        name="Long",
        default=1.0,
        min=0.5, 
        max=1.5, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Medium",
        default=1.0,
        min=0.5, 
        max=1.5, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Short",
        default=1.0,
        min=0.5, 
        max=1.5, 
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Adapt Luminance",
        default=0,
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Pre Normalize",
        default=0,
    ) # type: ignore
    var_prop8: BoolProperty(
        name="Auto Balance",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"gcd_balance_lms {self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop6)},{int(self.var_prop7)},{int(self.var_prop8)}"

################################################################################
################################################################################

class GMIC_FColor_localcontrast(GMICBaseNode):
    """Local Contrast by &lt;strong&gt;Enhance local contrast. Filter by &lt;a href&#x3D;&quot;https://discuss.pixls.us/u/afre&quot;&gt;afre&lt;/a&gt; 2020 Jul28-Sep5.&lt;/strong&gt; """
    # afre_localcontrast

    bl_idname = "FColor_localcontrast"
    bl_label = "Local Contrast"

    node_props = ["var_prop1", "var_prop2"]

    var_prop1: IntProperty(
        name="Radius",
        default=1,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Amount",
        default=50,
        min=-100, 
        max=100, 
    ) # type: ignore

    def create_command(self):
        return f"afre_localcontrast {self.var_prop1},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FColor_metalliclook(GMICBaseNode):
    """Metallic Look by Author : Tom Keil. Latest update: 2011/12/04."""
    # fx_tk_metallic

    bl_idname = "FColor_metalliclook"
    bl_label = "Metallic Look"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: FloatProperty(
        name="Strength",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Metal",
        default="0",
        items=create_enum(["Silver", "Gold", "Copper", "Bronze", "Blue steel"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_tk_metallic {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FColor_mixercmyk(GMICBaseNode):
    """Mixer [CMYK] by Author: David Tschumperlé. Latest Update: 2016/20/06."""
    # fx_mix_cmyk

    bl_idname = "FColor_mixercmyk"
    bl_label = "Mixer [CMYK]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop13", "var_prop14", "var_prop16", "var_prop17", "var_prop19"]

    var_prop0: FloatProperty(
        name="Cyan Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Cyan Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Cyan Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Magenta Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Magenta Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Magenta Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Yellow Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Yellow Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Yellow Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Key Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Key Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Key Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop16: EnumProperty(
        name="Tones Range",
        default="0",
        items=create_enum(["All tones", "Shadows", "Mid-Tones", "Highlights"]),
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Tones Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop19: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_mix_cmyk {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop16},{self.var_prop17},{self.var_prop19},50,50"

################################################################################
################################################################################

class GMIC_FColor_mixerhsv(GMICBaseNode):
    """Mixer [HSV] by Author: David Tschumperlé. Latest Update: 2016/20/06."""
    # fx_mix_hsv

    bl_idname = "FColor_mixerhsv"
    bl_label = "Mixer [HSV]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop13", "var_prop15"]

    var_prop0: FloatProperty(
        name="Hue Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Hue Shift",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Hue Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Saturation Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Saturation Shift",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Saturation Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Value Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Value Shift",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Value Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Tones Range",
        default="0",
        items=create_enum(["All Tones", "Shadows", "Mid-Tones", "Highlights"]),
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Tones Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop15: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_mix_hsv {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop12},{self.var_prop13},{self.var_prop15},50,50"

################################################################################
################################################################################

class GMIC_FColor_mixerlab(GMICBaseNode):
    """Mixer [Lab] by Author: David Tschumperlé. Latest Update: 2016/20/06."""
    # fx_mix_lab

    bl_idname = "FColor_mixerlab"
    bl_label = "Mixer [Lab]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop13", "var_prop15"]

    var_prop0: FloatProperty(
        name="Lightness Factor",
        default=1.0,
        min=0.5, 
        max=1.5, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Lightness Shift",
        default=0.0,
        min=-50.0, 
        max=50.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Lightness Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="A-Color Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="A-Color Shift",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="A-Color Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="B-Color Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="B-Color Shift",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="B-Color Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Tones Range",
        default="0",
        items=create_enum(["All Tones", "Shadows", "Mid-Tones", "Highlights"]),
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Tones Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop15: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_mix_lab {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop12},{self.var_prop13},{self.var_prop15},50,50"

################################################################################
################################################################################

class GMIC_FColor_mixerpca(GMICBaseNode):
    """Mixer [PCA] by Author: David Tschumperlé. Latest Update: 2018/07/18."""
    # fx_mix_pca

    bl_idname = "FColor_mixerpca"
    bl_label = "Mixer [PCA]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop15", "var_prop19"]

    var_prop0: FloatProperty(
        name="Primary Factor",
        default=0.0,
        min=-1.5, 
        max=1.5, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Primary Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Primary Twist",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Primary Gamma",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Secondary Factor",
        default=0.0,
        min=-1.5, 
        max=1.5, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Secondary Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Secondary Twist",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Secondary Gamma",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Tertiary Factor",
        default=0.0,
        min=-1.5, 
        max=1.5, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Tertiary Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Tertiary Twist",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Tertiary Gamma",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop15: BoolProperty(
        name="Display Color Axes",
        default=1,
    ) # type: ignore
    var_prop19: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_mix_pca {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{int(self.var_prop15)},NaN,NaN,{self.var_prop19},50,50"

################################################################################
################################################################################

class GMIC_FColor_mixerrgb(GMICBaseNode):
    """Mixer [RGB] by Author: David Tschumperlé. Latest Update: 2016/20/06."""
    # fx_mix_rgb

    bl_idname = "FColor_mixerrgb"
    bl_label = "Mixer [RGB]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop13", "var_prop15"]

    var_prop0: FloatProperty(
        name="Red Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Red Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Red Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Green Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Green Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Green Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Blue Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Blue Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Blue Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Tones Range",
        default="0",
        items=create_enum(["All Tones", "Shadows", "Mid-Tones", "Highlights"]),
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Tones Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop15: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_mix_rgb {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop12},{self.var_prop13},{self.var_prop15},50,50"

################################################################################
################################################################################

class GMIC_FColor_mixerycbcr(GMICBaseNode):
    """Mixer [YCbCr] by Author: David Tschumperlé. Latest Update: 2016/20/06."""
    # fx_mix_ycbcr

    bl_idname = "FColor_mixerycbcr"
    bl_label = "Mixer [YCbCr]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop13", "var_prop15"]

    var_prop0: FloatProperty(
        name="Luminance Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Luminance Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Luminance Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Blue Chroma Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Blue Chroma Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Blue Chroma Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Red Chroma Factor",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Red Chroma Shift",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Red Chroma Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Tones Range",
        default="0",
        items=create_enum(["All Tones", "Shadows", "Mid-Tones", "Highlights"]),
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Tones Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop15: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_mix_ycbcr {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop12},{self.var_prop13},{self.var_prop15},50,50"

################################################################################
################################################################################

class GMIC_FColor_normalizebrightness(GMICBaseNode):
    """Normalize Brightness by Author : Garagecoder. Latest update : 2017/05/27."""
    # gcd_normalize_brightness

    bl_idname = "FColor_normalizebrightness"
    bl_label = "Normalize Brightness"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7"]

    var_prop2: FloatProperty(
        name="Bright",
        default=0.0,
        min=-2.0, 
        max=2.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Area",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smooth",
        default=0.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Channels",
        default="3",
        items=create_enum(["HSI", "HSV", "Lab", "YCbCr", "sRGB"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Mask",
        default="0",
        items=create_enum(["Normal", "Darken", "Lighten"]),
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Absolute Brightness",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"gcd_normalize_brightness {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{int(self.var_prop7)}"

################################################################################
################################################################################

class GMIC_FColor_retinex(GMICBaseNode):
    """Retinex by Author: David Tschumperlé. Latest Update: 2016/13/09."""
    # fx_retinex

    bl_idname = "FColor_retinex"
    bl_label = "Retinex"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7", "var_prop8", "var_prop9", "var_prop11"]

    var_prop0: FloatProperty(
        name="Strength (%)",
        default=75.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Value Offset",
        default=16.0,
        min=1.0, 
        max=256.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Colorspace",
        default="1",
        items=create_enum(["HSI", "HSV", "Lab", "Linear RGB", "RGB", "YCbCr"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Min Cut (%)",
        default=1.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Max Cut (%)",
        default=1.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Regularization",
        default=5.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Low Scale",
        default=15.0,
        min=1.0, 
        max=512.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Middle Scale",
        default=80.0,
        min=1.0, 
        max=512.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="High Scale",
        default=250.0,
        min=1.0, 
        max=512.0, 
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_retinex {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop11},50,50"

################################################################################
################################################################################

class GMIC_FColor_retrofade(GMICBaseNode):
    """Retro Fade by Author: David Tschumperlé. Latest Update: 2016/25/10."""
    # fx_retrofade

    bl_idname = "FColor_retrofade"
    bl_label = "Retro Fade"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: IntProperty(
        name="Iterations",
        default=20,
        min=1, 
        max=64, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Colors",
        default=6,
        min=2, 
        max=32, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Grain",
        default=40.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_retrofade {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FColor_rgbtone(GMICBaseNode):
    """RGB Tone by """
    # iain_rgb_tone

    bl_idname = "FColor_rgbtone"
    bl_label = "RGB Tone"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop7", "var_prop9", "var_prop10", "var_prop11", "var_prop14", "var_prop15", "var_prop16", "var_prop18", "var_prop19", "var_prop20", "var_prop22", "var_prop23", "var_prop24", "var_prop27", "var_prop28", "var_prop29", "var_prop31", "var_prop32", "var_prop33", "var_prop35", "var_prop36", "var_prop37", "var_prop40", "var_prop41", "var_prop42", "var_prop43", "var_prop44", "var_prop46"]

    var_prop1: FloatProperty(
        name="Little Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Some Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Much Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Little Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Some Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Much Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Little Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Some Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Much Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Little Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Some Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Much Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Little Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Some Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Much Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop22: FloatProperty(
        name="Little Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop23: FloatProperty(
        name="Some Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop24: FloatProperty(
        name="Much Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop27: FloatProperty(
        name="Little Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop28: FloatProperty(
        name="Some Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop29: FloatProperty(
        name="Much Red",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop31: FloatProperty(
        name="Little Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop32: FloatProperty(
        name="Some Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop33: FloatProperty(
        name="Much Green",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop35: FloatProperty(
        name="Little Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop36: FloatProperty(
        name="Some Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop37: FloatProperty(
        name="Much Blue",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop40: FloatProperty(
        name="None",
        default=255.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop41: FloatProperty(
        name="Little",
        default=255.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop42: FloatProperty(
        name="Some",
        default=255.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop43: FloatProperty(
        name="Much",
        default=255.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop44: FloatProperty(
        name="Most",
        default=255.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop46: EnumProperty(
        name="Output",
        default="0",
        items=create_enum(["Perserve Luminance", "Clip", "Scale"]),
    ) # type: ignore

    def create_command(self):
        return f"iain_rgb_tone {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop18},{self.var_prop19},{self.var_prop20},{self.var_prop22},{self.var_prop23},{self.var_prop24},{self.var_prop27},{self.var_prop28},{self.var_prop29},{self.var_prop31},{self.var_prop32},{self.var_prop33},{self.var_prop35},{self.var_prop36},{self.var_prop37},{self.var_prop40},{self.var_prop41},{self.var_prop42},{self.var_prop43},{self.var_prop44},{self.var_prop46}"

################################################################################
################################################################################

class GMIC_FColor_saturationeq(GMICBaseNode):
    """Saturation EQ by Author : Iain Fergusson. Update: 4 March 2014 - Added parallel processing option"""
    # Saturation_EQ_p

    bl_idname = "FColor_saturationeq"
    bl_label = "Saturation EQ"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop19", "var_prop20", "var_prop21", "var_prop23"]

    var_prop1: FloatProperty(
        name="Black",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Near Black",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Dark Grey",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Mid-Dark Grey",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Middle Grey",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Mid-Light Grey",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Light Grey",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Highlights",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="White",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="0",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="45",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="90",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="135",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="180",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="225",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="270",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="315",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop20: FloatProperty(
        name="360",
        default=0.0,
        min=-128.0, 
        max=128.0, 
    ) # type: ignore
    var_prop21: FloatProperty(
        name="Rotate Hue Bands",
        default=0.0,
        min=-45.0, 
        max=45.0, 
    ) # type: ignore
    var_prop23: EnumProperty(
        name="Parallel Processing",
        default="0",
        items=create_enum(["Auto", "Off"]),
    ) # type: ignore

    def create_command(self):
        return f"Saturation_EQ_p {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18},{self.var_prop19},{self.var_prop20},{self.var_prop21},{self.var_prop23}"

################################################################################
################################################################################

class GMIC_FColor_selectreplacecolor(GMICBaseNode):
    """Select-Replace Color by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_select_color

    bl_idname = "FColor_selectreplacecolor"
    bl_label = "Select-Replace Color"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: EnumProperty(
        name="Similarity Space",
        default="0",
        items=create_enum(["RGB[A]", "RGB", "YCbCr", "Red", "Green", "Blue", "Opacity", "Luminance", "Blue & Red Chrominances", "Hue", "Saturation"]),
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Tolerance",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Fill Holes",
        default=0,
        min=0, 
        max=256, 
    ) # type: ignore
    var_prop4: FloatVectorProperty(
        name="Selected Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Output As",
        default="0",
        items=create_enum(["Selected Colors", "Selected Mask", "Rejected Colors", "Rejected Mask", "Replaced Color"]),
    ) # type: ignore
    var_prop6: FloatVectorProperty(
        name="Replacement Color",
        default=(1.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_select_color {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4[0]*255},{self.var_prop4[1]*255},{self.var_prop4[2]*255},255,{self.var_prop5},{self.var_prop6[0]*255},{self.var_prop6[1]*255},{self.var_prop6[2]*255},255,{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FColor_selectivedesaturation(GMICBaseNode):
    """Selective Desaturation by Author: David Tschumperlé. Latest Update: 2015/15/07."""
    # fx_selective_desaturation

    bl_idname = "FColor_selectivedesaturation"
    bl_label = "Selective Desaturation"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatVectorProperty(
        name="Reference Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Desaturate",
        default="0",
        items=create_enum(["Reference Color", "All but Reference Color"]),
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Strength",
        default=3.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Regularization",
        default=0,
        min=0, 
        max=20, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Maximum Saturation",
        default="0",
        items=create_enum(["From Input", "From Reference Color", "Maximum Value"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_selective_desaturation {self.var_prop0[0]*255},{self.var_prop0[1]*255},{self.var_prop0[2]*255},255,{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FColor_sepia(GMICBaseNode):
    """Sepia by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_sepia

    bl_idname = "FColor_sepia"
    bl_label = "Sepia"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

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
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_sepia {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FColor_simulatefilm(GMICBaseNode):
    """Simulate Film by Author: David Tschumperlé. Latest Update: 2019/02/27."""
    # fx_simulate_film

    bl_idname = "FColor_simulatefilm"
    bl_label = "Simulate Film"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop20"]

    var_prop0: EnumProperty(
        name="Category",
        default="0",
        items=create_enum(["Black & White (25)", "Instant [Consumer] (54)", "Instant [Pro] (68)", "Fuji XTrans III (15)", "Negative [Color] (13)", "Negative [New] (39)", "Negative [Old] (44)", "Print Films (12)", "Slide [Color] (26)"]),
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Black & White",
        default="1",
        items=create_enum(["All [Collage]", "None", "Agfa APX 100", "Agfa APX 25", "Fuji Neopan 1600", "Fuji Neopan Acros 100", "Ilford Delta 100", "Ilford Delta 3200", "Ilford Delta 400", "Ilford FP4 Plus 125", "Ilford HP5 Plus 400", "Ilford HPS 800", "Ilford Pan F Plus 50", "Ilford XP2", "Kodak BW 400 CN", "Kodak HIE (HS Infra)", "Kodak T-Max 100", "Kodak T-Max 3200", "Kodak T-Max 400", "Kodak Tri-X 400", "Polaroid 664", "Polaroid 667", "Polaroid 672", "Rollei IR 400", "Rollei Ortho 25", "Rollei Retro 100 Tonal", "Rollei Retro 80s"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Instant [Consumer]",
        default="1",
        items=create_enum(["All [Collage]", "None", "Polaroid PX-100UV+ Cold --", "Polaroid PX-100UV+ Cold -", "Polaroid PX-100UV+ Cold", "Polaroid PX-100UV+ Cold +", "Polaroid PX-100UV+ Cold ++", "Polaroid PX-100UV+ Cold +++", "Polaroid PX-100UV+ Warm --", "Polaroid PX-100UV+ Warm -", "Polaroid PX-100UV+ Warm", "Polaroid PX-100UV+ Warm +", "Polaroid PX-100UV+ Warm ++", "Polaroid PX-100UV+ Warm +++", "Polaroid PX-680 --", "Polaroid PX-680 -", "Polaroid PX-680", "Polaroid PX-680 +", "Polaroid PX-680 ++", "Polaroid PX-680 Cold --", "Polaroid PX-680 Cold -", "Polaroid PX-680 Cold", "Polaroid PX-680 Cold +", "Polaroid PX-680 Cold ++", "Polaroid PX-680 Cold ++a", "Polaroid PX-680 Warm --", "Polaroid PX-680 Warm -", "Polaroid PX-680 Warm", "Polaroid PX-680 Warm +", "Polaroid PX-680 Warm ++", "Polaroid PX-70 --", "Polaroid PX-70 -", "Polaroid PX-70", "Polaroid PX-70 +", "Polaroid PX-70 ++", "Polaroid PX-70 +++", "Polaroid PX-70 Cold --", "Polaroid PX-70 Cold -", "Polaroid PX-70 Cold", "Polaroid PX-70 Cold +", "Polaroid PX-70 Cold ++", "Polaroid PX-70 Warm --", "Polaroid PX-70 Warm -", "Polaroid PX-70 Warm", "Polaroid PX-70 Warm +", "Polaroid PX-70 Warm ++", "Polaroid Time Zero (Expired) ---", "Polaroid Time Zero (Expired) --", "Polaroid Time Zero (Expired) -", "Polaroid Time Zero (Expired)", "Polaroid Time Zero (Expired) +", "Polaroid Time Zero (Expired) ++", "Polaroid Time Zero (Expired) Cold ---", "Polaroid Time Zero (Expired) Cold --", "Polaroid Time Zero (Expired) Cold -", "Polaroid Time Zero (Expired) Cold"]),
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Instant [Pro]",
        default="1",
        items=create_enum(["All [Collage]", "None", "Fuji FP-100c --", "Fuji FP-100c -", "Fuji FP-100c", "Fuji FP-100c (alt)", "Fuji FP-100c +", "Fuji FP-100c ++", "Fuji FP-100c ++a", "Fuji FP-100c +++", "Fuji FP-100c Cool --", "Fuji FP-100c Cool -", "Fuji FP-100c Cool", "Fuji FP-100c Cool +", "Fuji FP-100c Cool ++", "Fuji FP-100c Negative --", "Fuji FP-100c Negative -", "Fuji FP-100c Negative", "Fuji FP-100c Negative +", "Fuji FP-100c Negative ++", "Fuji FP-100c Negative ++a", "Fuji FP-100c Negative +++", "Fuji FP-3000b --", "Fuji FP-3000b -", "Fuji FP-3000b", "Fuji FP-3000b +", "Fuji FP-3000b ++", "Fuji FP-3000b +++", "Fuji FP-3000b HC", "Fuji FP-3000b Negative --", "Fuji FP-3000b Negative -", "Fuji FP-3000b Negative", "Fuji FP-3000b Negative +", "Fuji FP-3000b Negative ++", "Fuji FP-3000b Negative +++", "Fuji FP-3000b Negative Early", "Polaroid 665 --", "Polaroid 665 -", "Polaroid 665", "Polaroid 665 +", "Polaroid 665 ++", "Polaroid 665 Negative -", "Polaroid 665 Negative", "Polaroid 665 Negative +", "Polaroid 665 Negative HC", "Polaroid 669 --", "Polaroid 669 -", "Polaroid 669", "Polaroid 669 +", "Polaroid 669 ++", "Polaroid 669 +++", "Polaroid 669 Cold --", "Polaroid 669 Cold -", "Polaroid 669 Cold", "Polaroid 669 Cold +", "Polaroid 690 --", "Polaroid 690 -", "Polaroid 690", "Polaroid 690 +", "Polaroid 690 ++", "Polaroid 690 Cold --", "Polaroid 690 Cold -", "Polaroid 690 Cold", "Polaroid 690 Cold +", "Polaroid 690 Cold ++", "Polaroid 690 Warm --", "Polaroid 690 Warm -", "Polaroid 690 Warm", "Polaroid 690 Warm +", "Polaroid 690 Warm ++"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Fuji XTrans III",
        default="1",
        items=create_enum(["All [Collage]", "None", "Acros", "Acros+G", "Acros+R", "Acros+Ye", "Astia", "Classic Chrome", "Mono", "Mono+G", "Mono+R", "Mono+Ye", "Pro Neg Hi", "Pro Neg Std", "Provia", "Sepia", "Velvia"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Negative [Color]",
        default="1",
        items=create_enum(["All [Collage]", "None", "Agfa Ultra Color 100", "Agfa Vista 200", "Fuji Superia 200", "Fuji Superia HG 1600", "Fuji Superia Reala 100", "Fuji Superia X-Tra 800", "Kodak Ektar 100", "Kodak Elite 100 XPRO", "Kodak Elite Color 200", "Kodak Elite Color 400", "Kodak Portra 160 NC", "Kodak Portra 160 VC", "Lomography Redscale 100"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Negative [New]",
        default="1",
        items=create_enum(["All [Collage]", "None", "Fuji 160C -", "Fuji 160C", "Fuji 160C +", "Fuji 160C ++", "Fuji 400H -", "Fuji 400H", "Fuji 400H +", "Fuji 400H ++", "Fuji 800Z -", "Fuji 800Z", "Fuji 800Z +", "Fuji 800Z ++", "Fuji Ilford HP5 -", "Fuji Ilford HP5", "Fuji Ilford HP5 +", "Fuji Ilford HP5 ++", "Kodak Portra 160 -", "Kodak Portra 160", "Kodak Portra 160 +", "Kodak Portra 160 ++", "Kodak Portra 400 -", "Kodak Portra 400", "Kodak Portra 400 +", "Kodak Portra 400 ++", "Kodak Portra 800 -", "Kodak Portra 800", "Kodak Portra 800 +", "Kodak Portra 800 ++", "Kodak Portra 800 HC", "Kodak T-MAX 3200 -", "Kodak T-MAX 3200", "Kodak T-MAX 3200 +", "Kodak T-MAX 3200 ++", "Kodak T-MAX 3200 (alt)", "Kodak TRI-X 400 -", "Kodak TRI-X 400", "Kodak TRI-X 400 +", "Kodak TRI-X 400 ++", "Kodak TRI-X 400 (alt)"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Negative [Old]",
        default="1",
        items=create_enum(["All [Collage]", "None", "Fuji Ilford Delta 3200 -", "Fuji Ilford Delta 3200", "Fuji Ilford Delta 3200 +", "Fuji Ilford Delta 3200 ++", "Fuji Neopan 1600 -", "Fuji Neopan 1600", "Fuji Neopan 1600 +", "Fuji Neopan 1600 ++", "Fuji Superia 100 -", "Fuji Superia 100", "Fuji Superia 100 +", "Fuji Superia 100 ++", "Fuji Superia 400 -", "Fuji Superia 400", "Fuji Superia 400 +", "Fuji Superia 400 ++", "Fuji Superia 800 -", "Fuji Superia 800", "Fuji Superia 800 +", "Fuji Superia 800 ++", "Fuji Superia 1600 -", "Fuji Superia 1600", "Fuji Superia 1600 +", "Fuji Superia 1600 ++", "Kodak Portra 160 NC -", "Kodak Portra 160 NC", "Kodak Portra 160 NC +", "Kodak Portra 160 NC ++", "Kodak Portra 160 VC -", "Kodak Portra 160 VC", "Kodak Portra 160 VC +", "Kodak Portra 160 VC ++", "Kodak Portra 400 NC -", "Kodak Portra 400 NC", "Kodak Portra 400 NC +", "Kodak Portra 400 NC ++", "Kodak Portra 400 UC -", "Kodak Portra 400 UC", "Kodak Portra 400 UC +", "Kodak Portra 400 UC ++", "Kodak Portra 400 VC -", "Kodak Portra 400 VC", "Kodak Portra 400 VC +", "Kodak Portra 400 VC ++"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Print Films",
        default="1",
        items=create_enum(["All [Collage]", "None", "Fuji 3510 (Constlclip)", "Fuji 3510 (Constlmap)", "Fuji 3510 (Cuspclip)", "Fuji 3513 (Constlclip)", "Fuji 3513 (Constlmap)", "Fuji 3513 (Cuspclip)", "Kodak 2383 (Constlclip)", "Kodak 2383 (Constlmap)", "Kodak 2383 (Cuspclip)", "Kodak 2393 (Constlclip)", "Kodak 2393 (Constlmap)", "Kodak 2393 (Cuspclip)"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Slide [Color]",
        default="1",
        items=create_enum(["All [Collage]", "None", "Agfa Precisa 100", "Fuji Astia 100F", "Fuji FP 100C", "Fuji Provia 100F", "Fuji Provia 400F", "Fuji Provia 400X", "Fuji Sensia 100", "Fuji Superia 200 XPRO", "Fuji Velvia 50", "Generic Fuji Astia 100", "Generic Fuji Provia 100", "Generic Fuji Velvia 100", "Generic Kodachrome 64", "Generic Kodak Ektachrome 100 VS", "Kodak E-100 GX Ektachrome 100", "Kodak Ektachrome 100 VS", "Kodak Elite Chrome 200", "Kodak Elite Chrome 400", "Kodak Elite ExtraColor 100", "Kodak Kodachrome 200", "Kodak Kodachrome 25", "Kodak Kodachrome 64", "Lomography X-Pro Slide 200", "Polaroid 669", "Polaroid 690", "Polaroid Polachrome"]),
    ) # type: ignore
    var_prop10: IntProperty(
        name="Thumbnail Size",
        default=512,
        min=0, 
        max=1024, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Strength (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Gamma (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Hue (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Saturation (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop18: EnumProperty(
        name="Normalize Colors",
        default="0",
        items=create_enum(["None", "Pre-Normalize", "Post-Normalize", "Both"]),
    ) # type: ignore
    var_prop20: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_simulate_film {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18},{self.var_prop20},50,50"

################################################################################
################################################################################

class GMIC_FColor_temperaturebalance(GMICBaseNode):
    """Temperature Balance by Author : Garagecoder. Latest update : 2016/08/30."""
    # gcd_temp_balance

    bl_idname = "FColor_temperaturebalance"
    bl_label = "Temperature Balance"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop5"]

    var_prop2: FloatProperty(
        name="Saturation",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Level",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Color",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Lighting",
        default="0",
        items=create_enum(["Automatic", "Automatic [Scan All Hues]", "Standard [No Scan]"]),
    ) # type: ignore

    def create_command(self):
        return f"gcd_temp_balance {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5}"

################################################################################
################################################################################

class GMIC_FColor_tonepresets(GMICBaseNode):
    """Tone Presets by Author : Iain Fergusson. Update: 4 March 2014 - Added parallel processing option"""
    # iain_tone_presets_p

    bl_idname = "FColor_tonepresets"
    bl_label = "Tone Presets"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: EnumProperty(
        name="Preset",
        default="0",
        items=create_enum(["Whiter Whites", "Warm Vintage", "Magenta-Yellow", "Velvetia", "Seventies Magazine", "Faded Print", "Expired 69", "Modern Film"]),
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Strength",
        default=100.0,
        min=-200.0, 
        max=200.0, 
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Scale Output",
        default=0,
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Parallel Processing",
        default="0",
        items=create_enum(["Auto", "Off"]),
    ) # type: ignore

    def create_command(self):
        return f"iain_tone_presets_p {self.var_prop0},{self.var_prop1},{int(self.var_prop2)},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FColor_userdefined(GMICBaseNode):
    """User-Defined by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_custom_transform

    bl_idname = "FColor_userdefined"
    bl_label = "User-Defined"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6"]

    var_prop0: StringProperty(
        name="Red - Green - Blue - Alpha",
        default="i",
    ) # type: ignore
    var_prop1: StringProperty(
        name="Red - Green - Blue",
        default="i + 90*(x/w)*cos(i/10)",
    ) # type: ignore
    var_prop2: StringProperty(
        name="Red",
        default="i",
    ) # type: ignore
    var_prop3: StringProperty(
        name="Green",
        default="i",
    ) # type: ignore
    var_prop4: StringProperty(
        name="Blue",
        default="i",
    ) # type: ignore
    var_prop5: StringProperty(
        name="Alpha",
        default="i",
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Value Normalization",
        default="0",
        items=create_enum(["None", "RGB", "RGBA"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_custom_transform \\\"{self.var_prop0}\\\",\\\"{self.var_prop1}\\\",\\\"{self.var_prop2}\\\",\\\"{self.var_prop3}\\\",\\\"{self.var_prop4}\\\",\\\"{self.var_prop5}\\\",{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FColor_vibrance(GMICBaseNode):
    """Vibrance by Author: Age / Pixls.us. Latest Update: 2022/06/28."""
    # fx_vibrance

    bl_idname = "FColor_vibrance"
    bl_label = "Vibrance"

    node_props = ["var_prop0", "var_prop2"]

    var_prop0: FloatProperty(
        name="Strength",
        default=0.5,
        min=-1.0, 
        max=3.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_vibrance {self.var_prop0},{self.var_prop2},50,50"

################################################################################
################################################################################

class GMIC_FColor_vintagestyle(GMICBaseNode):
    """Vintage Style by Author : Tom Keil. Latest update: 2011/04/06."""
    # fx_tk_vintage

    bl_idname = "FColor_vintagestyle"
    bl_label = "Vintage Style"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop17", "var_prop18", "var_prop20"]

    var_prop0: FloatProperty(
        name="Exposure",
        default=2.0,
        min=-5.0, 
        max=5.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Contrast",
        default=0.85,
        min=0.5, 
        max=1.5, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Saturation",
        default=0.7,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Shadows Threshold",
        default=80.0,
        min=0.0, 
        max=128.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Highlights Threshold",
        default=200.0,
        min=128.0, 
        max=255.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Transition Smoothness",
        default=5.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop7: FloatVectorProperty(
        name="Color Shadows",
        default=(0.5764705882352941,0.10196078431372549,0.6313725490196078),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Strength Shadows",
        default=0.3,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop9: FloatVectorProperty(
        name="Color Midtones",
        default=(0.9215686274509803,0.8627450980392157,0.6901960784313725),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Strength Midtones",
        default=0.4,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop11: FloatVectorProperty(
        name="Color Highlights",
        default=(0.7450980392156863,0.7098039215686275,0.4235294117647059),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Strength Highlights",
        default=0.2,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop13: FloatVectorProperty(
        name="Color Overall Effect",
        default=(0.0,0.0,0.39215686274509803),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop14: EnumProperty(
        name="Color Effect Mode",
        default="0",
        items=create_enum(["exclusion", "overlay", "soft  Light", "multiply", "screen"]),
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Strength Effect",
        default=0.3,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Vignette Size",
        default=25.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Vignette Strenth",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop20: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward  horizontal", "Forward vertical", "Backward horizontal", "Backward vertical"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_tk_vintage {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7[0]*255},{self.var_prop7[1]*255},{self.var_prop7[2]*255},255,{self.var_prop8},{self.var_prop9[0]*255},{self.var_prop9[1]*255},{self.var_prop9[2]*255},255,{self.var_prop10},{self.var_prop11[0]*255},{self.var_prop11[1]*255},{self.var_prop11[2]*255},255,{self.var_prop12},{self.var_prop13[0]*255},{self.var_prop13[1]*255},{self.var_prop13[2]*255},255,{self.var_prop14},{self.var_prop15},{self.var_prop17},{self.var_prop18},{self.var_prop20}"

################################################################################
################################################################################

class GMIC_FColor_zonesystem(GMICBaseNode):
    """Zone System by Author : Tom Keil. Latest update: 2011/13/02."""
    # fx_zonesystem

    bl_idname = "FColor_zonesystem"
    bl_label = "Zone System"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: IntProperty(
        name="Shadows Zone",
        default=1,
        min=1, 
        max=5, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Highlights Zone",
        default=10,
        min=6, 
        max=10, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Gamma",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Contrast",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Black Point",
        default=0,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="White Point",
        default=255,
        min=0, 
        max=255, 
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_zonesystem {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7}"

################################################################################
################################################################################

node_classes = [
    GMIC_FColor_channelprocessing, GMIC_FColor_cmyktone, GMIC_FColor_colorbalance, GMIC_FColor_colorblindness, GMIC_FColor_colorgrading, GMIC_FColor_colorpresets,
    GMIC_FColor_colortemperature, GMIC_FColor_colormap, GMIC_FColor_contrast, GMIC_FColor_customizeclut, GMIC_FColor_darksky, GMIC_FColor_detectskin, GMIC_FColor_equalizehsihslhsv, GMIC_FColor_equalizehsv, GMIC_FColor_hsladjustment,
    GMIC_FColor_huelightendarken, GMIC_FColor_lmsadjustment, GMIC_FColor_localcontrast, GMIC_FColor_metalliclook, GMIC_FColor_mixercmyk, GMIC_FColor_mixerhsv, GMIC_FColor_mixerlab, GMIC_FColor_mixerpca, GMIC_FColor_mixerrgb, GMIC_FColor_mixerycbcr,
    GMIC_FColor_normalizebrightness, GMIC_FColor_retinex, GMIC_FColor_retrofade, GMIC_FColor_rgbtone, GMIC_FColor_saturationeq, GMIC_FColor_selectreplacecolor, GMIC_FColor_selectivedesaturation, GMIC_FColor_sepia, GMIC_FColor_simulatefilm,
    GMIC_FColor_temperaturebalance, GMIC_FColor_tonepresets, GMIC_FColor_userdefined, GMIC_FColor_vibrance, GMIC_FColor_vintagestyle, GMIC_FColor_zonesystem
]

################################################################################