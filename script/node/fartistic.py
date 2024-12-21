from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty )

from ..base.node import GMICBaseNode, create_enum

class FArt_AngoisseAnguish(GMICBaseNode):
    """Angoisse Anguish by Samj"""
    # samj_Angoisse 1,5,0,5,100,2,4,1,250

    bl_idname = "GMIC_FArt_AngoisseAnguish"
    bl_label = "Angoisse Anguish"

    node_props = ["iteration", "sigma1", "sigma2", "segment_threshold", "smooth_amplitude", "noise_amplitude", "noise_type", "opacity", "sharp_amplitude"]

    iteration: IntProperty(name="Iteration", default=1, min=0, max=3) # type: ignore
    sigma1: FloatProperty(name="Sigma 1", default=5, min=0.0, max=10.0) # type: ignore
    sigma2: FloatProperty(name="Sigma 2", default=0.0, min=0.0, max=10.0) # type: ignore
    segment_threshold: FloatProperty(name="Segment Threshold", default=5, min=0.0, max=10.0) # type: ignore
    smooth_amplitude: FloatProperty(name="Smooth Amplitude", default=100.0, min=0.0, max=200.0) # type: ignore
    noise_amplitude: FloatProperty(name="Noise Amplitude", default=2.0, min=0.0, max=200.0) # type: ignore
    noise_type: EnumProperty(
        name="Noise Type",
        items=create_enum(["Gaussian", "Uniform", "Salt & Pepper", "Poission", "Rice"]),
        default="4"
    ) # type: ignore
    opacity: FloatProperty(name="Opacity", default=1.0, min=0.0, max=1.0) # type: ignore
    sharp_amplitude: FloatProperty(name="Sharp Amplitude", default=250.0, min=0.0, max=500.0) # type: ignore

    def create_command(self):
        return "samj_Angoisse {0},{1},{2},{3},{4},{5},{6},{7},{8}".format(
            self.iteration,
            self.sigma1,
            self.sigma2,
            self.segment_threshold,
            self.smooth_amplitude,
            self.noise_amplitude,
            self.noise_type,
            self.opacity,
            self.sharp_amplitude
        )

class FArt_Aurora(GMICBaseNode):
    """Aurora by Garagecoder"""
    # gcd_aurora 6,1,0
    
    bl_idname = "GMIC_FArt_Aurora"
    bl_label = "Aurora"

    node_props = ["vertical", "horizontal", "blend"]

    vertical: FloatProperty(name="Vertical", default=45.0, min=0.0, max=50.0) # type: ignore
    horizontal: FloatProperty(name="Horizontal", default=0.1, min=0.0, max=50.0) # type: ignore
    blend: EnumProperty(
        name="Blend Mode",
        items=create_enum(["None", "Average"]),
        default="0"
    ) # type: ignore

    def create_command(self):
        return "gcd_aurora {0},{1},{2}".format(
            self.vertical,
            self.horizontal,
            self.blend
        )

class FArt_BarbouillagePaintDaub(GMICBaseNode):
    """Barbouillage Paint Daub by Samj"""
    # samj_Barbouillage_Paint_Daub 2,2,100,0.2,1,4,1,0,8
    
    bl_idname = "GMIC_FArt_BarbouillagePaintDaub"
    bl_label = "Barbouillage Paint Daub"

    node_props = ["iteration", "amplitude", "sharpness", "anisotropy", "sigma", "di", "plasma", "opacity", "sharp_amplitude"]

    iteration: IntProperty(name="Iteration", default=2, min=0, max=3) # type: ignore
    amplitude: FloatProperty(name="Amplitude", default=2.0, min=0.0, max=5.0) # type: ignore
    sharpness: FloatProperty(name="Sharpness", default=100.0, min=0.0, max=500.0) # type: ignore
    anisotropy: FloatProperty(name="Anisotropy", default=0.2, min=0.0, max=0.5) # type: ignore
    sigma: FloatProperty(name="Sigma", default=1.0, min=0.0, max=10.0) # type: ignore
    di: FloatProperty(name="DI", default=4.0, min=0.0, max=10.0) # type: ignore
    plasma: EnumProperty(
        name="Plasma",
        items=create_enum(["None", "Couleurs A", "Couleurs B"]),
        default="0"
    ) # type: ignore
    plasmaScale: FloatProperty(name="Plasma Scale", default=0.0, min=0.0, max=50.0) # type: ignore

    def create_command(self):
        return "samj_Barbouillage_Paint_Daub {0},{1},{2},{3},{4},{5},{6},{7},{8}".format(
            self.iteration,
            self.amplitude,
            self.sharpness,
            self.anisotropy,
            self.sigma,
            self.di,
            1,
            self.plasma,
            self.plasmaScale,
        )

class FArt_BlackCrayonGraffiti(GMICBaseNode):
    """Black Crayon Graffiti by PhotoComiX"""
    # fx_crayongraffiti2 300,50,1,0.4,12,1,2,2,0
    
    bl_idname = "GMIC_FArt_BlackCrayonGraffiti"
    bl_label = "Black Crayon Graffiti"

    node_props = ["iteration", "amplitude", "sharpness", "anisotropy", "sigma", "di", "plasma", "opacity", "sharp_amplitude"]

    amplitude: IntProperty(name="Amplitude", default=300, min=0, max=4000) # type: ignore
    density: FloatProperty(name="Density", default=50.0, min=0.0, max=100.0) # type: ignore
    smooth: FloatProperty(name="Smooth", default=1.0, min=0.0, max=10.0) # type: ignore
    opacity: FloatProperty(name="Opacity", default=0.4, min=0.0, max=1.0) # type: ignore
    edge: FloatProperty(name="Edge", default=12.0, min=0.0, max=50.0) # type: ignore
    approx: EnumProperty(
        name="Approximation",
        items=create_enum(["No", "Yes"]),
        default="1"
    ) # type: ignore
    colorSmooth: FloatProperty(name="Color Smooth", default=2.0, min=0.0, max=30.0) # type: ignore
    mix: EnumProperty(
        name="Mix Style",
        items=create_enum(["Lightness", "Value", "Color Doping"]),
        default="2"
    ) # type: ignore


    def create_command(self):
        return "fx_crayongraffiti2 {0},{1},{2},{3},{4},{5},{6},{7},{8}".format(
            self.amplitude,
            self.density,
            self.smooth,
            self.opacity,
            self.edge,
            self.approx,
            self.colorSmooth,
            self.mix,
            0
        )

class FArt_Blockism(GMICBaseNode):
    """Blockism by Arto Huotari"""
    # fx_blockism 3,1.6,0.5,50,0.5,64,0,1,0
    
    bl_idname = "GMIC_FArt_Blockism"
    bl_label = "Blockism"

    node_props = ["size", "ratio", "variance", "count", "opacity", "tolerance", "reverse", "color"]

    size: FloatProperty(name="Size", default=3.0, min=0.0, max=20.0) # type: ignore
    ratio: FloatProperty(name="Ratio", default=1.6, min=0.0, max=10.0) # type: ignore
    variance: FloatProperty(name="Variance", default=0.5, min=0.0, max=10.0) # type: ignore
    count: IntProperty(name="Count", default=50, min=0, max=500) # type: ignore
    opacity: FloatProperty(name="Opacity", default=0.5, min=0.0, max=1.0) # type: ignore
    tolerance: IntProperty(name="Tolerance", default=64, min=0, max=255) # type: ignore
    reverse: BoolProperty(name="Reverse", default=False) # type: ignore
    color: EnumProperty(
        name="Color",
        items=create_enum(["Lab", "RGB"]),
        default="1"
    ) # type: ignore

    def create_command(self):
        return "fx_blockism {0},{1},{2},{3},{4},{5},{6},{7},{8}".format(
            self.size,
            self.ratio,
            self.variance,
            self.count,
            self.opacity,
            self.tolerance,
            int(self.reverse),
            self.color,
            0
        )

class FArt_Brushify(GMICBaseNode):
    """Brushify by David Tschumperlé"""
    # fx_brushify 7,0.25,4,64,25,12,0,2,4,0.2,0.5,30,1,1,1,5,0,0.2,0
    
    bl_idname = "GMIC_FArt_Brushify"
    bl_label = "Bruishify"

    node_props = ["shape", "ratio", "numSize", "maxSize", "minSize", "numOrientations", "fuzzy", "smoothness", "lightType", "lightStrength", "opacity", "density", "contour", "orientation", "gradient", "structure", "angle", "angleDispersion"]

    shape: EnumProperty(
        name="Shape",
        items=create_enum(["Reactangle", "Diamond", "Pentagon", "Hexagon", "Octagon", "Ellipse", "Gaussian", "Star", "Heart"]),
        default="5"
    ) # type: ignore
    ratio: FloatProperty(name="Ratio", default=0.25, min=0.0, max=1.0) # type: ignore
    numSize: IntProperty(name="Number Size", default=4, min=0, max=16) # type: ignore
    maxSize: IntProperty(name="Max Size", default=64, min=0, max=128) # type: ignore
    minSize: IntProperty(name="Min Size", default=25, min=0, max=100) # type: ignore
    numOrientations: IntProperty(name="Number Orientations", default=12, min=0, max=24) # type: ignore
    fuzzy: FloatProperty(name="Fuzzy", default=0.0, min=0.0, max=10.0) # type: ignore
    smoothness: FloatProperty(name="Smoothness", default=2.0, min=0.0, max=10.0) # type: ignore
    lightType: EnumProperty(
        name="Light Type",
        items=create_enum(["None", "Flat", "Dark", "Light", "Full"]),
        default="4"
    ) # type: ignore
    lightStrength: FloatProperty(name="Light Strength", default=0.2, min=0.0, max=1.0) # type: ignore
    opacity: FloatProperty(name="Opacity", default=0.5, min=0.0, max=1.0) # type: ignore
    density: FloatProperty(name="Density", default=30.0, min=0.0, max=100.0) # type: ignore
    contour: FloatProperty(name="Contour", default=1.0, min=0.0, max=1.0) # type: ignore
    orientation: FloatProperty(name="Orientation", default=1.0, min=0.0, max=1.0) # type: ignore
    gradient: FloatProperty(name="Gradient", default=1.0, min=0.0, max=10.0) # type: ignore
    structure: FloatProperty(name="Structure", default=5.0, min=0.0, max=10.0) # type: ignore
    angle: FloatProperty(name="Angle", default=0.0, min=-180.0, max=180.0) # type: ignore
    angleDispersion: FloatProperty(name="Angle Dispersion", default=0.2, min=0.0, max=1.0) # type: ignore

    def create_command(self):
        return "fx_brushify {0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18}".format(
            (int(self.shape) + 2),
            self.ratio,
            self.numSize,
            self.maxSize,
            self.minSize,
            self.numOrientations,
            self.fuzzy,
            self.smoothness,
            self.lightType,
            self.lightStrength,
            self.opacity,
            self.density,
            self.contour,
            self.orientation,
            self.gradient,
            self.structure,
            self.angle,
            self.angleDispersion,
            0
        )

class FArt_Cartoon(GMICBaseNode):
    """Cartoon by David Tschumperlé"""
    # cartoon 3,200,20,0.25,1.5,8,0,50,50
    
    bl_idname = "GMIC_FArt_Cartoon"
    bl_label = "Cartoon"

    node_props = ["smooth", "sharp", "edgeThreshold", "edgeThickness", "colorStrength", "quantization"]

    smooth: FloatProperty(name="Smooth", default=3.0, min=0.0, max=10.0) # type: ignore
    sharp: FloatProperty(name="Sharp", default=200.0, min=0.0, max=400.0) # type: ignore
    edgeThreshold: FloatProperty(name="Edge Threshold", default=20.0, min=0.0, max=30.0) # type: ignore
    edgeThickness: FloatProperty(name="Edge Thickness", default=0.25, min=0.0, max=1.0) # type: ignore
    colorStrength: FloatProperty(name="Color Strength", default=1.5, min=0.0, max=3.0) # type: ignore
    quantization: FloatProperty(name="Quantization", default=8.0, min=0.0, max=256.0) # type: ignore

    def create_command(self):
        return "cartoon {0},{1},{2},{3},{4},{5},0,50,50".format(
            self.smooth,
            self.sharp,
            self.edgeThreshold,
            self.edgeThickness,
            self.colorStrength,
            self.quantization
        )

class FArt_ChalkItUp(GMICBaseNode):
    """Chalk It Up by Lylejk/samj/Ronounours"""
    # samj_chalkitup 5,2.5,1.5,50,1,5,5,0,0,7,0.8,1.9,7,0
    
    bl_idname = "GMIC_FArt_ChalkItUp"
    bl_label = "Chalk It Up"

    node_props = ["abstraction", "detail", "color", "smooth", "sharpShade", "action", "size", "invertColor", "shape", "xVariation", "yVariation"]

    abstraction: FloatProperty(name="Abstraction", default=5.0, min=0.0, max=10.0) # type: ignore
    detail: FloatProperty(name="Detail", default=2.5, min=0.0, max=10.0) # type: ignore
    color: FloatProperty(name="Color", default=1.5, min=0.0, max=5.0) # type: ignore
    smooth: FloatProperty(name="Smooth", default=50.0, min=0.0, max=200.0) # type: ignore
    sharpShade: BoolProperty(name="Sharp Shade", default=True) # type: ignore
    action: EnumProperty(
        name="Action",
        items=create_enum(["Erossion", "Dilation", "Opening", "Closing", "Original Erossion", "Original Dilation", "Original Opening", "Original Closing"]),
        default="5"
    ) # type: ignore
    size: FloatProperty(name="Size", default=5.0, min=0.0, max=32.0) # type: ignore
    invertColor: BoolProperty(name="Invert Color", default=False) # type: ignore
    shape: BoolProperty(name="Shape", default=False) # type: ignore
    xVariation: FloatProperty(name="X Variation", default=0.8, min=0.0, max=5.0) # type: ignore
    yVariation: FloatProperty(name="Y Variation", default=1.9, min=0.0, max=5.0) # type: ignore

    def create_command(self):
        return "samj_chalkitup {0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}".format(
            self.abstraction,
            self.detail,
            self.color,
            self.smooth,
            int(self.sharpShade),
            self.action,
            self.size,
            int(self.invertColor),
            int(self.shape),
            7,
            self.xVariation,
            self.yVariation,
            7,
            0
        )

class FArt_CircleAbstraction(GMICBaseNode):
    """Circle Abstraction by David Tschumperlé"""
    # fx_circle_abstraction 8,5,0.8,0,1,1,1,0,50,50
    
    bl_idname = "GMIC_FArt_CircleAbstraction"
    bl_label = "Circle Abstraction"

    node_props = ["numColor", "desnity", "opacity", "smooth", "filled", "fillHole", "normalize"]

    numColor: IntProperty(name="Number of Colors", default=8, min=0, max=16) # type: ignore
    desnity: FloatProperty(name="Desnity", default=5.0, min=0.0, max=100.0) # type: ignore
    opacity: FloatProperty(name="Opacity", default=0.8, min=0.0, max=1.0) # type: ignore
    smooth: FloatProperty(name="Smooth", default=0.0, min=0.0, max=4.0) # type: ignore
    filled: BoolProperty(name="Filled", default=True) # type: ignore
    fillHole: BoolProperty(name="Fill Hole", default=True) # type: ignore
    normalize: BoolProperty(name="Normalize", default=True) # type: ignore

    def create_command(self):
        return "fx_circle_abstraction {0},{1},{2},{3},{4},{5},{6},0,50,50".format(
            self.numColor,
            self.desnity,
            self.opacity,
            self.smooth,
            int(self.filled),
            int(self.fillHole),
            int(self.normalize),
        )

class FArt_Cubism(GMICBaseNode):
    """Cubism by David Tschumperlé"""
    # fx_cubism 2,50,10,90,0.7,0,0,50,50
    
    bl_idname = "GMIC_FArt_Cubism"
    bl_label = "Cubism"

    node_props = ["iteration", "density", "thickness", "angle", "opacity", "smooth"]

    iteration: IntProperty(name="Iteration", default=2, min=0, max=10) # type: ignore
    density: FloatProperty(name="Density", default=50.0, min=0.0, max=200.0) # type: ignore
    thickness: FloatProperty(name="Thickness", default=10.0, min=0.0, max=50.0) # type: ignore
    angle: FloatProperty(name="Angle", default=90.0, min=0.0, max=360.0) # type: ignore
    opacity: FloatProperty(name="Opacity", default=0.7, min=0.0, max=1.0) # type: ignore
    smooth: FloatProperty(name="Smooth", default=0.0, min=0.0, max=5.0) # type: ignore

    def create_command(self):
        return "fx_cubism {0},{1},{2},{3},{4},{5},0,50,50".format(
            self.iteration,
            self.density,
            self.thickness,
            self.angle,
            self.opacity,
            self.smooth
        )



classes = [
    FArt_AngoisseAnguish,
    FArt_Aurora,
    FArt_BarbouillagePaintDaub,
    FArt_BlackCrayonGraffiti,
    FArt_Blockism,
    FArt_Brushify,
    FArt_Cartoon,
    FArt_ChalkItUp,
    FArt_CircleAbstraction,
    FArt_Cubism
]