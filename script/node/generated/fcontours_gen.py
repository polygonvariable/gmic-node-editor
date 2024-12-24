from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FContour_convolve(GMICBaseNode):
    """Convolve by Author: David Tschumperlé. Latest Update: 2013/06/06."""
    # fx_convolve

    bl_idname = "FContour_convolve"
    bl_label = "Convolve"

    node_props = ["var_prop0", "var_prop1", "var_prop4", "var_prop7", "var_prop8", "var_prop10", "var_prop12"]

    var_prop0: EnumProperty(
        name="Kernel",
        default="0",
        items=create_enum(["Custom", "Average 3x3", "Average 5x5", "Average 7x7", "Average 9x9", "Prewitt-X", "Prewitt-Y", "Sobel-X", "Sobel-Y", "Rotinv-X", "Rotinv-Y", "Laplacian", "Robert Cross 1", "Robert Cross 2", "Impulses 5x5", "Impulses 7x7", "Impulses 9x9"]),
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Boundary",
        default="1",
        items=create_enum(["Dirichlet", "Neumann"]),
    ) # type: ignore
    var_prop4: StringProperty(
        name="Custom Kernel",
        default="0,1,0;1,-4,1;0,1,0",
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Value Range",
        default="1",
        items=create_enum(["Cut", "Normalize"]),
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Kernel Multiplier",
        default=1.0,
        min=0.0, 
        max=50.0, 
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
        return f"fx_convolve {self.var_prop0},{self.var_prop1},\\\"{self.var_prop4}\\\",{self.var_prop7},{self.var_prop8},{self.var_prop10},{self.var_prop12},50,50"

################################################################################
################################################################################

class GMIC_FContour_edges(GMICBaseNode):
    """Edges by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_edges

    bl_idname = "FContour_edges"
    bl_label = "Edges"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Threshold",
        default=15.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Negative Colors",
        default=0,
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_edges {self.var_prop0},{self.var_prop1},{int(self.var_prop2)},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FContour_edgesoffsets(GMICBaseNode):
    """Edges Offsets by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_edge_offsets

    bl_idname = "FContour_edgesoffsets"
    bl_label = "Edges Offsets"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Threshold",
        default=15.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Scale",
        default=4,
        min=0, 
        max=32, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Thickness",
        default=1,
        min=0, 
        max=16, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Negative Colors",
        default=0,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_edge_offsets {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FContour_gradientnorm(GMICBaseNode):
    """Gradient Norm by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_gradient_norm

    bl_idname = "FContour_gradientnorm"
    bl_label = "Gradient Norm"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Linearity",
        default=0.5,
        min=0.0, 
        max=1.5, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Min Threshold",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Max Threshold",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Negative Colors",
        default=0,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_gradient_norm {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{int(self.var_prop4)},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FContour_gradientrgb(GMICBaseNode):
    """Gradient RGB by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_gradient2rgb

    bl_idname = "FContour_gradientrgb"
    bl_label = "Gradient RGB"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Min Threshold",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Max Threshold",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Orientation Only",
        default=0,
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Negative Colors",
        default=0,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_gradient2rgb {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{int(self.var_prop4)},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FContour_isophotes(GMICBaseNode):
    """Isophotes by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_isophotes

    bl_idname = "FContour_isophotes"
    bl_label = "Isophotes"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: IntProperty(
        name="Levels",
        default=8,
        min=1, 
        max=256, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Filling",
        default="1",
        items=create_enum(["Transparent", "Colors"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_isophotes {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FContour_laplacian(GMICBaseNode):
    """Laplacian by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_laplacian

    bl_idname = "FContour_laplacian"
    bl_label = "Laplacian"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Min Threshold",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Max Threshold",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Absolute Value",
        default=0,
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Negative Colors",
        default=0,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_laplacian {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{int(self.var_prop4)},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FContour_localorientation(GMICBaseNode):
    """Local Orientation by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_local_orientation

    bl_idname = "FContour_localorientation"
    bl_label = "Local Orientation"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Min Threshold",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Max Threshold",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Negative Colors",
        default=0,
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
        return f"fx_local_orientation {self.var_prop0},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FContour_morphologicalfilter(GMICBaseNode):
    """Morphological Filter by Author: David Tschumperlé. Latest Update: 2016/22/06."""
    # fx_morphological

    bl_idname = "FContour_morphologicalfilter"
    bl_label = "Morphological Filter"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop11"]

    var_prop0: EnumProperty(
        name="Action",
        default="0",
        items=create_enum(["Erosion", "Dilation", "Opening", "Closing", "Original - Erosion", "Dilation - Original", "Original - Opening", "Closing - Original", "Original - (Opening + Closing)/2", "Closing - Opening"]),
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Kernel",
        default="0",
        items=create_enum(["Square", "Octagonal", "Circular", "Custom"]),
    ) # type: ignore
    var_prop2: IntProperty(
        name="Size",
        default=5,
        min=2, 
        max=60, 
    ) # type: ignore
    var_prop4: StringProperty(
        name="Custom Kernel",
        default="1,0,1; 0,1,0; 1,0,1",
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Negative",
        default=0,
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Process Transparency",
        default=0,
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Stretch"]),
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_morphological {self.var_prop0},{self.var_prop1},{self.var_prop2},\\\"{self.var_prop4}\\\",{int(self.var_prop5)},{int(self.var_prop6)},{self.var_prop8},{self.var_prop9},{self.var_prop11},50,50"

################################################################################
################################################################################

class GMIC_FContour_segmentation(GMICBaseNode):
    """Segmentation by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_segment_watershed

    bl_idname = "FContour_segmentation"
    bl_label = "Segmentation"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="Edge Threshold",
        default=2.0,
        min=0.0, 
        max=15.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=5.0, 
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
        return f"fx_segment_watershed {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FContour_skeleton(GMICBaseNode):
    """Skeleton by Author: David Tschumperlé. Latest Update: 2011/07/04."""
    # fx_skeleton

    bl_idname = "FContour_skeleton"
    bl_label = "Skeleton"

    node_props = ["var_prop0", "var_prop1", "var_prop3"]

    var_prop0: EnumProperty(
        name="Method",
        default="0",
        items=create_enum(["Distance (Fast)", "Thinning (Slow)"]),
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_skeleton {self.var_prop0},{self.var_prop1},{self.var_prop3},50,50"

################################################################################
################################################################################

class GMIC_FContour_superpixels(GMICBaseNode):
    """Super-Pixels by Author: David Tschumperlé. Latest Update: 2017/11/16."""
    # fx_superpixels

    bl_idname = "FContour_superpixels"
    bl_label = "Super-Pixels"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: IntProperty(
        name="Size",
        default=16,
        min=4, 
        max=64, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Regularity",
        default=10.0,
        min=0.0, 
        max=128.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Iterations",
        default=5,
        min=1, 
        max=16, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Colors",
        default="1",
        items=create_enum(["Random", "Average"]),
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Border Opacity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Border Thickness (px)",
        default=1,
        min=1, 
        max=16, 
    ) # type: ignore
    var_prop6: FloatVectorProperty(
        name="Border Color",
        default=(0.0,0.0,0.0),
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
        return f"fx_superpixels {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6[0]*255},{self.var_prop6[1]*255},{self.var_prop6[2]*255},255,{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FContour_thinedges(GMICBaseNode):
    """Thin Edges by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_thin_edges

    bl_idname = "FContour_thinedges"
    bl_label = "Thin Edges"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4"]

    var_prop0: FloatProperty(
        name="Smoothness",
        default=0.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Threshold",
        default=15.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Negative Colors",
        default=0,
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_thin_edges {self.var_prop0},{self.var_prop1},{int(self.var_prop2)},{self.var_prop4},50,50"

################################################################################
################################################################################

node_classes = [
    GMIC_FContour_convolve, GMIC_FContour_edges, GMIC_FContour_edgesoffsets, GMIC_FContour_gradientnorm, GMIC_FContour_gradientrgb, GMIC_FContour_isophotes, GMIC_FContour_laplacian, GMIC_FContour_localorientation, GMIC_FContour_morphologicalfilter, GMIC_FContour_segmentation,
    GMIC_FContour_skeleton, GMIC_FContour_superpixels, GMIC_FContour_thinedges
]

################################################################################