from nodeitems_utils import NodeItem
from bpy.props import ( BoolProperty, FloatProperty, EnumProperty )

from ..base.node import GMICBaseNode, create_enum

class FArt_AngoisseAnguish(GMICBaseNode):
    """Angoisse Anguish by David Tschumperlé"""

    bl_idname = "GMIC_FArt_AngoisseAnguish"
    bl_label = "Angoisse Anguish"

    node_props = ["iteration", "sigma1", "sigma2", "segment_threshold", "smooth_amplitude", "noise_amplitude", "noise_type", "opacity", "sharp_amplitude"]

    iteration: FloatProperty(name="Iteration", default=1.0, min=0.0, max=3.0) # type: ignore
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
    """Aurora by David Tschumperlé"""
    
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

classes = [
    FArt_AngoisseAnguish,
    FArt_Aurora
]