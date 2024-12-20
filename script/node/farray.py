from ..base.node import GMICBaseNode, create_enum
import tempfile
from nodeitems_utils import NodeItem
from bpy.props import ( StringProperty, BoolProperty, FloatProperty, EnumProperty )

class FAT_ArrayFaded(GMICBaseNode):
    """Filter Array Faded Node"""
    """by David Tschumperlé"""
    # fx_array_fade 2,2,0,0,80,90,0,0

    bl_idname = "GMIC_FAT_ArrayFaded"
    bl_label = "Array Faded"
    bl_icon = "NODE"
    
    node_props = ["xTile", "yTile", "xOffset", "yOffset", "fadeStart", "fadeEnd", "mirror"]
    
    xTile: FloatProperty(name="X Tile",default=2.0, min=0.0, max=10.0) # type: ignore
    yTile: FloatProperty(name="Y Tile", default=2.0, min=0.0, max=10.0) # type: ignore
    xOffset: FloatProperty(name= "X Offset",default=0.0, min=0.0, max=100.0) # type: ignore
    yOffset: FloatProperty(name= "Y Offset",default=0.0, min=0.0, max=100.0) # type: ignore
    fadeStart: FloatProperty(name= "Fade Start",default=80.0, min=0.0, max=100.0) # type: ignore
    fadeEnd: FloatProperty(name= "Fade End",default=90.0, min=0.0, max=100.0) # type: ignore
    mirror: EnumProperty(
        name="Mirror",
        items=create_enum(["None", "X", "Y", "XY"]),
        default="0"
    ) # type: ignore

    def create_command(self):
        return "fx_array_fade {0},{1},{2},{3},{4},{5},{6},{7}".format(
            self.xTile,
            self.yTile,
            self.xOffset,
            self.yOffset,
            self.fadeStart,
            self.fadeEnd,
            int(self.mirror),
            0
        )

class FAT_ArrayMirrored(GMICBaseNode):
    """Filter Array Mirrored Node"""
    """by David Tschumperlé"""
    # fx_array_mirror 1,0,0,2,0,0,0

    bl_idname = "GMIC_FAT_ArrayMirrored"
    bl_label = "Array Mirrored"
    bl_icon = "NODE"
    
    node_props = ["iteration", "xOffset", "yOffset", "arrayMode", "initilization", "crop"]

    iteration: FloatProperty(name="Iteration",default=1.0, min=0.0, max=10.0) # type: ignore
    xOffset: FloatProperty(name="X Offset", default=0.0, min=0.0, max=100.0) # type: ignore
    yOffset: FloatProperty(name= "Y Offset",default=0.0, min=0.0, max=100.0) # type: ignore
    arrayMode: EnumProperty(
        name="Array Mode",
        items=create_enum(["X", "Y", "XY", "2XY"]),
        default="2"
    ) # type: ignore
    initilization: EnumProperty(
        name="Initilization",
        items=create_enum(["Original", "Mirror X", "Mirror Y", "Rotate 90", "Rotate 180", "Rotate 270"]),
        default="0"
    ) # type: ignore
    crop: FloatProperty(default=0.0, min=0.0, max=100.0) # type: ignore

    def create_command(self):
        return "fx_array_mirror {0},{1},{2},{3},{4},{5},{6}".format(
            self.iteration,
            self.xOffset,
            self.yOffset,
            int(self.arrayMode),
            int(self.initilization),
            0,
            self.crop
        )

class FAT_ArrayRandomColor(GMICBaseNode):
    """Filter Array Random Color Node"""
    """by David Tschumperlé"""
    # fx_array_color 5,5,0.5

    bl_idname = "GMIC_FAT_ArrayRandomColor"
    bl_label = "Array Random Color"
    bl_icon = "NODE"
    
    node_props = ["xTile", "yTile", "opacity"]
    
    xTile: FloatProperty(name="X Tile",default=2.0, min=0.0, max=10.0) # type: ignore
    yTile: FloatProperty(name="Y Tile", default=2.0, min=0.0, max=10.0) # type: ignore
    opacity: FloatProperty(name="Opacity", default=0.5, min=0.0, max=1.0) # type: ignore

    def create_command(self):
        return "fx_array_color {0},{1},{2}".format(
            self.xTile,
            self.yTile,
            self.opacity
        )

class FAT_ArrayRandom(GMICBaseNode):
    """Filter Array Random Node"""
    """by David Tschumperlé"""
    # array_random 5,5,7,7

    bl_idname = "GMIC_FAT_ArrayRandom"
    bl_label = "Array Random"
    bl_icon = "NODE"
    
    node_props = ["srcXTile", "srcYTile", "desXTile", "desYTile"]
    
    srcXTile: FloatProperty(name="Source X Tile",default=5.0, min=0.0, max=20.0) # type: ignore
    srcYTile: FloatProperty(name="Source Y Tile", default=5.0, min=0.0, max=20.0) # type: ignore
    desXTile: FloatProperty(name="Destination X Tile",default=7.0, min=0.0, max=20.0) # type: ignore
    desYTile: FloatProperty(name="Destination Y Tile", default=7.0, min=0.0, max=20.0) # type: ignore

    def create_command(self):
        return "array_random {0},{1},{2},{3}".format(
            self.srcXTile,
            self.srcYTile,
            self.desXTile,
            self.desYTile
        )

class FAT_ASCIIArt(GMICBaseNode):
    """Filter ASCII Art Node"""
    """by David Tschumperlé"""
    # fx_asciiart 5," +-",16,15,16,2,0,0.2,0,0,"C:/Users/Public","gmic_asciiart.txt"

    bl_idname = "GMIC_FAT_ASCIIArt"
    bl_label = "ASCII Art"
    bl_icon = "NODE"

    node_props = ["charset", "dictionary", "scale", "smooth", "synthesis", "background", "gamma", "smoothness"]
    
    charset: EnumProperty(
        name="Charset",
        items=create_enum(["Custom", "Binary", "Number", "Lowercase", "Uppercase", "ASCII", "Card Suits", "Symbol"]),
        default="5"
    ) # type: ignore
    dictionary: StringProperty(name="Dictionary", default=" +-") # type: ignore
    scale: FloatProperty(name="Analysis Scale", default=16.0, min=0.0, max=103.0) # type: ignore
    smooth: FloatProperty(name="Analysis Smooth", default=15.0, min=0.0, max=100.0) # type: ignore
    synthesis: FloatProperty(name="Synthesis", default=16.0, min=0.0, max=103.0) # type: ignore
    background: EnumProperty(
        name="Background",
        items=create_enum(["White on Black", "Black on White", "Color on Black", "Color on Transparent"]),
        default="2"
    ) # type: ignore
    gamma : FloatProperty(name="Gamma", default=0.0, min=-3.0, max=3.0) # type: ignore
    smoothness: FloatProperty(name="Smoothness", default=0.2, min=0.0, max=5.0) # type: ignore

    def create_command(self):
        return "fx_asciiart {0},\\\"{1}\\\",{2},{3},{4},{5},{6},{7},0,0,\\\"{8}\\\",\\\"{9}\\\"".format(
            int(self.charset),
            self.dictionary,
            self.scale,
            self.smooth,
            self.synthesis,
            int(self.background),
            self.gamma,
            self.smoothness,
            tempfile.gettempdir(),
            "gmic_asciiart.txt"
        )

class FAT_Dices(GMICBaseNode):
    """Filter Dices Node"""
    """by David Tschumperlé"""
    # fx_dices 2,24,3

    bl_idname = "GMIC_FAT_Dices"
    bl_label = "Dices"
    bl_icon = "NODE"

    node_props = [ "resolution", "size", "color" ]
    
    resolution: FloatProperty(name="Resolution",default=2.0, min=0.0, max=10.0) # type: ignore
    size: FloatProperty(name="Size", default=24.0, min=0.0, max=64.0) # type: ignore
    color: EnumProperty(
        name="Color Model",
        items=create_enum(["White", "Black", "Color Number", "Color Sides"]),
        default="3"
    ) # type: ignore
    
    def create_command(self):
        return "fx_dices {0},{1},{2}".format(
            self.resolution,
            self.size,
            int(self.color)
        )

class FAT_GridCartesian(GMICBaseNode):
    """Filter Grid Cartesian Node"""
    """by David Tschumperlé"""
    # fx_imagegrid 10,10
    
    bl_idname = "GMIC_FAT_GridCartesian"
    bl_label = "Grid Cartesian"
    bl_icon = "NODE"

    node_props = ["xSize", "ySize"]
    
    xSize = FloatProperty(name="X Size", default=10.0, min=0.0, max=512.0) # type: ignore
    ySize = FloatProperty(name="Y Size", default=10.0, min=0.0, max=512.0) # type: ignore
    
    def create_command(self):
        return "fx_imagegrid {0},{1}".format(
            self.xSize,
            self.ySize
        )

class FAT_GridHexagon(GMICBaseNode):
    """Filter Grid Hexagon Node"""
    """by David Tschumperlé"""
    # fx_imagegrid_hexagonal 32,0.1,1
    
    bl_idname = "GMIC_FAT_GridHexagon"
    bl_label = "Grid Hexagon"
    bl_icon = "NODE"
    
    node_props = ["resolution", "outline"]

    resolution: FloatProperty(name="Resolution", default=32.0, min=0.0, max=128.0) # type: ignore
    outline: FloatProperty(name="Outline", default=0.1, min=0.0, max=0.5) # type: ignore
    
    def create_command(self):
        return "fx_imagegrid_hexagonal {0},{1},{2}".format(
            self.resolution,
            self.outline,
            1
        )


classes = [
    FAT_ArrayFaded,
    FAT_ArrayMirrored,
    FAT_ArrayRandomColor,
    FAT_ArrayRandom,
    FAT_ASCIIArt,
    FAT_Dices,
    FAT_GridCartesian,
    FAT_GridHexagon
]