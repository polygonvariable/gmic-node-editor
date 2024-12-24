from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FArt_cutout(GMICBaseNode):
    """Cutout by Authors: David Tschumperlé and Garagecoder Latest Update: 2014/03/06."""
    # fx_cutout

    bl_idname = "FArt_cutout"
    bl_label = "Cutout"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: IntProperty(
        name="Number of Levels",
        default=4,
        min=2, 
        max=32, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Edge Simplicity",
        default=0.5,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Edge Fidelity",
        default=4,
        min=0, 
        max=10, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Normalize",
        default=1,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_cutout {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FArt_diffusiontensors(GMICBaseNode):
    """Diffusion Tensors by Author: David Tschumperlé. Latest Update: 2016/19/10."""
    # fx_diffusiontensors

    bl_idname = "FArt_diffusiontensors"
    bl_label = "Diffusion Tensors"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop10"]

    var_prop0: FloatProperty(
        name="Resolution (%)",
        default=10.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Size",
        default=5.0,
        min=0.0, 
        max=16.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Color Mode",
        default="3",
        items=create_enum(["Monochrome", "Grayscale", "Orientation", "Color"]),
    ) # type: ignore
    var_prop3: IntProperty(
        name="Outline",
        default=1,
        min=0, 
        max=16, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Sharpness",
        default=0.15,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Anisotropy",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Gradient Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Tensor Smoothness",
        default=3.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_diffusiontensors {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop10},50,50"

################################################################################
################################################################################

class GMIC_FArt_dreamsmoothing(GMICBaseNode):
    """Dream Smoothing by  Author: Arto Huotari Latest update : 2014/02/20."""
    # fx_dreamsmooth

    bl_idname = "FArt_dreamsmoothing"
    bl_label = "Dream Smoothing"

    node_props = ["var_prop4", "var_prop5", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop15", "var_prop16", "var_prop18"]

    var_prop4: IntProperty(
        name="Iterations",
        default=3,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Equalize at Each Step",
        default=1,
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Merging Option",
        default="1",
        items=create_enum(["add", "alpha", "and", "average", "blue", "burn", "darken", "difference", "divide", "dodge", "exclusion", "freeze", "grainextract", "grainmerge", "green", "hardlight", "hardmix", "hue", "interpolation", "lighten", "lightness", "linearburn", "linearlight", "luminance", "multiply", "negation", "or", "overlay", "pinlight", "red", "reflect", "saturation", "screen", "shapeaverage", "softburn", "softdodge", "softlight", "stamp", "subtract", "value", "vividlight", "xor", "edges"]),
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Opacity",
        default=0.8,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop10: BoolProperty(
        name="Reverse Order",
        default=0,
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Smoothness",
        default=0.8,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop15: EnumProperty(
        name="Parallel Processing",
        default="1",
        items=create_enum(["Auto", "One thread", "Two threads", "Four threads", "Eight threads", "Sixteen threads"]),
    ) # type: ignore
    var_prop16: IntProperty(
        name="Spatial Overlap",
        default=24,
        min=0, 
        max=256, 
    ) # type: ignore
    var_prop18: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_dreamsmooth {self.var_prop4},{int(self.var_prop5)},{self.var_prop8},{self.var_prop9},{int(self.var_prop10)},{self.var_prop12},{self.var_prop15},{self.var_prop16},{self.var_prop18}"

################################################################################
################################################################################

class GMIC_FArt_ellipsionism(GMICBaseNode):
    """Ellipsionism by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_ellipsionism

    bl_idname = "FArt_ellipsionism"
    bl_label = "Ellipsionism"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Primary Radius",
        default=20.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Secondary Radius",
        default=10.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Opacity",
        default=0.7,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Outline",
        default=3.0,
        min=1.0, 
        max=3.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Density",
        default=0.5,
        min=0.1, 
        max=2.0, 
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_ellipsionism {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FArt_feltpen(GMICBaseNode):
    """Felt Pen by Author: David Tschumperlé. Latest Update: 2012/25/10."""
    # fx_feltpen

    bl_idname = "FArt_feltpen"
    bl_label = "Felt Pen"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=300.0,
        min=0.0, 
        max=4000.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Density",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Opacity",
        default=0.1,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Edge",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Thickness",
        default=5,
        min=2, 
        max=32, 
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_feltpen {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FArt_fingerpaint(GMICBaseNode):
    """Finger Paint by Author: Garry R. Osgood. Latest update: 2015/02/26."""
    # gtutor_fpaint

    bl_idname = "FArt_fingerpaint"
    bl_label = "Finger Paint"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop12"]

    var_prop1: FloatProperty(
        name="Finger Size",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Keep Detail",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Bristle Size",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Edge Detect Includes Chroma",
        default=0,
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Light Direction",
        default=45.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Shadow",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Highlight",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Specular",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"gtutor_fpaint {self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop12}"

################################################################################
################################################################################

class GMIC_FArt_hardsketch(GMICBaseNode):
    """Hard Sketch by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_hardsketchbw

    bl_idname = "FArt_hardsketch"
    bl_label = "Hard Sketch"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=300.0,
        min=0.0, 
        max=4000.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Density",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Opacity",
        default=0.1,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Edge",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Fast Approximation",
        default=0,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Color Model",
        default="4",
        items=create_enum(["Black on white", "White on black", "Black on transparent white", "White on transparent black", "Color on white"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_hardsketchbw {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{self.var_prop6},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FArt_graphicnovel(GMICBaseNode):
    """Graphic Novel by Author: PhotoComiX. Latest update : 2011/13/11."""
    # fx_graphic_novelfxl

    bl_idname = "FArt_graphicnovel"
    bl_label = "Graphic Novel"

    node_props = ["var_prop2", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop10", "var_prop14", "var_prop15", "var_prop17", "var_prop20", "var_prop23", "var_prop24", "var_prop25", "var_prop27", "var_prop31", "var_prop32", "var_prop33", "var_prop34", "var_prop36", "var_prop38", "var_prop39", "var_prop40"]

    var_prop2: BoolProperty(
        name="Skip This Step",
        default=0,
    ) # type: ignore
    var_prop5: FloatProperty(
        name="LN Amplititude",
        default=2.0,
        min=0.0, 
        max=60.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="LN Size",
        default=6.0,
        min=0.0, 
        max=64.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="LN Neightborhood-Smoothness",
        default=5.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="LN Average-Smoothness",
        default=20.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop10: BoolProperty(
        name="Skip All Other Steps",
        default=0,
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Pencil Size",
        default=0.62,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Pencil Amplitude",
        default=14.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop17: BoolProperty(
        name="Skip All Other Steps",
        default=0,
    ) # type: ignore
    var_prop20: BoolProperty(
        name="Activate Pencil Smoother",
        default=1,
    ) # type: ignore
    var_prop23: FloatProperty(
        name="Pencil Smoother Sharpness",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop24: FloatProperty(
        name="Pencil Smoother Edge Protection",
        default=0.78,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop25: FloatProperty(
        name="Pencil Smoother Smoothness",
        default=1.92,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop27: BoolProperty(
        name="Skip All Other Steps",
        default=0,
    ) # type: ignore
    var_prop31: BoolProperty(
        name="Swap Layers",
        default=0,
    ) # type: ignore
    var_prop32: EnumProperty(
        name="MIxer",
        default="0",
        items=create_enum(["Overlay", "Multiply", "Soft light", "Color Burn", "Darken", "Stamp", "Hard Light", "Value", "Grain Merge", "Freeze", "Lightness", "Luminance", "*Colors Doping", "*Comix Colors*", "Graphic Colours", "*Graphix Colors", "*Vivid Edges*", "*Dark Edges*", "*Dark Screen*", "*Vivid Screen*", "Interpolate"]),
    ) # type: ignore
    var_prop33: FloatProperty(
        name="Opacity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop34: FloatProperty(
        name="Intensity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop36: BoolProperty(
        name="Add Painters Touch",
        default=1,
    ) # type: ignore
    var_prop38: FloatProperty(
        name="Painters Touch Sharpness",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop39: FloatProperty(
        name="Painters Edge Protection Flow",
        default=0.8,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop40: FloatProperty(
        name="Painters Smoothness",
        default=1.28,
        min=0.0, 
        max=10.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_graphic_novelfxl {int(self.var_prop2)},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{int(self.var_prop10)},{self.var_prop14},{self.var_prop15},{int(self.var_prop17)},{int(self.var_prop20)},{self.var_prop23},{self.var_prop24},{self.var_prop25},{int(self.var_prop27)},{int(self.var_prop31)},{self.var_prop32},{self.var_prop33},{self.var_prop34},{int(self.var_prop36)},{self.var_prop38},{self.var_prop39},{self.var_prop40}"

################################################################################
################################################################################

class GMIC_FArt_graphicboost(GMICBaseNode):
    """Graphic Boost by Author: PhotoComiX. Latest update : 2011/13/11 ."""
    # fx_graphic_boost4

    bl_idname = "FArt_graphicboost"
    bl_label = "Graphic Boost"

    node_props = ["var_prop2", "var_prop3", "var_prop5", "var_prop10", "var_prop11", "var_prop13", "var_prop16", "var_prop18", "var_prop19", "var_prop20", "var_prop22", "var_prop26", "var_prop28", "var_prop29", "var_prop30", "var_prop32", "var_prop35", "var_prop36", "var_prop37"]

    var_prop2: FloatProperty(
        name="Radius",
        default=1.25,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Darken",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Skip Others Steps",
        default=0,
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Pencil Size",
        default=0.15,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Pencil Amplitude",
        default=14.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop13: BoolProperty(
        name="Skip Others Steps",
        default=0,
    ) # type: ignore
    var_prop16: BoolProperty(
        name="Activate Pencil Smoother",
        default=1,
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Pencil Smoother Sharpness",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Pencil Smoother Edge Protection",
        default=0.45,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Pencil Smoother Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop22: BoolProperty(
        name="Skip Others Steps",
        default=0,
    ) # type: ignore
    var_prop26: BoolProperty(
        name="Swap Layers",
        default=1,
    ) # type: ignore
    var_prop28: EnumProperty(
        name="Merging Option",
        default="0",
        items=create_enum(["Hard Light", "Grain Merge", "Multiply", "Color Burn", "Overlay", "Value", "Darken", "Lightness", "Luminance", "*Colors Doping*", "Comix Colors", "Graphic Colours", "Graphix Colors", "Vivid Edges*", "Dark Edges", "Dark Screen", "Vivid Screen", "Interpolate"]),
    ) # type: ignore
    var_prop29: FloatProperty(
        name="Opacity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop30: FloatProperty(
        name="Intensity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop32: BoolProperty(
        name="Add Painters Touch",
        default=1,
    ) # type: ignore
    var_prop35: FloatProperty(
        name="Painters Touch Sharpness",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop36: FloatProperty(
        name="Painters Edge Protection Flow",
        default=0.45,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop37: FloatProperty(
        name="Painters Smoothness",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_graphic_boost4 {self.var_prop2},{self.var_prop3},{int(self.var_prop5)},{self.var_prop10},{self.var_prop11},{int(self.var_prop13)},{int(self.var_prop16)},{self.var_prop18},{self.var_prop19},{self.var_prop20},{int(self.var_prop22)},{int(self.var_prop26)},{self.var_prop28},{self.var_prop29},{self.var_prop30},{int(self.var_prop32)},{self.var_prop35},{self.var_prop36},{self.var_prop37}"

################################################################################
################################################################################

class GMIC_FArt_ghost(GMICBaseNode):
    """Ghost by Author: David Tschumperlé. Latest Update: 2021/01/30."""
    # fx_ghost

    bl_idname = "FArt_ghost"
    bl_label = "Ghost"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop9", "var_prop11"]

    var_prop1: FloatProperty(
        name="Amplitude",
        default=200.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Coherence",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Gamma",
        default=1.0,
        min=-3.0, 
        max=3.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Amplitude",
        default=3.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Radius",
        default=16.0,
        min=1.0, 
        max=64.0, 
    ) # type: ignore
    var_prop9: BoolProperty(
        name="Invert",
        default=0,
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_ghost {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop7},{self.var_prop8},{int(self.var_prop9)},{self.var_prop11},50,50"

################################################################################
################################################################################

class GMIC_FArt_fractalize(GMICBaseNode):
    """Fractalize by Author: David Tschumperlé. Latest Update: 2014/25/04."""
    # fractalize

    bl_idname = "FArt_fractalize"
    bl_label = "Fractalize"

    node_props = ["var_prop0"]

    var_prop0: FloatProperty(
        name="Detail Level",
        default=0.8,
        min=0.0, 
        max=1.0, 
    ) # type: ignore

    def create_command(self):
        return f"fractalize {self.var_prop0}"

################################################################################
################################################################################

class GMIC_FArt_highlightbloom(GMICBaseNode):
    """Highlight Bloom by Author: David Tschumperlé. Latest Update: 2016/24/10."""
    # fx_highlight_bloom

    bl_idname = "FArt_highlightbloom"
    bl_label = "Highlight Bloom"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Details Strength (%)",
        default=90.0,
        min=0.0, 
        max=400.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Details Scale",
        default=60.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=60.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Highlight (%)",
        default=30,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Contrast (%)",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_highlight_bloom {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FArt_morphologypainting(GMICBaseNode):
    """Morphology Painting by Author : Arto Huotari. Latest update : 2013/09/28."""
    # fx_MorphoPaint

    bl_idname = "FArt_morphologypainting"
    bl_label = "Morphology Painting"

    node_props = ["var_prop5", "var_prop6", "var_prop7", "var_prop10", "var_prop11", "var_prop12", "var_prop15", "var_prop16", "var_prop19", "var_prop20", "var_prop23", "var_prop24", "var_prop25", "var_prop27", "var_prop30", "var_prop31", "var_prop32", "var_prop33", "var_prop34", "var_prop35", "var_prop36", "var_prop38"]

    var_prop5: EnumProperty(
        name="Method",
        default="1",
        items=create_enum(["Erosion", "Dilation", "Opening", "Closing"]),
    ) # type: ignore
    var_prop6: IntProperty(
        name="MorphoStrenght",
        default=18,
        min=2, 
        max=60, 
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Shape",
        default="2",
        items=create_enum(["Square", "Octagonal", "Circular"]),
    ) # type: ignore
    var_prop10: IntProperty(
        name="Black Point",
        default=25,
        min=0, 
        max=50, 
    ) # type: ignore
    var_prop11: IntProperty(
        name="Expand Shadows",
        default=100,
        min=50, 
        max=255, 
    ) # type: ignore
    var_prop12: IntProperty(
        name="Compress Highlights",
        default=230,
        min=200, 
        max=255, 
    ) # type: ignore
    var_prop15: IntProperty(
        name="Spread Amount",
        default=8,
        min=0, 
        max=20, 
    ) # type: ignore
    var_prop16: IntProperty(
        name="Blur Strength",
        default=3,
        min=0, 
        max=10, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Edge Threshold",
        default=4.0,
        min=0.0, 
        max=15.0, 
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop23: IntProperty(
        name="Abstraction",
        default=2,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop24: FloatProperty(
        name="Details Scale",
        default=0.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop25: FloatProperty(
        name="Smoothness",
        default=200.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop27: BoolProperty(
        name="Merge Layers?",
        default=1,
    ) # type: ignore
    var_prop30: BoolProperty(
        name="Enable Paintstroke",
        default=1,
    ) # type: ignore
    var_prop31: FloatProperty(
        name="Stroke Strength",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop32: BoolProperty(
        name="Enable Segmentation",
        default=1,
    ) # type: ignore
    var_prop33: FloatProperty(
        name="Segments Strength",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop34: BoolProperty(
        name="Enable Morphology",
        default=1,
    ) # type: ignore
    var_prop35: FloatProperty(
        name="Morphology Strength",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop36: BoolProperty(
        name="Normalize",
        default=1,
    ) # type: ignore
    var_prop38: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_MorphoPaint {self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop15},{self.var_prop16},{self.var_prop19},{self.var_prop20},{self.var_prop23},{self.var_prop24},{self.var_prop25},{int(self.var_prop27)},{int(self.var_prop30)},{self.var_prop31},{int(self.var_prop32)},{self.var_prop33},{int(self.var_prop34)},{self.var_prop35},{int(self.var_prop36)},{self.var_prop38}"

################################################################################
################################################################################

class GMIC_FArt_makesquiggly(GMICBaseNode):
    """Make Squiggly by Author : Arto Huotari. Latest update : 2013/09/28."""
    # fx_Squiggly

    bl_idname = "FArt_makesquiggly"
    bl_label = "Make Squiggly"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop12", "var_prop13", "var_prop15", "var_prop16", "var_prop17", "var_prop19", "var_prop20", "var_prop21", "var_prop23"]

    var_prop2: FloatProperty(
        name="Spread Noise Amount",
        default=2.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Segmentation Edge Threshold",
        default=12.0,
        min=0.0, 
        max=15.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Segmentation Smoothness",
        default=0.8,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="GradienNormSmoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="GradienNormLinearity",
        default=0.5,
        min=0.0, 
        max=1.5, 
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Invert Luminance",
        default=1,
    ) # type: ignore
    var_prop12: BoolProperty(
        name="Activate Color Enhancement",
        default=0,
    ) # type: ignore
    var_prop13: BoolProperty(
        name="Toggle to View Base Image",
        default=0,
    ) # type: ignore
    var_prop15: FloatProperty(
        name="IncreaseChroma1",
        default=3.0,
        min=1.0, 
        max=4.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Tone Threshold",
        default=0.2,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Tone Gamma",
        default=0.4,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop19: EnumProperty(
        name="Merging Option",
        default="0",
        items=create_enum(["Alpha", "And", "Average", "Burn", "Darken", "Difference", "Divide", "Dodge", "Exclusion", "Freeze", "Grain extract", "Grain merge", "Hard light", "Hue", "Interpolation", "Lighten", "Lightness", "Luminance", "Multiply", "Negation", "Or", "Overlay", "Reflect", "Saturation", "Soft light", "Screen", "Stamp", "Value", "Xor"]),
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Opacity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop21: BoolProperty(
        name="Reverse Order",
        default=1,
    ) # type: ignore
    var_prop23: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_Squiggly {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{int(self.var_prop7)},{int(self.var_prop12)},{int(self.var_prop13)},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop19},{self.var_prop20},{int(self.var_prop21)},{self.var_prop23}"

################################################################################
################################################################################

class GMIC_FArt_lylejkspainting(GMICBaseNode):
    """Lylejks Painting by Authors: Lyle Kroll and David Tschumperlé. Latest Update: 2015/23/02."""
    # fx_lylejk_painting

    bl_idname = "FArt_lylejkspainting"
    bl_label = "Lylejks Painting"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: IntProperty(
        name="Iterations",
        default=10,
        min=1, 
        max=20, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Abstraction",
        default=2,
        min=1, 
        max=20, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Radius",
        default=4,
        min=1, 
        max=30, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Canvas",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_lylejk_painting {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FArt_linify(GMICBaseNode):
    """Linify by Author: David Tschumperlé. Latest Update: 2017/11/21."""
    # fx_linify

    bl_idname = "FArt_linify"
    bl_label = "Linify"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7", "var_prop9"]

    var_prop0: FloatProperty(
        name="Density",
        default=40.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Spreading",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Resolution (%)",
        default=40.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Line Opacity",
        default=10.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Line Precision",
        default=24,
        min=1, 
        max=128, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Color Mode",
        default="0",
        items=create_enum(["Subtractive", "Additive"]),
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Preview Progression While Running",
        default=1,
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_linify {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{int(self.var_prop7)},{self.var_prop9},50,50"

################################################################################
################################################################################

class GMIC_FArt_lineart(GMICBaseNode):
    """Lineart by Author: Claude Lion. Latest Update: 2022/05/10."""
    # cl_lineart

    bl_idname = "FArt_lineart"
    bl_label = "Lineart"

    node_props = ["var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop12", "var_prop14", "var_prop15", "var_prop16", "var_prop18", "var_prop19", "var_prop21", "var_prop23"]

    var_prop3: IntProperty(
        name="Local Contrast Enhancement",
        default=0,
        min=0, 
        max=4, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Simplification",
        default=0,
    ) # type: ignore
    var_prop7: IntProperty(
        name="Flattening for Edge (bilateral)",
        default=2,
        min=0, 
        max=5, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Line Thickness",
        default=1.0,
        min=0.5, 
        max=2.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Line Strength",
        default=15.0,
        min=0.0, 
        max=19.0, 
    ) # type: ignore
    var_prop10: IntProperty(
        name="Lines Antialias",
        default=15,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop12: BoolProperty(
        name="Add Black or Gray",
        default=1,
    ) # type: ignore
    var_prop14: IntProperty(
        name="Luminosity Increase",
        default=0,
        min=0, 
        max=40, 
    ) # type: ignore
    var_prop15: IntProperty(
        name="Final Flattening (bilateral)",
        default=6,
        min=0, 
        max=10, 
    ) # type: ignore
    var_prop16: EnumProperty(
        name="Type",
        default="2",
        items=create_enum(["Soft Threshold", "Gray Patches", "Lines and Black", "Black and Lines"]),
    ) # type: ignore
    var_prop18: EnumProperty(
        name="Final Antialias",
        default="2",
        items=create_enum(["None", "Light Simple", "Simple", "Very Strong"]),
    ) # type: ignore
    var_prop19: EnumProperty(
        name="Pen Drawing",
        default="0",
        items=create_enum(["None", "Simple", "Undoing Patterns"]),
    ) # type: ignore
    var_prop21: EnumProperty(
        name="Effect",
        default="0",
        items=create_enum(["None", "Charcoal", "Groove"]),
    ) # type: ignore
    var_prop23: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"cl_lineart {self.var_prop3},{int(self.var_prop4)},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{int(self.var_prop12)},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop18},{self.var_prop19},{self.var_prop21},{self.var_prop23},50,50"

################################################################################
################################################################################

class GMIC_FArt_illustrationlook(GMICBaseNode):
    """Illustration Look by Authors: Sébastien Guyader and David Tschumperlé. Latest update: 2017/05/01."""
    # fx_illustration_look

    bl_idname = "FArt_illustrationlook"
    bl_label = "Illustration Look"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Strength (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Tone Mapping (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Desaturate (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Vintage Tone (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Output as Multiple Layers",
        default=0,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_illustration_look {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FArt_houghsketch(GMICBaseNode):
    """Hough Sketch by Author: David Tschumperlé. Latest Update: 2023/05/29."""
    # fx_houghsketchbw

    bl_idname = "FArt_houghsketch"
    bl_label = "Hough Sketch"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Smoothness",
        default=1.25,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Density (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Radius",
        default=5,
        min=0, 
        max=30, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Threshold",
        default=80.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Opacity",
        default=0.1,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Color Model",
        default="4",
        items=create_enum(["Black on white", "White on black", "Black on transparent white", "White on transparent black", "Color on white"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_houghsketchbw {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FArt_hopeposter(GMICBaseNode):
    """Hope Poster by Author: David Tschumperlé. Latest Update: 2013/07/11."""
    # fx_poster_hope

    bl_idname = "FArt_hopeposter"
    bl_label = "Hope Poster"

    node_props = ["var_prop0", "var_prop1", "var_prop3"]

    var_prop0: FloatProperty(
        name="Gamma",
        default=0.0,
        min=-3.0, 
        max=3.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=3.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_poster_hope {self.var_prop0},{self.var_prop1},{self.var_prop3},50,50"

################################################################################
################################################################################

class GMIC_FArt_paintwithbrush(GMICBaseNode):
    """Paint With Brush by Author: David Tschumperlé. Latest Update: 2021/08/30."""
    # fx_paint_with_brush

    bl_idname = "FArt_paintwithbrush"
    bl_label = "Paint With Brush"

    node_props = ["var_prop0", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop15", "var_prop17", "var_prop20", "var_prop21", "var_prop22", "var_prop23", "var_prop24", "var_prop25", "var_prop28", "var_prop29", "var_prop30", "var_prop31", "var_prop32", "var_prop33", "var_prop36", "var_prop37", "var_prop38", "var_prop39", "var_prop40", "var_prop41", "var_prop42", "var_prop43", "var_prop45", "var_prop46"]

    var_prop0: EnumProperty(
        name="Predefined style",
        default="0",
        items=create_enum(["Default", "Felt Spots", "Colored Edges", "Circles", "Dreamy", "Fuzzy", "Whirls", "Smooth"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Painting Order",
        default="1",
        items=create_enum(["Random", "Coarse to Fine", "Fine to Coarse"]),
    ) # type: ignore
    var_prop5: IntProperty(
        name="Number of Iterations",
        default=16,
        min=1, 
        max=128, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Precision (%)",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Details (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Background (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Sharpness (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Anisotropy (%)",
        default=80.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=8.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Coherence",
        default=3.0,
        min=0.0, 
        max=16.0, 
    ) # type: ignore
    var_prop13: IntProperty(
        name="Twist Angle (°)",
        default=45,
        min=-1, 
        max=360, 
    ) # type: ignore
    var_prop15: IntProperty(
        name="Twist strength (%)",
        default=0,
        min=-1, 
        max=100, 
    ) # type: ignore
    var_prop17: EnumProperty(
        name="Init Canvas",
        default="6",
        items=create_enum(["Black", "Gray", "White", "Self", "Blur", "Kuwahara", "Vector Painting"]),
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Brush Diameter (px)",
        default=2.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop21: FloatProperty(
        name="Stroke Length (px)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop22: FloatProperty(
        name="Hue Randomness (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop23: FloatProperty(
        name="Saturation Randomness (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop24: FloatProperty(
        name="Value Randomness (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop25: FloatProperty(
        name="Opacity (%)",
        default=60.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop28: FloatProperty(
        name="Brush Diameter (px)",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop29: FloatProperty(
        name="Stroke Length (px)",
        default=1.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop30: FloatProperty(
        name="Hue Randomness (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop31: FloatProperty(
        name="Saturation Randomness (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop32: FloatProperty(
        name="Value Randomness (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop33: FloatProperty(
        name="Opacity (%)",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop36: FloatProperty(
        name="Brush Diameter",
        default=15.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop37: FloatProperty(
        name="Stroke Length",
        default=15.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop38: FloatProperty(
        name="Hue Randomness",
        default=15.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop39: FloatProperty(
        name="Saturation Randomness",
        default=15.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop40: FloatProperty(
        name="Value Randomness",
        default=15.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop41: FloatProperty(
        name="Opacity",
        default=15.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop42: FloatProperty(
        name="Spatial Step",
        default=1.0,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop43: FloatProperty(
        name="Angular Step (°)",
        default=45.0,
        min=0.0, 
        max=90.0, 
    ) # type: ignore
    var_prop45: BoolProperty(
        name="Preview Progression While Running",
        default=0,
    ) # type: ignore
    var_prop46: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_paint_with_brush {self.var_prop0},-1,{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop15},{self.var_prop17},{self.var_prop20},{self.var_prop21},{self.var_prop22},{self.var_prop23},{self.var_prop24},{self.var_prop25},{self.var_prop28},{self.var_prop29},{self.var_prop30},{self.var_prop31},{self.var_prop32},{self.var_prop33},{self.var_prop36},{self.var_prop37},{self.var_prop38},{self.var_prop39},{self.var_prop40},{self.var_prop41},{self.var_prop42},{self.var_prop43},{int(self.var_prop45)},{self.var_prop46},50,50"

################################################################################
################################################################################

class GMIC_FArt_painting(GMICBaseNode):
    """Painting by Authors: Lyle Kroll, Angelo Lama and David Tschumperlé. Latest Update: 2011/02/28."""
    # fx_painting

    bl_idname = "FArt_painting"
    bl_label = "Painting"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: IntProperty(
        name="Abstraction",
        default=5,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Details Scale",
        default=2.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Color",
        default=1.5,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Smoothness",
        default=50.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Sharpen Shades",
        default=1,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_painting {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FArt_pastellart(GMICBaseNode):
    """Pastell Art by Author : Arto Huotari. Latest update : 2013/09/28."""
    # fx_pastell

    bl_idname = "FArt_pastellart"
    bl_label = "Pastell Art"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop13", "var_prop14", "var_prop15", "var_prop17", "var_prop18", "var_prop19", "var_prop21", "var_prop22", "var_prop23", "var_prop25", "var_prop26", "var_prop28"]

    var_prop0: FloatProperty(
        name="MasterOpacity",
        default=0.6,
        min=0.3, 
        max=1.0, 
    ) # type: ignore
    var_prop1: BoolProperty(
        name="BG Textured",
        default=1,
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Reverse Effect",
        default=0,
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Amplitude",
        default=20.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Thickness",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Sharpness",
        default=300.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Orientations",
        default=1,
        min=1, 
        max=36, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Offset",
        default=30.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Color Mode",
        default="1",
        items=create_enum(["Darker", "Lighter"]),
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Linearity",
        default=0.5,
        min=0.0, 
        max=1.5, 
    ) # type: ignore
    var_prop15: BoolProperty(
        name="Negative Colors",
        default=0,
    ) # type: ignore
    var_prop17: BoolProperty(
        name="Activate Shakes",
        default=0,
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Amount",
        default=10.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Strength",
        default=3.0,
        min=1.0, 
        max=300.0, 
    ) # type: ignore
    var_prop21: BoolProperty(
        name="Activate Lizards",
        default=0,
    ) # type: ignore
    var_prop22: FloatProperty(
        name="Toes",
        default=9.0,
        min=0.0, 
        max=300.0, 
    ) # type: ignore
    var_prop23: FloatProperty(
        name="Shivers",
        default=3.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop25: BoolProperty(
        name="Activate Pink elephants",
        default=0,
    ) # type: ignore
    var_prop26: FloatProperty(
        name="Trunks",
        default=12.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop28: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_pastell {self.var_prop0},{int(self.var_prop1)},{int(self.var_prop2)},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop13},{self.var_prop14},{int(self.var_prop15)},{int(self.var_prop17)},{self.var_prop18},{self.var_prop19},{int(self.var_prop21)},{self.var_prop22},{self.var_prop23},{int(self.var_prop25)},{self.var_prop26},{self.var_prop28}"

################################################################################
################################################################################

class GMIC_FArt_pendrawing(GMICBaseNode):
    """Pen Drawing by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_pen_drawing

    bl_idname = "FArt_pendrawing"
    bl_label = "Pen Drawing"

    node_props = ["var_prop0", "var_prop2"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=10.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_pen_drawing {self.var_prop0},{self.var_prop2},50,50"

################################################################################
################################################################################

class GMIC_FArt_photoillustration(GMICBaseNode):
    """Photoillustration by Author: Tom Keil Latest update: 2012/08/28."""
    # fx_tk_photoillustration

    bl_idname = "FArt_photoillustration"
    bl_label = "Photoillustration"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop19", "var_prop20", "var_prop21", "var_prop22", "var_prop23", "var_prop24", "var_prop25", "var_prop26", "var_prop27", "var_prop29"]

    var_prop2: EnumProperty(
        name="Local Contrast Style",
        default="0",
        items=create_enum(["tone mapping", "tone mapping soft", "tone mapping fast", "local  normalisation", "unsharp mask", "global mapping", "dynamic range increase", "none"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Local Contrast Effect",
        default=0.25,
        min=0.00, 
        max=2.5, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Smoothing Style",
        default="0",
        items=create_enum(["anisotropic", "bilateral", "color channel  smoothing", "segmentation", "morphological closing", "selective gaussian", "wavelet", "Kuwahara", "none"]),
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Contour Precision",
        default=0.30,
        min=0.00, 
        max=1.00, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Area Smoothness",
        default=0.50,
        min=0.00, 
        max=10.00, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Sharpening Radius",
        default=0.50,
        min=0.00, 
        max=10.00, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Sharpening Strength",
        default=1.00,
        min=0.00, 
        max=5.00, 
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Special Effects",
        default="0",
        items=create_enum(["none", "soft glow", "dusty", "Orton glow", "extra  smooth", "bloom", "paintstroke"]),
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Effect Strength",
        default=5.00,
        min=0.00, 
        max=20.00, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Overall Lightness",
        default=0.0,
        min=-50.0, 
        max=50.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Overall Contrast",
        default=1.0,
        min=0.5, 
        max=1.5, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Shadows Lightness",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Highlights Lightness",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Mid Tone Contrast",
        default=1.0,
        min=0.5, 
        max=4.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Color Green-Magenta",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Color Blue-Yellow",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Color Boost",
        default=1.2,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Detail Reconstruction Detection",
        default=98.5,
        min=50.0, 
        max=100.0, 
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Detail Reconstruction Smoothness",
        default=5.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop21: FloatProperty(
        name="Detail Reconstruction Strength",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop22: EnumProperty(
        name="Detail Reconstruction Style",
        default="0",
        items=create_enum(["micro/macro details  adjusted", "fine", "strong", "high pass", "artistic round", "artistic hard", "artistic  modern", "comic Style", "gritty", "none"]),
    ) # type: ignore
    var_prop23: BoolProperty(
        name="Keep Detail Layer Separate",
        default=0,
    ) # type: ignore
    var_prop24: BoolProperty(
        name="Remove Artifacts From Micro/Macro Detail",
        default=0,
    ) # type: ignore
    var_prop25: BoolProperty(
        name="Skin Tone Protection",
        default=0,
    ) # type: ignore
    var_prop26: BoolProperty(
        name="Sharpen Edges Only",
        default=0,
    ) # type: ignore
    var_prop27: EnumProperty(
        name="Computation Mode",
        default="1",
        items=create_enum(["high quality", "normal", "high speed"]),
    ) # type: ignore
    var_prop29: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward  horizontal", "Forward vertical", "Backward horizontal", "Backward vertical"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_tk_photoillustration {self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18},{self.var_prop19},{self.var_prop20},{self.var_prop21},{self.var_prop22},{int(self.var_prop23)},{int(self.var_prop24)},{int(self.var_prop25)},{int(self.var_prop26)},{self.var_prop27},{self.var_prop29}"

################################################################################
################################################################################

class GMIC_FArt_polygonizedelaunay(GMICBaseNode):
    """Polygonize [Delaunay] by Author: David Tschumperlé. Latest Update: 2018/06/05."""
    # fx_polygonize_delaunay

    bl_idname = "FArt_polygonizedelaunay"
    bl_label = "Polygonize [Delaunay]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop9"]

    var_prop0: FloatProperty(
        name="Density (%)",
        default=40.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Edges",
        default=5.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Boundaries (%)",
        default=75.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=8.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Filling",
        default="3",
        items=create_enum(["Black", "White", "Random", "Average", "Linear"]),
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Outline (%)",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: FloatVectorProperty(
        name="Outline Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Anti-Aliasing",
        default=1,
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_polygonize_delaunay {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6[0]*255},{self.var_prop6[1]*255},{self.var_prop6[2]*255},255,{int(self.var_prop7)},{self.var_prop9},50,50"

################################################################################
################################################################################

class GMIC_FArt_polygonizeenergy(GMICBaseNode):
    """Polygonize [Energy] by Author: David Tschumperlé. Latest Update: 2013/02/12."""
    # fx_polygonize

    bl_idname = "FArt_polygonizeenergy"
    bl_label = "Polygonize [Energy]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: IntProperty(
        name="Amplitude",
        default=300,
        min=0, 
        max=2000, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Minimal Area",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="X-Resolution",
        default=10.0,
        min=1.0, 
        max=256.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Y-Resolution",
        default=10.0,
        min=1.0, 
        max=256.0, 
    ) # type: ignore
    var_prop5: FloatVectorProperty(
        name="Outline Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_polygonize {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5[0]*255},{self.var_prop5[1]*255},{self.var_prop5[2]*255},255,{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FArt_posteredges(GMICBaseNode):
    """Poster Edges by Authors: David Tschumperlé and David Revoy. Latest Update: 2012/30/11."""
    # fx_poster_edges

    bl_idname = "FArt_posteredges"
    bl_label = "Poster Edges"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="Image Smoothness",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Edge Threshold",
        default=60.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Edge Shade",
        default=5.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Edge Thickness",
        default=0.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Edge Antialiasing",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Posterization Level",
        default=0,
        min=0, 
        max=15, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Posterization Antialiasing",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_poster_edges {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FArt_posterize(GMICBaseNode):
    """Posterize by Author: David Tschumperlé. Latest Update: 2016/25/10."""
    # fx_posterize

    bl_idname = "FArt_posterize"
    bl_label = "Posterize"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="Smoothness",
        default=150.0,
        min=0.0, 
        max=800.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Edges (%)",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Paint",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Colors",
        default=12,
        min=2, 
        max=256, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Minimal Area",
        default=0,
        min=0, 
        max=64, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Outline (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Normalize Colors",
        default=0,
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_posterize {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{int(self.var_prop6)},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FArt_posterizeddithering(GMICBaseNode):
    """Posterized Dithering by Author: PhotoComiX. Latest update : 2010/29/12."""
    # fx_pdithered

    bl_idname = "FArt_posterizeddithering"
    bl_label = "Posterized Dithering"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop9"]

    var_prop0: FloatProperty(
        name="Gamma",
        default=1.0,
        min=0.01, 
        max=5.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Contrast",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Brightness",
        default=0.0,
        min=-255.0, 
        max=255.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Quantize Colors",
        default=20,
        min=2, 
        max=255, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Smooth Colors",
        default=1.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Mixer Mode",
        default="0",
        items=create_enum(["Color Doping", "Darken", "Soft Light", "Grain Merge", "Multiply", "Value"]),
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Color Intensity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_pdithered {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop9}"

################################################################################
################################################################################

class GMIC_FArt_quadtreevariations(GMICBaseNode):
    """Quadtree Variations by Author: David Tschumperlé. Latest Update: 2017/15/06."""
    # fx_quadtree

    bl_idname = "FArt_quadtreevariations"
    bl_label = "Quadtree Variations"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop11"]

    var_prop0: EnumProperty(
        name="Mode",
        default="0",
        items=create_enum(["Squares", "Sierpinksi Design", "Ellipse Painting"]),
    ) # type: ignore
    var_prop1: IntProperty(
        name="Precision",
        default=1024,
        min=2, 
        max=4096, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Homogeneity",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Outline",
        default=0,
        min=0, 
        max=4, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Primary Radius",
        default=3.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Secondary Radius",
        default=1.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Anisotropy",
        default=1.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop9: BoolProperty(
        name="Only Leafs",
        default=1,
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_quadtree {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop6},{self.var_prop7},{self.var_prop8},{int(self.var_prop9)},{self.var_prop11},50,50"

################################################################################
################################################################################

class GMIC_FArt_rodilius(GMICBaseNode):
    """Rodilius by Authors: David Tschumperlé and Rod/GimpChat. Latest Update: 2013/05/03."""
    # fx_rodilius

    bl_idname = "FArt_rodilius"
    bl_label = "Rodilius"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop11"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=10.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Thickness",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Sharpness",
        default=300.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Orientations",
        default=5,
        min=2, 
        max=36, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Offset",
        default=30.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Smoothness",
        default=0,
        min=0, 
        max=5, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Color Mode",
        default="1",
        items=create_enum(["Darker", "Lighter"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_rodilius {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop11},50,50"

################################################################################
################################################################################

class GMIC_FArt_sharpabstract(GMICBaseNode):
    """Sharp Abstract by Author: David Tschumperlé. Latest Update: 2016/20/09."""
    # fx_sharp_abstract

    bl_idname = "FArt_sharpabstract"
    bl_label = "Sharp Abstract"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Spatial Scale",
        default=4.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Value Scale",
        default=10.0,
        min=0.0, 
        max=16.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Precision",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_sharp_abstract {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FArt_simplenoisecanvas(GMICBaseNode):
    """Simple Noise Canvas by Author : Arto Huotari. Latest update : 2013/09/28."""
    # fx_SimpleNoiseCanvas

    bl_idname = "FArt_simplenoisecanvas"
    bl_label = "Simple Noise Canvas"

    node_props = ["var_prop2", "var_prop5", "var_prop6", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop16", "var_prop17", "var_prop18", "var_prop20", "var_prop21", "var_prop22", "var_prop23", "var_prop25"]

    var_prop2: FloatProperty(
        name="Scale Factor",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Amplitude",
        default=3.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Noise Type",
        default="2",
        items=create_enum(["Gaussian", "Uniform", "Salt and Pepper", "Poisson"]),
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Horisontal Length",
        default=5.0,
        min=2.0, 
        max=15.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Vertical Length",
        default=5.0,
        min=2.0, 
        max=15.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Overall Blur",
        default=0.0,
        min=0.0, 
        max=15.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Canvas Brightness",
        default=255.0,
        min=230.0, 
        max=255.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Canvas Darkness",
        default=0.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop16: EnumProperty(
        name="Merging Option",
        default="2",
        items=create_enum(["Average", "Multiply", "Darken", "Edges"]),
    ) # type: ignore
    var_prop17: BoolProperty(
        name="Invert Canvas Colors",
        default=0,
    ) # type: ignore
    var_prop18: BoolProperty(
        name="Invert Image Colors",
        default=0,
    ) # type: ignore
    var_prop20: BoolProperty(
        name="Reverse Order",
        default=0,
    ) # type: ignore
    var_prop21: EnumProperty(
        name="Merging Option",
        default="1",
        items=create_enum(["Avg", "Multiply", "Scr", "Darken", "Lighten", "Dif", "Negation", "Exclusion", "Overlay", "Hardlight", "Softlight", "Dodge", "Colorburn", "Reflect", "Freeze", "Stamp", "Interpolate", "Grainext", "Grainmerge", "Xor", "Edges", "DoNothing"]),
    ) # type: ignore
    var_prop22: BoolProperty(
        name="Preserve Canvas for Post Bump Mapping",
        default=0,
    ) # type: ignore
    var_prop23: FloatVectorProperty(
        name="Canvas Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop25: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_SimpleNoiseCanvas {self.var_prop2},{self.var_prop5},{self.var_prop6},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop16},{int(self.var_prop17)},{int(self.var_prop18)},{int(self.var_prop20)},{self.var_prop21},{int(self.var_prop22)},{self.var_prop23[0]*255},{self.var_prop23[1]*255},{self.var_prop23[2]*255},255,{self.var_prop25}"

################################################################################
################################################################################

class GMIC_FArt_skeletik(GMICBaseNode):
    """Skeletik by samj - Update : 2019/12/14."""
    # samj_Test_Skeletik

    bl_idname = "FArt_skeletik"
    bl_label = "Skeletik"

    node_props = ["var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop10", "var_prop13", "var_prop14"]

    var_prop3: IntProperty(
        name="Itérations",
        default=10,
        min=1, 
        max=50, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Skeleton",
        default=1,
        min=1, 
        max=20, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Deform",
        default=0.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop6: IntProperty(
        name="Dilate",
        default=0,
        min=0, 
        max=16, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Spread",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Mode",
        default="3",
        items=create_enum(["Add", "Alpha", "And", "Average", "Blue", "Burn", "Darken", "Difference", "Divide", "Dodge", "Edges", "Exclusion", "Freeze", "Grain extract", "Grain merge", "Green", "Hard light", "Hard mix", "Hue", "Interpolation", "Lighten", "Lightness", "Linear burn", "Linear light", "Luminance", "Multiply", "Negation", "Or", "Overlay", "Pin light", "Red", "Reflect", "Saturation", "Shape area max", "Shape area max0", "Shape area min", "Shape area min0", "Shape average", "Shape average0", "Shape min", "Shape min0", "Shape max", "Shape max0", "Soft burn", "Soft dodge", "Soft light", "Screen", "Stamp", "Subtract", "Value", "Vivid light", "Xor"]),
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Lines",
        default=1.0,
        min=0.75, 
        max=1.25, 
    ) # type: ignore
    var_prop14: FloatVectorProperty(
        name="Background Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore

    def create_command(self):
        return f"samj_Test_Skeletik {self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop10},{self.var_prop13},{self.var_prop14[0]*255},{self.var_prop14[1]*255},{self.var_prop14[2]*255},255"

################################################################################
################################################################################

class GMIC_FArt_sketch(GMICBaseNode):
    """Sketch by Author: David Tschumperlé. Latest Update: 2018/05/11."""
    # fx_sketchbw

    bl_idname = "FArt_sketch"
    bl_label = "Sketch"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop17"]

    var_prop0: IntProperty(
        name="Number of Orientations",
        default=3,
        min=1, 
        max=16, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Starting Angle",
        default=45.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Angle Range",
        default=180.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Stroke Length",
        default=30.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Contour Threshold",
        default=1.75,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Opacity",
        default=0.02,
        min=0.0, 
        max=0.3, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Background Intensity",
        default=0.5,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Density",
        default=0.75,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Sharpness",
        default=0.1,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Anisotropy",
        default=0.7,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Smoothness",
        default=3.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Coherence",
        default=6.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop12: BoolProperty(
        name="Boost Stroke",
        default=0,
    ) # type: ignore
    var_prop13: BoolProperty(
        name="Curved Stroke",
        default=1,
    ) # type: ignore
    var_prop14: EnumProperty(
        name="Color Model",
        default="4",
        items=create_enum(["Black on white", "White on black", "Black on transparent white", "White on transparent black", "Color on white"]),
    ) # type: ignore
    var_prop15: IntProperty(
        name="Random Seed",
        default=0,
        min=0, 
        max=65535, 
    ) # type: ignore
    var_prop17: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_sketchbw {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{int(self.var_prop12)},{int(self.var_prop13)},{self.var_prop14},{self.var_prop15},{self.var_prop17},50,50"

################################################################################
################################################################################

class GMIC_FArt_smoothabstract(GMICBaseNode):
    """Smooth Abstract by Author: David Tschumperlé. Latest Update: 2016/06/04."""
    # fx_smooth_abstract

    bl_idname = "FArt_smoothabstract"
    bl_label = "Smooth Abstract"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Smoothness (%)",
        default=75.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Regularization",
        default="0",
        items=create_enum(["Isotropic", "Delaunay-Guided", "Edge-Oriented"]),
    ) # type: ignore
    var_prop2: IntProperty(
        name="Regularization Iterations",
        default=20,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Geometry",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Details",
        default=30.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_smooth_abstract {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FArt_vectorpainting(GMICBaseNode):
    """Vector Painting by Author: David Tschumperlé. Latest Update: 2015/08/25."""
    # fx_vector_painting

    bl_idname = "FArt_vectorpainting"
    bl_label = "Vector Painting"

    node_props = ["var_prop0", "var_prop2"]

    var_prop0: FloatProperty(
        name="Details",
        default=9.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_vector_painting {self.var_prop0},{self.var_prop2},50,50"

################################################################################
################################################################################

class GMIC_FArt_warhol(GMICBaseNode):
    """Warhol by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # warhol

    bl_idname = "FArt_warhol"
    bl_label = "Warhol"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3"]

    var_prop0: IntProperty(
        name="X-Tiles",
        default=3,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Y-Tiles",
        default=3,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Color",
        default=40.0,
        min=0.0, 
        max=60.0, 
    ) # type: ignore

    def create_command(self):
        return f"warhol {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3}"

################################################################################
################################################################################

class GMIC_FArt_whirldrawing(GMICBaseNode):
    """Whirl Drawing by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_draw_whirl

    bl_idname = "FArt_whirldrawing"
    bl_label = "Whirl Drawing"

    node_props = ["var_prop0", "var_prop2"]

    var_prop0: FloatProperty(
        name="Amplitude",
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
        return f"fx_draw_whirl {self.var_prop0},{self.var_prop2},50,50"

################################################################################
################################################################################

node_classes = [
    GMIC_FArt_cutout, GMIC_FArt_diffusiontensors, GMIC_FArt_dreamsmoothing, GMIC_FArt_ellipsionism, GMIC_FArt_feltpen, GMIC_FArt_fingerpaint, GMIC_FArt_hardsketch, GMIC_FArt_graphicnovel, GMIC_FArt_graphicboost, GMIC_FArt_ghost, GMIC_FArt_fractalize, GMIC_FArt_highlightbloom, GMIC_FArt_morphologypainting, GMIC_FArt_makesquiggly, GMIC_FArt_lylejkspainting, GMIC_FArt_linify, GMIC_FArt_lineart, GMIC_FArt_illustrationlook, GMIC_FArt_houghsketch, GMIC_FArt_hopeposter, GMIC_FArt_paintwithbrush, GMIC_FArt_painting, GMIC_FArt_pastellart, GMIC_FArt_pendrawing, GMIC_FArt_photoillustration, GMIC_FArt_polygonizedelaunay, GMIC_FArt_polygonizeenergy, GMIC_FArt_posteredges, GMIC_FArt_posterize, GMIC_FArt_posterizeddithering, GMIC_FArt_quadtreevariations, GMIC_FArt_rodilius, GMIC_FArt_sharpabstract, GMIC_FArt_simplenoisecanvas, GMIC_FArt_skeletik, GMIC_FArt_sketch, GMIC_FArt_smoothabstract, GMIC_FArt_vectorpainting, GMIC_FArt_warhol, GMIC_FArt_whirldrawing
]

################################################################################