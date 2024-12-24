from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FFrame_droste(GMICBaseNode):
    """Droste by Author: David Tschumperlé. Latest Update: 2012/11/06."""
    # fx_droste

    bl_idname = "FFrame_droste"
    bl_label = "Droste"

    node_props = ["var_prop1_x", "var_prop1_y", "var_prop4_x", "var_prop4_y", "var_prop7_x", "var_prop7_y", "var_prop10_x", "var_prop10_y", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop18", "var_prop19", "var_prop20"]

    var_prop1_x: FloatProperty(
        name="Point #0 X",
        default=20.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_y: FloatProperty(
        name="Point #0 Y",
        default=20.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4_x: FloatProperty(
        name="Point #1 X",
        default=80.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4_y: FloatProperty(
        name="Point #1 Y",
        default=20.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop7_x: FloatProperty(
        name="Point #2 X",
        default=80.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop7_y: FloatProperty(
        name="Point #2 Y",
        default=80.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop10_x: FloatProperty(
        name="Point #3 X",
        default=20.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop10_y: FloatProperty(
        name="Point #3 Y",
        default=80.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop12: IntProperty(
        name="Iterations",
        default=1,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="X-Shift",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Y-Shift",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Zoom",
        default=1.0,
        min=0.1, 
        max=5.0, 
    ) # type: ignore
    var_prop17: EnumProperty(
        name="Mirror",
        default="0",
        items=create_enum(["None", "X-Axis", "Y-Axis", "XY-Axes"]),
    ) # type: ignore
    var_prop18: EnumProperty(
        name="Boundary",
        default="1",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop19: EnumProperty(
        name="Drawing Mode",
        default="0",
        items=create_enum(["Replace", "Replace (Sharpest)", "Behind", "Below"]),
    ) # type: ignore
    var_prop20: BoolProperty(
        name="View Outlines Only",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_droste {self.var_prop1_x},{self.var_prop1_y},{self.var_prop4_x},{self.var_prop4_y},{self.var_prop7_x},{self.var_prop7_y},{self.var_prop10_x},{self.var_prop10_y},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18},{self.var_prop19},{int(self.var_prop20)}"

################################################################################
################################################################################

class GMIC_FFrame_frameblur(GMICBaseNode):
    """Frame [Blur] by Author: David Tschumperlé. Latest Update: 2014/19/01."""
    # fx_frame_blur

    bl_idname = "FFrame_frameblur"
    bl_label = "Frame [Blur]"

    node_props = ["var_prop0", "var_prop1", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop18"]

    var_prop0: FloatProperty(
        name="Horizontal Size (%)",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Vertical Size (%)",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Crop",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Blur",
        default=5.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Roundness",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop6: BoolProperty(
        name="Apply Color Balance",
        default=0,
    ) # type: ignore
    var_prop7: FloatVectorProperty(
        name="Balance Color",
        default=(0.5019607843137255,0.5019607843137255,0.5019607843137255),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Normalization",
        default="0",
        items=create_enum(["None", "Stretch", "Equalize"]),
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Outline Size",
        default=5.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop11: FloatVectorProperty(
        name="Outline Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop12: FloatProperty(
        name="X-Shadow",
        default=2.0,
        min=-10.0, 
        max=10.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Y-Shadow",
        default=2.0,
        min=-10.0, 
        max=10.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Shadow Smoothness",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop15: FloatProperty(
        name="Shadow Contrast",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="X-Centering",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Y-Centering",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Angle",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_frame_blur {self.var_prop0},{self.var_prop1},{self.var_prop3},{self.var_prop4},{self.var_prop5},{int(self.var_prop6)},{self.var_prop7[0]*255},{self.var_prop7[1]*255},{self.var_prop7[2]*255},255,{self.var_prop8},{self.var_prop10},{self.var_prop11[0]*255},{self.var_prop11[1]*255},{self.var_prop11[2]*255},255,{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop18}"

################################################################################
################################################################################

class GMIC_FFrame_framefuzzy(GMICBaseNode):
    """Frame [Fuzzy] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_frame_fuzzy

    bl_idname = "FFrame_framefuzzy"
    bl_label = "Frame [Fuzzy]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: FloatProperty(
        name="Horizontal Size (%)",
        default=5.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Vertical Size (%)",
        default=5.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Fuzzyness",
        default=10.0,
        min=0.0, 
        max=40.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Smoothness",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop4: FloatVectorProperty(
        name="Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore

    def create_command(self):
        return f"fx_frame_fuzzy {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4[0]*255},{self.var_prop4[1]*255},{self.var_prop4[2]*255},255"

################################################################################
################################################################################

class GMIC_FFrame_framemirror(GMICBaseNode):
    """Frame [Mirror] by Author: David Tschumperlé. Latest Update: 2018/08/20."""
    # fx_frame_mirror

    bl_idname = "FFrame_framemirror"
    bl_label = "Frame [Mirror]"

    node_props = ["var_prop1", "var_prop2", "var_prop5", "var_prop6", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop14"]

    var_prop1: FloatProperty(
        name="Horizontal (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Vertical (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Horizontal (%)",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Vertical (%)",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Left",
        default=0.0,
        min=-5.0, 
        max=5.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Right",
        default=0.0,
        min=-5.0, 
        max=5.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Up",
        default=0.0,
        min=-5.0, 
        max=5.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Bottom",
        default=0.0,
        min=-5.0, 
        max=5.0, 
    ) # type: ignore
    var_prop14: FloatProperty(
        name="Preview Opacity (%)",
        default=0.75,
        min=0.0, 
        max=1.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_frame_mirror {self.var_prop1},{self.var_prop2},{self.var_prop5},{self.var_prop6},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop14}"

################################################################################
################################################################################

class GMIC_FFrame_framepainting(GMICBaseNode):
    """Frame [Painting] by Author: David Tschumperlé. Latest Update: 2012/07/06."""
    # fx_frame_painting

    bl_idname = "FFrame_framepainting"
    bl_label = "Frame [Painting]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop5", "var_prop6", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop13", "var_prop14"]

    var_prop0: FloatProperty(
        name="Size (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Contrast",
        default=0.4,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=6.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop3: FloatVectorProperty(
        name="Color",
        default=(0.8823529411764706,0.7843137254901961,0.47058823529411764),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Vignette Size",
        default=2.0,
        min=0.0, 
        max=50.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Vignette Contrast",
        default=400.0,
        min=0.0, 
        max=1000.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Defects Contrast",
        default=50.0,
        min=0.0, 
        max=512.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Defects Density",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Defects Size",
        default=1.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Defects Smoothness",
        default=0.5,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop13: IntProperty(
        name="Serial Number",
        default=123456,
        min=0, 
        max=1000000, 
    ) # type: ignore
    var_prop14: BoolProperty(
        name="Frame as a New Layer",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_frame_painting {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3[0]*255},{self.var_prop3[1]*255},{self.var_prop3[2]*255},255,{self.var_prop5},{self.var_prop6},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop13},{int(self.var_prop14)}"

################################################################################
################################################################################

class GMIC_FFrame_frameregular(GMICBaseNode):
    """Frame [Regular] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_frame

    bl_idname = "FFrame_frameregular"
    bl_label = "Frame [Regular]"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11"]

    var_prop1: IntProperty(
        name="X-Start (%)",
        default=0,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="X-End (%)",
        default=100,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Y-Start (%)",
        default=0,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Y-End (%)",
        default=100,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Width (%)",
        default=10,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Height (%)",
        default=10,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop9: FloatVectorProperty(
        name="Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop10: IntProperty(
        name="Outline Size",
        default=1,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop11: FloatVectorProperty(
        name="Outline Color",
        default=(1.0,1.0,1.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore

    def create_command(self):
        return f"fx_frame {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop7},{self.var_prop8},{self.var_prop9[0]*255},{self.var_prop9[1]*255},{self.var_prop9[2]*255},255,{self.var_prop10},{self.var_prop11[0]*255},{self.var_prop11[1]*255},{self.var_prop11[2]*255},255"

################################################################################
################################################################################

class GMIC_FFrame_framerelief(GMICBaseNode):
    """Frame [Relief] by Author: Claude Lion. Latest Update: 2022/08/26."""
    # cl_reliefFrame

    bl_idname = "FFrame_framerelief"
    bl_label = "Frame [Relief]"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop15", "var_prop16", "var_prop19", "var_prop20", "var_prop21"]

    var_prop1: EnumProperty(
        name="Type",
        default="2",
        items=create_enum(["Outset", "Inset", "Groove", "Ridge"]),
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Size",
        default=10.0,
        min=6.0, 
        max=40.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Relief Width",
        default=1.5,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Relief Amount",
        default=75.0,
        min=0.0, 
        max=127.0, 
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Kaleidoscope Effect",
        default=1,
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Frame Blur",
        default=60.0,
        min=5.0, 
        max=80.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Frame Hue Change",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Frame Saturation Change",
        default=0.0,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Frame Luminosity Change",
        default=0.0,
        min=-0.5, 
        max=0.5, 
    ) # type: ignore
    var_prop15: BoolProperty(
        name="Set Uniform Frame Color",
        default=0,
    ) # type: ignore
    var_prop16: FloatVectorProperty(
        name="Frame Color",
        default=(0.7529411764705882,0.7529411764705882,0.7529411764705882),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop19: EnumProperty(
        name="Graininess Type",
        default="0",
        items=create_enum(["Gaussian", "Uniform", "Poisson"]),
    ) # type: ignore
    var_prop20: FloatProperty(
        name="Graininess Amount",
        default=0.0,
        min=0.0, 
        max=80.0, 
    ) # type: ignore
    var_prop21: EnumProperty(
        name="Graininess on",
        default="0",
        items=create_enum(["Frame", "Picture", "Both"]),
    ) # type: ignore

    def create_command(self):
        return f"cl_reliefFrame {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{int(self.var_prop7)},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{int(self.var_prop15)},{self.var_prop16[0]*255},{self.var_prop16[1]*255},{self.var_prop16[2]*255},255,{self.var_prop19},{self.var_prop20},{self.var_prop21}"

################################################################################
################################################################################

class GMIC_FFrame_frameround(GMICBaseNode):
    """Frame [Round] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_frame_round

    bl_idname = "FFrame_frameround"
    bl_label = "Frame [Round]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: FloatProperty(
        name="X-Size (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Y-Size (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Radius (%)",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Smoothness",
        default=0.1,
        min=0.0, 
        max=15.0, 
    ) # type: ignore
    var_prop4: FloatVectorProperty(
        name="Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore

    def create_command(self):
        return f"fx_frame_round {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4[0]*255},{self.var_prop4[1]*255},{self.var_prop4[2]*255},255"

################################################################################
################################################################################

class GMIC_FFrame_framesmooth(GMICBaseNode):
    """Frame [Smooth] by Author: David Tschumperlé. Latest Update: 2016/25/04."""
    # fx_frame_smooth

    bl_idname = "FFrame_framesmooth"
    bl_label = "Frame [Smooth]"

    node_props = ["var_prop0", "var_prop1", "var_prop2"]

    var_prop0: IntProperty(
        name="Width (%)",
        default=5,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Height (%)",
        default=5,
        min=0, 
        max=100, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Roundness",
        default=0.25,
        min=0.0, 
        max=1.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_frame_smooth {self.var_prop0},{self.var_prop1},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FFrame_oldphotograph(GMICBaseNode):
    """Old Photograph by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_old_photo

    bl_idname = "FFrame_oldphotograph"
    bl_label = "Old Photograph"

    node_props = ["var_prop0", "var_prop1", "var_prop2"]

    var_prop0: FloatProperty(
        name="Vignette Strength",
        default=200.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Vignette Min Radius",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Vignette Max Radius",
        default=85.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_old_photo {self.var_prop0},{self.var_prop1},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FFrame_polaroid(GMICBaseNode):
    """Polaroid by Author: David Tschumperlé. Latest Update: 2016/20/06."""
    # fx_polaroid

    bl_idname = "FFrame_polaroid"
    bl_label = "Polaroid"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10"]

    var_prop0: IntProperty(
        name="Frame Size",
        default=10,
        min=0, 
        max=400, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Bottom Size",
        default=20,
        min=0, 
        max=400, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="X-Shadow",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Y-Shadow",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Smoothness",
        default=3.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="X-Curvature",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Y-Curvature",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Angle",
        default=20.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Vignette Strength",
        default=50.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Vignette Min Radius",
        default=70.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Vignette Max Radius",
        default=95.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_polaroid {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10}"

################################################################################
################################################################################

class GMIC_FFrame_tunnel(GMICBaseNode):
    """Tunnel by Author: David Tschumperlé. Latest Update: 2012/22/11."""
    # fx_tunnel

    bl_idname = "FFrame_tunnel"
    bl_label = "Tunnel"

    node_props = ["var_prop0", "var_prop1", "var_prop2_x", "var_prop2_y", "var_prop3", "var_prop4"]

    var_prop0: IntProperty(
        name="Depth",
        default=4,
        min=1, 
        max=100, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Factor",
        default=80.0,
        min=1.0, 
        max=99.0, 
    ) # type: ignore
    var_prop2_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Opacity",
        default=0.2,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Angle",
        default=0.0,
        min=-90.0, 
        max=90.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_tunnel {self.var_prop0},{self.var_prop1},{self.var_prop2_x},{self.var_prop2_y},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FFrame_vignette(GMICBaseNode):
    """Vignette by Author: David Tschumperlé. Latest Update: 2012/24/10."""
    # fx_vignette

    bl_idname = "FFrame_vignette"
    bl_label = "Vignette"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3"]

    var_prop0: FloatProperty(
        name="Strength",
        default=70.0,
        min=0.0, 
        max=255.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Min Radius",
        default=70.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Max Radius",
        default=95.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatVectorProperty(
        name="Color",
        default=(0.0,0.0,0.0),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore

    def create_command(self):
        return f"fx_vignette {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3[0]*255},{self.var_prop3[1]*255},{self.var_prop3[2]*255},255"

################################################################################
################################################################################

node_classes = [
    GMIC_FFrame_droste, GMIC_FFrame_frameblur, GMIC_FFrame_framefuzzy, GMIC_FFrame_framemirror, GMIC_FFrame_framepainting, GMIC_FFrame_frameregular, GMIC_FFrame_framerelief, GMIC_FFrame_frameround, GMIC_FFrame_framesmooth, GMIC_FFrame_oldphotograph, GMIC_FFrame_polaroid, GMIC_FFrame_tunnel, GMIC_FFrame_vignette
]

################################################################################