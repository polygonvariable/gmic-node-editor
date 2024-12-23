from bpy.props import ( BoolProperty, FloatProperty, EnumProperty, StringProperty, IntProperty )

from .gen import fcontours_gen
from ..base.node import GMICBaseNode, create_enum

class FContour_Curvature(GMICBaseNode):
    """Curvature by David Tschumperlé"""
    # fx_curvature 2,0,100,0,0,0,50,50

    bl_idname = "GMIC_FContour_Curvature"
    bl_label = "Curvature"

    node_props = ["smooth", "min_threshold", "max_threshold", "absolute", "negative"]

    smooth: FloatProperty(name="Smooth", default=2.0, min=0.0, max=10.0) # type: ignore
    min_threshold: FloatProperty(name="Min Threshold", default=0.0, min=0.0, max=100.0) # type: ignore
    max_threshold: FloatProperty(name="Max Threshold", default=100.0, min=0.0, max=100.0) # type: ignore
    absolute: BoolProperty(name="Absolute", default=False) # type: ignore
    negative: BoolProperty(name="Negative", default=False) # type: ignore

    def create_command(self):
        return "fx_curvature {0},{1},{2},{3},{4},0,50,50".format(
            self.smooth,
            self.min_threshold,
            self.max_threshold,
            int(self.absolute),
            int(self.negative)
        )

class FContour_DifferenceGaussian(GMICBaseNode):
    """Difference of Gaussian by David Tschumperlé"""
    # fx_dog 1.4,1.5,0,0,1,0,50,50

    bl_idname = "GMIC_FContour_DifferenceGaussian"
    bl_label = "Difference of Gaussian"

    node_props = ["var1", "var2", "threshold", "negative", "monochrome"]

    var1: FloatProperty(name="Variance 1", default=1.4, min=0.0, max=5.0) # type: ignore
    var2: FloatProperty(name="Variance 2", default=1.5, min=0.0, max=5.0) # type: ignore
    threshold: FloatProperty(name="Threshold", default=100.0, min=0.0, max=100.0) # type: ignore
    negative: BoolProperty(name="Negative", default=False) # type: ignore
    monochrome: BoolProperty(name="Monochrome", default=True) # type: ignore

    def create_command(self):
        return "fx_dog {0},{1},{2},{3},{4},0,50,50".format(
            self.var1,
            self.var2,
            self.threshold,
            int(self.negative),
            int(self.monochrome)
        )

class FContour_DistanceTransform(GMICBaseNode):
    """Distance Transform by David Tschumperlé"""
    # fx_distance 128,2,2,32,0,50,50

    bl_idname = "GMIC_FContour_DistanceTransform"
    bl_label = "Distance Transform"

    node_props = ["value", "metric", "normalization", "modulo"]

    value: IntProperty(name="Value", default=128, min=0, max=255) # type: ignore
    metric: EnumProperty(
        name="Metric",
        items=create_enum(["Chebyshev", "Manhattan", "Euclidean", "Sqaured Euclidean"]),
        default="2"
    ) # type: ignore
    normalization: EnumProperty(
        name="Normalization",
        items=create_enum(["Cut", "Normalize", "Modulo"]),
        default="2"
    ) # type: ignore
    modulo: IntProperty(name="Modulo", default=32, min=0, max=255) # type: ignore

    def create_command(self):
        return "fx_distance {0},{1},{2},{3},0,50,50".format(
            self.value,
            int(self.metric),
            int(self.normalization),
            self.modulo
        )

class FContour_Edge(GMICBaseNode):
    """Edge by afre"""
    # afre_edge 0,1,1,1,1

    bl_idname = "GMIC_FContour_Edge"
    bl_label = "Edge"

    node_props = ["method", "thinning", "recovery", "brightness", "detail"]

    method: EnumProperty(
        name="Method",
        items=create_enum(["Gradient", "Standard Deviation"]),
        default="0"
    ) # type: ignore
    thinning: IntProperty(name="Thinning", default=1, min=0, max=10) # type: ignore
    recovery: FloatProperty(name="Recovery", default=1.0, min=0.5, max=4.0) # type: ignore
    brightness: FloatProperty(name="Brightness", default=1.0, min=0.5, max=4.0) # type: ignore
    detail: FloatProperty(name="Detail", default=1.0, min=0.5, max=4.0) # type: ignore

    def create_command(self):
        return "afre_edge {0},{1},{2},{3},{4}".format(
            self.method,
            self.thinning,
            self.recovery,
            self.brightness,
            self.detail
        )

class GMIC_BlurNode(GMICBaseNode):
    """Blur Node by Author Name"""

    bl_idname = "BlurNode"
    bl_label = "Blur Node"

    node_props = ["ti", "name", "channel"]

    ti: FloatProperty(
        name="Time",
        default=0.0,
        min=0.0,
        max=1.0,
    ) # type: ignore
    name: StringProperty(
        name="Name",
        default="Hello",
    ) # type: ignore
    channel: EnumProperty(
        name="Channel",
        default="0",
        items=create_enum(["name", "hello"])
    ) # type: ignore

    def create_command(self):
        return "blur {self.amount}"


classes = [
    GMIC_BlurNode,
    FContour_Curvature,
    FContour_DifferenceGaussian,
    FContour_DistanceTransform,
    FContour_Edge
]