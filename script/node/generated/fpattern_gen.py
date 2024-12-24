from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FPattern_bayerfilter(GMICBaseNode):
    """Bayer Filter by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # rgb2bayer

    bl_idname = "FPattern_bayerfilter"
    bl_label = "Bayer Filter"

    node_props = ["var_prop0", "var_prop1"]

    var_prop0: EnumProperty(
        name="Starting Pattern",
        default="0",
        items=create_enum(["Red-Green", "Blue-Green", "Green-Red", "Green-Blue"]),
    ) # type: ignore
    var_prop1: BoolProperty(
        name="Keep Colors",
        default=1,
    ) # type: ignore

    def create_command(self):
        return f"rgb2bayer {self.var_prop0},{int(self.var_prop1)}"

################################################################################
################################################################################

class GMIC_FPattern_boxfitting(GMICBaseNode):
    """Box Fitting by Author: David Tschumperlé. Latest Update: 2013/06/06."""
    # fx_boxfitting

    bl_idname = "FPattern_boxfitting"
    bl_label = "Box Fitting"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop5"]

    var_prop0: IntProperty(
        name="Minimal Size",
        default=3,
        min=1, 
        max=32, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Maximal Size",
        default=0,
        min=0, 
        max=32, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Initial Density",
        default=0.25,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Minimal Spacing",
        default=2,
        min=1, 
        max=16, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Transparency",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_boxfitting {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)}"

################################################################################
################################################################################

class GMIC_FPattern_camouflage(GMICBaseNode):
    """Camouflage by Author: David Tschumperlé. Latest Update: 2016/26/10."""
    # fx_camouflage

    bl_idname = "FPattern_camouflage"
    bl_label = "Camouflage"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6"]

    var_prop0: IntProperty(
        name="Scale",
        default=9,
        min=2, 
        max=12, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Levels",
        default=12,
        min=2, 
        max=32, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Coherence",
        default=100.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop3: FloatVectorProperty(
        name="Color 1",
        default=(0.11764705882352941,0.1803921568627451,0.12941176470588237),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop4: FloatVectorProperty(
        name="Color 2",
        default=(0.29411764705882354,0.35294117647058826,0.2549019607843137),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop5: FloatVectorProperty(
        name="Color 3",
        default=(0.7019607843137254,0.7411764705882353,0.4588235294117647),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop6: FloatVectorProperty(
        name="Color 4",
        default=(1.0,0.9647058823529412,0.6196078431372549),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore

    def create_command(self):
        return f"fx_camouflage {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3[0]*255},{self.var_prop3[1]*255},{self.var_prop3[2]*255},{self.var_prop4[0]*255},{self.var_prop4[1]*255},{self.var_prop4[2]*255},{self.var_prop5[0]*255},{self.var_prop5[1]*255},{self.var_prop5[2]*255},{self.var_prop6[0]*255},{self.var_prop6[1]*255},{self.var_prop6[2]*255}"

################################################################################
################################################################################

class GMIC_FPattern_canvas(GMICBaseNode):
    """Canvas by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_canvas

    bl_idname = "FPattern_canvas"
    bl_label = "Canvas"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop10"]

    var_prop1: FloatProperty(
        name="Amplitude",
        default=70.0,
        min=0.0, 
        max=300.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Angle",
        default=45.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Sharpness",
        default=400.0,
        min=0.0, 
        max=2000.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Activate Second Direction",
        default=1,
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Amplitude",
        default=70.0,
        min=0.0, 
        max=300.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Angle",
        default=135.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Sharpness",
        default=400.0,
        min=0.0, 
        max=2000.0, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_canvas {self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop5)},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop10},50,50"

################################################################################
################################################################################

class GMIC_FPattern_canvastexture(GMICBaseNode):
    """Canvas Texture by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # texturize_canvas

    bl_idname = "FPattern_canvastexture"
    bl_label = "Canvas Texture"

    node_props = ["var_prop0", "var_prop1", "var_prop2"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=20.0,
        min=0.0, 
        max=256.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Fibrousness",
        default=3.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Emboss",
        default=0.6,
        min=0.0, 
        max=1.0, 
    ) # type: ignore

    def create_command(self):
        return f"texturize_canvas {self.var_prop0},{self.var_prop1},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FPattern_clouds(GMICBaseNode):
    """Clouds by Author : Jérôme Boulanger. Latest update: 2013/05/29."""
    # jeje_clouds

    bl_idname = "FPattern_clouds"
    bl_label = "Clouds"

    node_props = ["var_prop0", "var_prop1"]

    var_prop0: FloatProperty(
        name="Density",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore

    def create_command(self):
        return f"jeje_clouds {self.var_prop0},{self.var_prop1}"

################################################################################
################################################################################

class GMIC_FPattern_cracks(GMICBaseNode):
    """Cracks by Author: David Tschumperlé. Latest Update: 2016/20/07."""
    # fx_cracks

    bl_idname = "FPattern_cracks"
    bl_label = "Cracks"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop2_alpha", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Density (%)",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: BoolProperty(
        name="Relief",
        default=1,
    ) # type: ignore
    var_prop2: FloatVectorProperty(
        name="Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop2_alpha: FloatProperty(
        name="Color",
        default=0.5019607843137255,
        
        max=1, 
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
        return f"fx_cracks {self.var_prop0},{int(self.var_prop1)},{self.var_prop2[0]*255},{self.var_prop2[1]*255},{self.var_prop2[2]*255},{self.var_prop2_alpha*255},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FPattern_crystal(GMICBaseNode):
    """Crystal by Author: David Tschumperlé. Latest Update: 2015/19/01."""
    # fx_crystal

    bl_idname = "FPattern_crystal"
    bl_label = "Crystal"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Density",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=0.2,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Edges",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Fast Fill",
        default=1,
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_crystal {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FPattern_crystalbackground(GMICBaseNode):
    """Crystal Background by Author: David Tschumperlé. Latest Update: 2016/18/10."""
    # fx_crystal_background

    bl_idname = "FPattern_crystalbackground"
    bl_label = "Crystal Background"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: IntProperty(
        name="Iterations",
        default=10,
        min=1, 
        max=32, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Density (%)",
        default=25.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Random Seed",
        default=0,
        min=0, 
        max=65535, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Opacity (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Color",
        default=1,
    ) # type: ignore

    def create_command(self):
        return f"fx_crystal_background {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)}"

################################################################################
################################################################################

class GMIC_FPattern_denimtexture(GMICBaseNode):
    """Denim Texture by samj - Version : 2020/10/24."""
    # Denim_samj

    bl_idname = "FPattern_denimtexture"
    bl_label = "Denim Texture"

    node_props = ["var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop12", "var_prop12_alpha"]

    var_prop2: IntProperty(
        name="Dimension motif base",
        default=5,
        min=2, 
        max=30, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Dilatation Motif / Pattern",
        default=2,
        min=0, 
        max=5, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Retourner Motif / Flip Pattern",
        default=0,
    ) # type: ignore
    var_prop5: IntProperty(
        name="Déformation 1",
        default=40,
        min=0, 
        max=200, 
    ) # type: ignore
    var_prop6: IntProperty(
        name="Déformation 2",
        default=40,
        min=0, 
        max=200, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Denim [bruit/noise]",
        default=25,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Usure [bruit/noise]",
        default=50,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Netteté / Sharpness",
        default=0.0,
        min=0.0, 
        max=500.0, 
    ) # type: ignore
    var_prop12: FloatVectorProperty(
        name="Couleur Denim",
        default=(0.16862745098039217,0.4235294117647059,0.49411764705882355),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop12_alpha: FloatProperty(
        name="Couleur Denim",
        default=1.0,
        
        max=1, 
    ) # type: ignore

    def create_command(self):
        return f"Denim_samj {self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop12[0]*255},{self.var_prop12[1]*255},{self.var_prop12[2]*255},{self.var_prop12_alpha*255}"

################################################################################
################################################################################

class GMIC_FPattern_fibers(GMICBaseNode):
    """Fibers by Author : Jérôme Boulanger. Latest update: 2015/07/17."""
    # jeje_fibers

    bl_idname = "FPattern_fibers"
    bl_label = "Fibers"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: IntProperty(
        name="Number",
        default=10,
        min=1, 
        max=100, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Length",
        default=50,
        min=1, 
        max=100, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_fibers {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FPattern_freqypattern(GMICBaseNode):
    """Freqy Pattern by Author : Jérôme Boulanger. Latest update: 2018/09/25."""
    # jeje_freqy_pattern

    bl_idname = "FPattern_freqypattern"
    bl_label = "Freqy Pattern"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: FloatProperty(
        name="Random",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Scale 1",
        default=33.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Scale 2",
        default=50.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_freqy_pattern {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FPattern_halftone(GMICBaseNode):
    """Halftone by Author: David Tschumperlé. Latest Update: 2012/23/07."""
    # fx_halftone

    bl_idname = "FPattern_halftone"
    bl_label = "Halftone"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop13"]

    var_prop1: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Gamma (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Number of Tones",
        default=5,
        min=2, 
        max=32, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Size for Dark Tones",
        default=8,
        min=2, 
        max=256, 
    ) # type: ignore
    var_prop9: IntProperty(
        name="Size for Bright Tones",
        default=8,
        min=2, 
        max=256, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Shape",
        default="5",
        items=create_enum(["Square", "Diamond", "Circle", "Square (Inv.)", "Diamond (Inv.)", "Circle (Inv.)"]),
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Smoothness",
        default=0.1,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_halftone {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop13},50,50"

################################################################################
################################################################################

class GMIC_FPattern_halftonegeneric(GMICBaseNode):
    """Halftone [Generic] by Author: David Tschumperlé. Latest Update: 2022/11/07."""
    # fx_generic_halftone

    bl_idname = "FPattern_halftonegeneric"
    bl_label = "Halftone [Generic]"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13"]

    var_prop1: EnumProperty(
        name="Background",
        default="0",
        items=create_enum(["Black", "White"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Base shape",
        default="1",
        items=create_enum(["Square", "Disc"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Max Radius (%)",
        default=100.0,
        min=0.0, 
        max=300.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Antialiasing",
        default="1",
        items=create_enum(["None", "x1.25", "x1.5", "x2", "x2.5"]),
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Black &amp; White",
        default=0,
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Shape",
        default="4",
        items=create_enum(["Custom (Top Layer)", "Dots", "Lines", "Self", "Spiral"]),
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Layout",
        default="0",
        items=create_enum(["Regular", "Semi-Regular", "Random"]),
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Density (%)",
        default=75.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Smoothness (%)",
        default=1.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_generic_halftone {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{int(self.var_prop6)},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},-1"

################################################################################
################################################################################

class GMIC_FPattern_halftoneshapes(GMICBaseNode):
    """Halftone Shapes by """
    # iain_halftone_shapes

    bl_idname = "FPattern_halftoneshapes"
    bl_label = "Halftone Shapes"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6"]

    var_prop0: FloatProperty(
        name="Scale",
        default=100.0,
        min=5.0, 
        max=200.0, 
    ) # type: ignore
    var_prop1: BoolProperty(
        name="Negative",
        default=0,
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Shape",
        default="0",
        items=create_enum(["Circle", "Star", "Triangle", "Heart"]),
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Oversample",
        default=0,
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Rotate",
        default=0.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Twirl",
        default=0.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Turn on rotate and twirl",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"iain_halftone_shapes {self.var_prop0},{int(self.var_prop1)},{self.var_prop2},{int(self.var_prop3)},{self.var_prop4},{self.var_prop5},{int(self.var_prop6)}"

################################################################################
################################################################################

class GMIC_FPattern_hearts(GMICBaseNode):
    """Hearts by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_hearts

    bl_idname = "FPattern_hearts"
    bl_label = "Hearts"

    node_props = ["var_prop0", "var_prop2", "var_prop4"]

    var_prop0: FloatProperty(
        name="Density",
        default=2.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_hearts {self.var_prop0},{self.var_prop2},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FPattern_hedcut(GMICBaseNode):
    """Hedcut by Author: Garry R. Osgood. Latest update: 2015/03/05."""
    # hedcut

    bl_idname = "FPattern_hedcut"
    bl_label = "Hedcut"

    node_props = ["var_prop1", "var_prop2", "var_prop5", "var_prop6", "var_prop7", "var_prop9", "var_prop10", "var_prop12"]

    var_prop1: FloatProperty(
        name="Contrast",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Luminance Level",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Smoothing",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Size",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Step",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop9: BoolProperty(
        name="Quality",
        default=0,
    ) # type: ignore
    var_prop10: BoolProperty(
        name="Force Gray",
        default=1,
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"hedcut {self.var_prop1},{self.var_prop2},{self.var_prop5},{self.var_prop6},{self.var_prop7},{int(self.var_prop9)},{int(self.var_prop10)},{self.var_prop12}"

################################################################################
################################################################################

class GMIC_FPattern_lava(GMICBaseNode):
    """Lava by Author: David Tschumperlé. Latest Update: 2012/26/11."""
    # fx_lava

    bl_idname = "FPattern_lava"
    bl_label = "Lava"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: IntProperty(
        name="Perturbation",
        default=8,
        min=0, 
        max=15, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=5.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Scale",
        default=3.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Sharpness",
        default=0.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_lava {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},50,50"

################################################################################
################################################################################

class GMIC_FPattern_marble(GMICBaseNode):
    """Marble by Author: Preben Soeberg. Latest Update: 2010/29/12."""
    # fx_marble

    bl_idname = "FPattern_marble"
    bl_label = "Marble"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9"]

    var_prop0: FloatProperty(
        name="Image Weight",
        default=.5,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Pattern Weight",
        default=1.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Pattern Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Amplitude",
        default=0.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Sharpness",
        default=.4,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Anisotropy",
        default=.6,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Alpha",
        default=.6,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Sigma",
        default=1.1,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Cut Low",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Cut High",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_marble {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9}"

################################################################################
################################################################################

class GMIC_FPattern_maze(GMICBaseNode):
    """Maze by Author: David Tschumperlé. Latest Update: 2011/02/09."""
    # fx_maze

    bl_idname = "FPattern_maze"
    bl_label = "Maze"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: IntProperty(
        name="Cell Size",
        default=24,
        min=1, 
        max=256, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Thickness",
        default=1,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Masking",
        default="0",
        items=create_enum(["None", "Render on Dark Areas", "Render on White Areas"]),
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Preserve Image Dimension",
        default=1,
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Maze Type",
        default="0",
        items=create_enum(["Dark Walls", "White Walls"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_maze {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FPattern_mineralmosaic(GMICBaseNode):
    """Mineral Mosaic by Author: David Tschumperlé. Latest Update: 2013/01/02."""
    # fx_mineral_mosaic

    bl_idname = "FPattern_mineralmosaic"
    bl_label = "Mineral Mosaic"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: FloatProperty(
        name="Density",
        default=1.0,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Area",
        default=2.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Shade Strength",
        default=100.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Shade Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_mineral_mosaic {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FPattern_mosaic(GMICBaseNode):
    """Mosaic by Author: David Tschumperlé. Latest Update: 2016/19/07."""
    # fx_mosaic

    bl_idname = "FPattern_mosaic"
    bl_label = "Mosaic"

    node_props = ["var_prop0", "var_prop2", "var_prop4"]

    var_prop0: FloatProperty(
        name="Density (%)",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_mosaic {self.var_prop0},{self.var_prop2},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FPattern_opart(GMICBaseNode):
    """Op Art by Author: David Tschumperlé. Latest Update: 2013/16/12."""
    # fx_shapes

    bl_idname = "FPattern_opart"
    bl_label = "Op Art"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop13"]

    var_prop0: EnumProperty(
        name="Shape",
        default="1",
        items=create_enum(["Custom Layers", "Circles", "Squares", "Diamonds", "Triangles", "Horizontal Stripes", "Vertical Stripes", "Balls", "Hearts", "Stars", "Arrows", "Truchet", "Circles (Outline)", "Squares (Outline)", "Diamonds (Outline)", "Triangles (Outline)", "Hearts (Outline)", "Stars (Outline)", "Arrows (Outline)"]),
    ) # type: ignore
    var_prop1: IntProperty(
        name="Number of Scales",
        default=16,
        min=2, 
        max=24, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Resolution",
        default=10.0,
        min=1.0, 
        max=50.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Zoom Factor",
        default=2,
        min=1, 
        max=8, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Minimal Size",
        default=5.0,
        min=0.0, 
        max=150.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Maximal Size",
        default=90.0,
        min=0.0, 
        max=150.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Stencil Type",
        default="0",
        items=create_enum(["Black &amp; White", "RGB", "Color"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Allow Angle",
        default="0",
        items=create_enum(["0 deg.", "90 deg.", "180 deg."]),
    ) # type: ignore
    var_prop8: BoolProperty(
        name="Negative",
        default=1,
    ) # type: ignore
    var_prop9: BoolProperty(
        name="Antialiasing",
        default=1,
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_shapes {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{int(self.var_prop8)},{int(self.var_prop9)},{self.var_prop13}"

################################################################################
################################################################################

class GMIC_FPattern_packellipses(GMICBaseNode):
    """Pack Ellipses by Author: David Tschumperlé. Latest Update: 2023/03/29."""
    # fx_pack_ellipses

    bl_idname = "FPattern_packellipses"
    bl_label = "Pack Ellipses"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop8_alpha", "var_prop9", "var_prop10"]

    var_prop0: FloatProperty(
        name="Min Radius (px)",
        default=3.0,
        min=1.0, 
        max=256.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Max Radius (px)",
        default=20.0,
        min=1.0, 
        max=256.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Radius Dilation/Erosion (px)",
        default=0.0,
        min=-10.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Min Isotropy (%)",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Max Isotropy (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Isotropy Quantization",
        default=6,
        min=0, 
        max=16, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Orientation",
        default="1",
        items=create_enum(["Isotropic (Circles Only)", "Anisotropic (Along Contours)", "Anisotropic (Orthogonal to Contours)"]),
    ) # type: ignore
    var_prop7: IntProperty(
        name="Region Analysis Size",
        default=3,
        min=0, 
        max=10, 
    ) # type: ignore
    var_prop8: FloatVectorProperty(
        name="Background Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop8_alpha: FloatProperty(
        name="Background Color",
        default=1.0,
        
        max=1, 
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Render Resolution",
        default="0",
        items=create_enum(["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]),
    ) # type: ignore
    var_prop10: BoolProperty(
        name="Preserve Image Size",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_pack_ellipses {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8[0]*255},{self.var_prop8[1]*255},{self.var_prop8[2]*255},{self.var_prop8_alpha*255},{self.var_prop9},{int(self.var_prop10)}"

################################################################################
################################################################################

class GMIC_FPattern_papertexture(GMICBaseNode):
    """Paper Texture by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_paper

    bl_idname = "FPattern_papertexture"
    bl_label = "Paper Texture"

    node_props = ["var_prop0", "var_prop2"]

    var_prop0: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_paper {self.var_prop0},{self.var_prop2},50,50"

################################################################################
################################################################################

class GMIC_FPattern_periodicdots(GMICBaseNode):
    """Periodic Dots by Author : Jérôme Boulanger. Latest update: 2013/05/29."""
    # jeje_periodic_dots

    bl_idname = "FPattern_periodicdots"
    bl_label = "Periodic Dots"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: IntProperty(
        name="Number",
        default=6,
        min=2, 
        max=32, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Scale",
        default=4.0,
        min=1.0, 
        max=12.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Repeat",
        default=1,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Map",
        default="0",
        items=create_enum(["None", "default", "HSV", "lines", "hot", "cool", "jet", "flag", "cube"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_periodic_dots {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FPattern_pills(GMICBaseNode):
    """Pills by Authors: Miloslav Číž and David Tschumperlé. Latest Update: 2022/11/08."""
    # fx_pills

    bl_idname = "FPattern_pills"
    bl_label = "Pills"

    node_props = ["var_prop0", "var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop11", "var_prop12", "var_prop15", "var_prop16"]

    var_prop0: EnumProperty(
        name="Mode",
        default="0",
        items=create_enum(["Gray", "RGB"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Cycles",
        default=4.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Cycles",
        default=4.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Cycles",
        default=4.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Cycles",
        default=4.0,
        min=0.0, 
        max=32.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_pills {self.var_prop0},{self.var_prop3},{self.var_prop4},{self.var_prop7},{self.var_prop8},{self.var_prop11},{self.var_prop12},{self.var_prop15},{self.var_prop16}"

################################################################################
################################################################################

class GMIC_FPattern_plaid(GMICBaseNode):
    """Plaid by Author: David Tschumperlé. Latest Update: 2011/16/05."""
    # fx_plaid_texture

    bl_idname = "FPattern_plaid"
    bl_label = "Plaid"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5"]

    var_prop0: FloatProperty(
        name="Line",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Number of Angles",
        default=2,
        min=1, 
        max=8, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Starting Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Angle Range",
        default=90.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Sharpen",
        default=300.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_plaid_texture {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5}"

################################################################################
################################################################################

class GMIC_FPattern_polkadots(GMICBaseNode):
    """Polka Dots by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_polka_dots

    bl_idname = "FPattern_polkadots"
    bl_label = "Polka Dots"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop8_alpha"]

    var_prop0: FloatProperty(
        name="Size",
        default=80.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Density",
        default=20.0,
        min=0.1, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="First Offset",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Second Offset",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Aliasing",
        default=0.5,
        min=0.1, 
        max=1.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Shading",
        default=0.1,
        min=0.1, 
        max=1.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Opacity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop8: FloatVectorProperty(
        name="Color",
        default=(1.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop8_alpha: FloatProperty(
        name="Color",
        default=1.0,
        
        max=1, 
    ) # type: ignore

    def create_command(self):
        return f"fx_polka_dots {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8[0]*255},{self.var_prop8[1]*255},{self.var_prop8[2]*255},{self.var_prop8_alpha*255}"

################################################################################
################################################################################

class GMIC_FPattern_randomcolorellipses(GMICBaseNode):
    """Random Color Ellipses by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_color_ellipses

    bl_idname = "FPattern_randomcolorellipses"
    bl_label = "Random Color Ellipses"

    node_props = ["var_prop0", "var_prop1", "var_prop2"]

    var_prop0: IntProperty(
        name="Density",
        default=400,
        min=0, 
        max=3000, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Radius",
        default=8.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Opacity",
        default=0.1,
        min=0.01, 
        max=0.5, 
    ) # type: ignore

    def create_command(self):
        return f"fx_color_ellipses {self.var_prop0},{self.var_prop1},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FPattern_rays(GMICBaseNode):
    """Rays by Author : Jérôme Boulanger. Latest update: 2023/07/13."""
    # jeje_rays

    bl_idname = "FPattern_rays"
    bl_label = "Rays"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="X Center",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Y Center",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Frequency",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Proportion",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: FloatVectorProperty(
        name="Color 1",
        default=(1.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop6: FloatVectorProperty(
        name="Color 2",
        default=(1.0,1.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_rays {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5[0]*255},{self.var_prop5[1]*255},{self.var_prop5[2]*255},{self.var_prop6[0]*255},{self.var_prop6[1]*255},{self.var_prop6[2]*255},{self.var_prop8}"

################################################################################
################################################################################

class GMIC_FPattern_reptile(GMICBaseNode):
    """Reptile by samj - Dernière mise à jour : 2020/10/24."""
    # samj_reptile

    bl_idname = "FPattern_reptile"
    bl_label = "Reptile"

    node_props = ["var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop11"]

    var_prop3: EnumProperty(
        name="Forme",
        default="0",
        items=create_enum(["hexagonal", "grid", "triangular Ha", "triangular Hb", "triangular Va", "triangular Vb"]),
    ) # type: ignore
    var_prop4: IntProperty(
        name="Résolution",
        default=64,
        min=1, 
        max=256, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Spread",
        default=25,
        min=5, 
        max=100, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Color",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Orientation",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Light",
        default=40,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Opacity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore

    def create_command(self):
        return f"samj_reptile {self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop11}"

################################################################################
################################################################################

class GMIC_FPattern_resynthetizetexturefft(GMICBaseNode):
    """Resynthetize Texture [FFT] by Authors: David Tschumperlé and Jérome Boulanger. Latest Update: 2014/09/04."""
    # syntexturize

    bl_idname = "FPattern_resynthetizetexturefft"
    bl_label = "Resynthetize Texture [FFT]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: IntProperty(
        name="Width",
        default=1024,
        min=32, 
        max=8192, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Height",
        default=1024,
        min=32, 
        max=8192, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Equalize Light",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"syntexturize {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FPattern_resynthetizetexturepatchbased(GMICBaseNode):
    """Resynthetize Texture [Patch-Based] by Author: David Tschumperlé. Latest Update: 2015/22/10."""
    # syntexturize_matchpatch

    bl_idname = "FPattern_resynthetizetexturepatchbased"
    bl_label = "Resynthetize Texture [Patch-Based]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: IntProperty(
        name="Width",
        default=512,
        min=32, 
        max=8192, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Height",
        default=512,
        min=32, 
        max=8192, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Number of Scales",
        default=0,
        min=0, 
        max=16, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Patch Size",
        default=7,
        min=1, 
        max=32, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Blending Size",
        default=5,
        min=1, 
        max=24, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Precision",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Equalize Light",
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
        return f"syntexturize_matchpatch {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FPattern_rorschach(GMICBaseNode):
    """Rorschach by Author: David Tschumperlé. Latest Update: 2011/12/03."""
    # fx_rorschach

    bl_idname = "FPattern_rorschach"
    bl_label = "Rorschach"

    node_props = ["var_prop0", "var_prop1", "var_prop2"]

    var_prop0: FloatProperty(
        name="Scale",
        default=3.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Mirror",
        default="1",
        items=create_enum(["None", "X-Axis", "Y-Axis", "XY-Axes"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Stencil Type",
        default="2",
        items=create_enum(["Black &amp; White", "RGB", "Color"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_rorschach {self.var_prop0},{self.var_prop1},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FPattern_satin(GMICBaseNode):
    """Satin by Author: David Tschumperlé. Latest Update: 2017/11/27."""
    # fx_satin

    bl_idname = "FPattern_satin"
    bl_label = "Satin"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop4_alpha", "var_prop5", "var_prop5_alpha", "var_prop6", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12"]

    var_prop0: IntProperty(
        name="Iterations",
        default=20,
        min=4, 
        max=128, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness (%)",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Seed",
        default=0,
        min=0, 
        max=65535, 
    ) # type: ignore
    var_prop4: FloatVectorProperty(
        name="Dark Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop4_alpha: FloatProperty(
        name="Dark Color",
        default=1.0,
        
        max=1, 
    ) # type: ignore
    var_prop5: FloatVectorProperty(
        name="Light Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop5_alpha: FloatProperty(
        name="Light Color",
        default=1.0,
        
        max=1, 
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Stretch Contrast",
        default=0,
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Gamma (%)",
        default=-50.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Hue (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Saturation (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_satin {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4[0]*255},{self.var_prop4[1]*255},{self.var_prop4[2]*255},{self.var_prop4_alpha*255},{self.var_prop5[0]*255},{self.var_prop5[1]*255},{self.var_prop5[2]*255},{self.var_prop5_alpha*255},{int(self.var_prop6)},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12}"

################################################################################
################################################################################

class GMIC_FPattern_seamlessdeco(GMICBaseNode):
    """Seamless Deco by Author: PhotoComix. Latest update : 2011/13/11."""
    # fx_mad_rorscharchp

    bl_idname = "FPattern_seamlessdeco"
    bl_label = "Seamless Deco"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop5", "var_prop7", "var_prop8", "var_prop9", "var_prop13"]

    var_prop0: FloatProperty(
        name="Scale",
        default=3.0,
        min=0.0, 
        max=15.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Mixer",
        default="0",
        items=create_enum(["Average", "Grain Extract", "Vivid Edges", "Difference", "Exclusion", "Negation"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Line",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Sharpen",
        default=300.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Remix",
        default="0",
        items=create_enum(["Vivid Edges", "Average", "Difference", "Negation", "Dark Edges"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="PhotoComix Preset",
        default="0",
        items=create_enum(["Neat Merge", "Lighty Smooth", "Dream", "Moody", "Soft", "Naif", "Dark Boost", "Whitening", "None- Skip"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Activate Mirror",
        default="0",
        items=create_enum(["No-Skip", "XY Mirror", "2XY Mirror"]),
    ) # type: ignore
    var_prop13: BoolProperty(
        name="Expanding Mirrors",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_mad_rorscharchp {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop7},{self.var_prop8},{self.var_prop9},{int(self.var_prop13)}"

################################################################################
################################################################################

class GMIC_FPattern_seamlessturbulence(GMICBaseNode):
    """Seamless Turbulence by Author: David Tschumperlé. Latest Update: 2013/02/04."""
    # fx_seamless_turbulence

    bl_idname = "FPattern_seamlessturbulence"
    bl_label = "Seamless Turbulence"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=15.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=20.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Orientation",
        default=0.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Deviation",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Contrast",
        default=3.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Color Rendering",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_seamless_turbulence {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)}"

################################################################################
################################################################################

class GMIC_FPattern_shockwaves(GMICBaseNode):
    """Shock Waves by Author: David Tschumperlé. Latest Update: 2014/01/12."""
    # fx_shockwaves

    bl_idname = "FPattern_shockwaves"
    bl_label = "Shock Waves"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Low Frequency",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Frequency Range",
        default=20.0,
        min=0.0, 
        max=100.0, 
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
        return f"fx_shockwaves {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FPattern_softrandomshades(GMICBaseNode):
    """Soft Random Shades by samj - Latest update : 2016/12/06."""
    # samj_Soft_Random_Shades

    bl_idname = "FPattern_softrandomshades"
    bl_label = "Soft Random Shades"

    node_props = ["var_prop2", "var_prop2_alpha", "var_prop3", "var_prop4", "var_prop5"]

    var_prop2: FloatVectorProperty(
        name="Background Color",
        default=(0.5490196078431373,0.47058823529411764,0.8627450980392157),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop2_alpha: FloatProperty(
        name="Background Color",
        default=1.0,
        
        max=1, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Variation A",
        default=0,
        min=0, 
        max=4, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Variation B",
        default=20,
        min=20, 
        max=120, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Variation C",
        default=0.0,
        min=0.0, 
        max=0.25, 
    ) # type: ignore

    def create_command(self):
        return f"samj_Soft_Random_Shades {self.var_prop2[0]*255},{self.var_prop2[1]*255},{self.var_prop2[2]*255},{self.var_prop2_alpha*255},{self.var_prop3},{self.var_prop4},{self.var_prop5}"

################################################################################
################################################################################

class GMIC_FPattern_sponge(GMICBaseNode):
    """Sponge by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_sponge

    bl_idname = "FPattern_sponge"
    bl_label = "Sponge"

    node_props = ["var_prop0", "var_prop2", "var_prop4"]

    var_prop0: IntProperty(
        name="Size",
        default=13,
        min=3, 
        max=21, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_sponge {self.var_prop0},{self.var_prop2},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FPattern_stainedglass(GMICBaseNode):
    """Stained Glass by Author: David Tschumperlé. Latest Update: 2011/18/03."""
    # fx_stained_glass

    bl_idname = "FPattern_stainedglass"
    bl_label = "Stained Glass"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop10"]

    var_prop0: FloatProperty(
        name="Edges (%)",
        default=40.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Shading",
        default=0.1,
        min=0.0, 
        max=0.5, 
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Thin Separators",
        default=0,
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Equalize",
        default=1,
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Colors",
        default=1.0,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Brightness (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Contrast (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Gamma (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_stained_glass {self.var_prop0},{self.var_prop1},{int(self.var_prop2)},{int(self.var_prop4)},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop10},50,50"

################################################################################
################################################################################

class GMIC_FPattern_stars(GMICBaseNode):
    """Stars by Author: David Tschumperlé. Latest Update: 2012/01/10."""
    # fx_stars

    bl_idname = "FPattern_stars"
    bl_label = "Stars"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop6_alpha"]

    var_prop0: FloatProperty(
        name="Density",
        default=10.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Depth",
        default=0.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Size",
        default=32,
        min=8, 
        max=128, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Branches",
        default=5,
        min=3, 
        max=16, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Thickness",
        default=0.38,
        min=0.1, 
        max=1.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop6: FloatVectorProperty(
        name="Color",
        default=(1.0,1.0,0.39215686274509803),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop6_alpha: FloatProperty(
        name="Color",
        default=0.7843137254901961,
        
        max=1, 
    ) # type: ignore

    def create_command(self):
        return f"fx_stars {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6[0]*255},{self.var_prop6[1]*255},{self.var_prop6[2]*255},{self.var_prop6_alpha*255}"

################################################################################
################################################################################

class GMIC_FPattern_stencil(GMICBaseNode):
    """Stencil by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_stencil

    bl_idname = "FPattern_stencil"
    bl_label = "Stencil"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Radius",
        default=3.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Iterations",
        default=8,
        min=1, 
        max=100, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Aliasing",
        default=0.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Stencil Type",
        default="2",
        items=create_enum(["Black &amp; White", "RGB", "Color"]),
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Transparency",
        default=0,
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_stencil {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop5)},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FPattern_strip(GMICBaseNode):
    """Strip by Author : Jérôme Boulanger. Latest update: 2013/06/07."""
    # jeje_strip

    bl_idname = "FPattern_strip"
    bl_label = "Strip"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5"]

    var_prop0: FloatProperty(
        name="Angle",
        default=45.0,
        min=0.0, 
        max=90.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Frequency",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Phase",
        default=0.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Amplitude",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Preview type",
        default="0",
        items=create_enum(["Full", "Forward horizontal", "Forward vertical", "Backward horizontal", "Backward vertical", "Duplicate top", "Duplicate left", "Duplicate bottom", "Duplicate right", "Duplicate horizontal", "Duplicate vertical", "Checkered", "Checkered inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"jeje_strip {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5}"

################################################################################
################################################################################

class GMIC_FPattern_tetris(GMICBaseNode):
    """Tetris by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_tetris

    bl_idname = "FPattern_tetris"
    bl_label = "Tetris"

    node_props = ["var_prop0"]

    var_prop0: IntProperty(
        name="Scale",
        default=10,
        min=1, 
        max=20, 
    ) # type: ignore

    def create_command(self):
        return f"fx_tetris {self.var_prop0}"

################################################################################
################################################################################

class GMIC_FPattern_triangularpattern(GMICBaseNode):
    """Triangular Pattern by Author: David Tschumperlé. Latest Update: 2021/09/29."""
    # fx_triangular_pattern

    bl_idname = "FPattern_triangularpattern"
    bl_label = "Triangular Pattern"

    node_props = ["var_prop0", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop10", "var_prop11", "var_prop11_alpha", "var_prop12"]

    var_prop0: IntProperty(
        name="Random Seed",
        default=43,
        min=0, 
        max=65535, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Depth",
        default=7,
        min=0, 
        max=16, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Split Type-1",
        default=4,
        min=0, 
        max=20, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Split Type-2",
        default=4,
        min=0, 
        max=20, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Split Type-3",
        default=4,
        min=0, 
        max=20, 
    ) # type: ignore
    var_prop6: IntProperty(
        name="Split Type-4",
        default=0,
        min=0, 
        max=20, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Split Type-5",
        default=0,
        min=0, 
        max=20, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Holes Probability (Type-5) (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Filling opacity (%)",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop11: FloatVectorProperty(
        name="Outline Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop11_alpha: FloatProperty(
        name="Outline Color",
        default=0.6274509803921569,
        
        max=1, 
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Anti-aliasing",
        default="1",
        items=create_enum(["None", "x1.5", "x2", "x3", "x4"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_triangular_pattern {self.var_prop0},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop10},{self.var_prop11[0]*255},{self.var_prop11[1]*255},{self.var_prop11[2]*255},{self.var_prop11_alpha*255},{self.var_prop12}"

################################################################################
################################################################################

class GMIC_FPattern_truchet(GMICBaseNode):
    """Truchet by Author: David Tschumperlé. Latest Update: 2011/26/10."""
    # fx_truchet

    bl_idname = "FPattern_truchet"
    bl_label = "Truchet"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: IntProperty(
        name="Scale",
        default=32,
        min=1, 
        max=256, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Radius",
        default=5,
        min=1, 
        max=64, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Type",
        default="1",
        items=create_enum(["Straight", "Curved"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Color",
        default="0",
        items=create_enum(["White on Black", "Black on White", "White on Transparent", "Black on Transparent", "Transparent on White", "Transparent on Black", "Random"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_truchet {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FPattern_turbulenthalftone(GMICBaseNode):
    """Turbulent Halftone by Older updates: 2018/08/24."""
    # iain_turbulent_halftone

    bl_idname = "FPattern_turbulenthalftone"
    bl_label = "Turbulent Halftone"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=15.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=20.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Orientation",
        default=0.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Deviation",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Tile Size",
        default=512,
        min=128, 
        max=2048, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Blob Size",
        default=0.75,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Colour Model",
        default="0",
        items=create_enum(["RGB", "CMYK", "Luminance"]),
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Enhance Detail",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: BoolProperty(
        name="Oversample",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"iain_turbulent_halftone {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{int(self.var_prop8)}"

################################################################################
################################################################################

class GMIC_FPattern_voronoi(GMICBaseNode):
    """Voronoi by Author: David Tschumperlé. Latest Update: 2020/04/30."""
    # fx_voronoi

    bl_idname = "FPattern_voronoi"
    bl_label = "Voronoi"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop7", "var_prop7_alpha", "var_prop8", "var_prop9", "var_prop9_alpha", "var_prop11"]

    var_prop0: FloatProperty(
        name="Threshold",
        default=160.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Threshold on",
        default="1",
        items=create_enum(["Pixel values", "Gradient values"]),
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Subsampling (%)",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Flat color",
        default="3",
        items=create_enum(["Black", "White", "Transparent", "Image"]),
    ) # type: ignore
    var_prop6: IntProperty(
        name="Outline thickness",
        default=1,
        min=0, 
        max=8, 
    ) # type: ignore
    var_prop7: FloatVectorProperty(
        name="Outline color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop7_alpha: FloatProperty(
        name="Outline color",
        default=0.39215686274509803,
        
        max=1, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Centers radius",
        default=2,
        min=0, 
        max=10, 
    ) # type: ignore
    var_prop9: FloatVectorProperty(
        name="Centers color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop9_alpha: FloatProperty(
        name="Centers color",
        default=0.1568627450980392,
        
        max=1, 
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Anti-aliasing",
        default="1",
        items=create_enum(["x1 (none)", "x1.5", "x2", "x2.5"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_voronoi {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop6},{self.var_prop7[0]*255},{self.var_prop7[1]*255},{self.var_prop7[2]*255},{self.var_prop7_alpha*255},{self.var_prop8},{self.var_prop9[0]*255},{self.var_prop9[1]*255},{self.var_prop9[2]*255},{self.var_prop9_alpha*255},{self.var_prop11}"

################################################################################
################################################################################

class GMIC_FPattern_weave(GMICBaseNode):
    """Weave by Author: David Tschumperlé. Latest Update: 2013/18/01."""
    # weave

    bl_idname = "FPattern_weave"
    bl_label = "Weave"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8"]

    var_prop0: IntProperty(
        name="Density",
        default=6,
        min=1, 
        max=32, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Thickness",
        default=65.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Shadow",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Shading",
        default=0.5,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Fibers Amplitude",
        default=0.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Fibers Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Angle",
        default="0",
        items=create_enum(["0 deg.", "22.5 deg.", "45 deg.", "67.5 deg."]),
    ) # type: ignore
    var_prop7: FloatProperty(
        name="X-Curvature",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Y-Curvature",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore

    def create_command(self):
        return f"weave {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8}"

################################################################################
################################################################################

class GMIC_FPattern_whirls(GMICBaseNode):
    """Whirls by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_whirls

    bl_idname = "FPattern_whirls"
    bl_label = "Whirls"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop7"]

    var_prop0: IntProperty(
        name="Density",
        default=7,
        min=3, 
        max=20, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Darkness",
        default=0.2,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Lightness",
        default=1.8,
        min=1.0, 
        max=3.0, 
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
        return f"fx_whirls {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

node_classes = [
    GMIC_FPattern_bayerfilter, GMIC_FPattern_boxfitting, GMIC_FPattern_camouflage, GMIC_FPattern_canvas, GMIC_FPattern_canvastexture, GMIC_FPattern_clouds, GMIC_FPattern_cracks, GMIC_FPattern_crystal, GMIC_FPattern_crystalbackground, GMIC_FPattern_denimtexture, GMIC_FPattern_fibers, GMIC_FPattern_freqypattern, GMIC_FPattern_halftone, GMIC_FPattern_halftonegeneric, GMIC_FPattern_halftoneshapes, GMIC_FPattern_hearts, GMIC_FPattern_hedcut, GMIC_FPattern_lava, GMIC_FPattern_marble, GMIC_FPattern_maze, GMIC_FPattern_mineralmosaic, GMIC_FPattern_mosaic, GMIC_FPattern_opart, GMIC_FPattern_packellipses, GMIC_FPattern_papertexture, GMIC_FPattern_periodicdots, GMIC_FPattern_pills, GMIC_FPattern_plaid, GMIC_FPattern_polkadots, GMIC_FPattern_randomcolorellipses, GMIC_FPattern_rays, GMIC_FPattern_reptile, GMIC_FPattern_resynthetizetexturefft, GMIC_FPattern_resynthetizetexturepatchbased, GMIC_FPattern_rorschach, GMIC_FPattern_satin, GMIC_FPattern_seamlessdeco, GMIC_FPattern_seamlessturbulence, GMIC_FPattern_shockwaves, GMIC_FPattern_softrandomshades, GMIC_FPattern_sponge, GMIC_FPattern_stainedglass, GMIC_FPattern_stars, GMIC_FPattern_stencil, GMIC_FPattern_strip, GMIC_FPattern_tetris, GMIC_FPattern_triangularpattern, GMIC_FPattern_truchet, GMIC_FPattern_turbulenthalftone, GMIC_FPattern_voronoi, GMIC_FPattern_weave, GMIC_FPattern_whirls
]

################################################################################