from bpy.props import ( IntProperty, FloatProperty, EnumProperty, BoolProperty, FloatVectorProperty, StringProperty )

from ...base.node import GMICBaseNode
from ...base.library import create_enum


################################################################################

class GMIC_FDeform_breaks(GMICBaseNode):
    """Breaks by Author: David Tschumperlé. Latest Update: 2021/09/09."""
    # fx_breaks

    bl_idname = "FDeform_breaks"
    bl_label = "Breaks"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: EnumProperty(
        name="Type",
        default="0",
        items=create_enum(["Flat", "Relief"]),
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Amplitude",
        default=30.0,
        min=0.0, 
        max=300.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Frequency (%)",
        default=30.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_breaks {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FDeform_cartesiantransform(GMICBaseNode):
    """Cartesian Transform by Author: David Tschumperlé. Latest Update: 2023/10/26."""
    # fx_custom_deformation

    bl_idname = "FDeform_cartesiantransform"
    bl_label = "Cartesian Transform"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop7", "var_prop8", "var_prop9", "var_prop10"]

    var_prop0: StringProperty(
        name="X-Warping",
        default="(w*a%)*cos(b*y/h)",
    ) # type: ignore
    var_prop1: StringProperty(
        name="Y-Warping",
        default="(h*c%)*cos(d*x/w)",
    ) # type: ignore
    var_prop2: BoolProperty(
        name="Relative Warping",
        default=1,
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Interpolation",
        default="1",
        items=create_enum(["Nearest Neighbor", "Linear"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop7: FloatProperty(
        name="a",
        default=10.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="b",
        default=10.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="c",
        default=10.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="d",
        default=10.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_custom_deformation \\\"{self.var_prop0}\\\",\\\"{self.var_prop1}\\\",{int(self.var_prop2)},{self.var_prop3},{self.var_prop4},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10}"

################################################################################
################################################################################

class GMIC_FDeform_continuousdroste(GMICBaseNode):
    """Continuous Droste by Author : Souphead. Latest update : 2016/19/01."""
    # souphead_droste10

    bl_idname = "FDeform_continuousdroste"
    bl_label = "Continuous Droste"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop19", "var_prop20", "var_prop21", "var_prop23", "var_prop24", "var_prop25", "var_prop26", "var_prop27", "var_prop28", "var_prop30", "var_prop31", "var_prop33", "var_prop34", "var_prop35"]

    var_prop0: FloatProperty(
        name="Inner Radius",
        default=40.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Outer Radius",
        default=100.0,
        min=1.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Periodicity",
        default=1.0,
        min=-6.0, 
        max=6.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Strands",
        default=1,
        min=-6, 
        max=6, 
    ) # type: ignore
    var_prop4: IntProperty(
        name="Zoom",
        default=1,
        min=1, 
        max=100, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Rotate",
        default=0,
        min=-360, 
        max=360, 
    ) # type: ignore
    var_prop6: IntProperty(
        name="X-Shift",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop7: IntProperty(
        name="Y-Shift",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop8: IntProperty(
        name="Center X-Shift",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop9: IntProperty(
        name="Center Y-Shift",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop10: IntProperty(
        name="Starting Level",
        default=1,
        min=1, 
        max=20, 
    ) # type: ignore
    var_prop11: IntProperty(
        name="Number of Levels",
        default=10,
        min=1, 
        max=20, 
    ) # type: ignore
    var_prop12: IntProperty(
        name="Level Frequency",
        default=1,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop14: BoolProperty(
        name="Show Both Poles",
        default=0,
    ) # type: ignore
    var_prop15: IntProperty(
        name="Pole Rotation",
        default=90,
        min=-180, 
        max=180, 
    ) # type: ignore
    var_prop16: IntProperty(
        name="Pole Long",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop17: IntProperty(
        name="Pole Lat",
        default=0,
        min=-100, 
        max=100, 
    ) # type: ignore
    var_prop19: BoolProperty(
        name="Tile Poles",
        default=0,
    ) # type: ignore
    var_prop20: BoolProperty(
        name="Hyper Droste",
        default=0,
    ) # type: ignore
    var_prop21: IntProperty(
        name="Fractal Points",
        default=1,
        min=1, 
        max=10, 
    ) # type: ignore
    var_prop23: BoolProperty(
        name="Auto-Set Periodicity",
        default=0,
    ) # type: ignore
    var_prop24: BoolProperty(
        name="No Transparency",
        default=0,
    ) # type: ignore
    var_prop25: BoolProperty(
        name="External Transparency",
        default=1,
    ) # type: ignore
    var_prop26: BoolProperty(
        name="Mirror Effect",
        default=0,
    ) # type: ignore
    var_prop27: BoolProperty(
        name="Untwist",
        default=0,
    ) # type: ignore
    var_prop28: BoolProperty(
        name="Do Not Flatten Transparency",
        default=0,
    ) # type: ignore
    var_prop30: BoolProperty(
        name="Show Grid",
        default=0,
    ) # type: ignore
    var_prop31: BoolProperty(
        name="Show Frame",
        default=0,
    ) # type: ignore
    var_prop33: BoolProperty(
        name="Antialiasing",
        default=1,
    ) # type: ignore
    var_prop34: EnumProperty(
        name="Edge Behavior X",
        default="0",
        items=create_enum(["Blank", "Wrap", "Reflect", "Rotate"]),
    ) # type: ignore
    var_prop35: EnumProperty(
        name="Edge Behavior Y",
        default="0",
        items=create_enum(["Blank", "Wrap", "Reflect", "Rotate"]),
    ) # type: ignore

    def create_command(self):
        return f"souphead_droste10 {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{int(self.var_prop14)},{self.var_prop15},{self.var_prop16},{self.var_prop17},{int(self.var_prop19)},{int(self.var_prop20)},{self.var_prop21},{int(self.var_prop23)},{int(self.var_prop24)},{int(self.var_prop25)},{int(self.var_prop26)},{int(self.var_prop27)},{int(self.var_prop28)},{int(self.var_prop30)},{int(self.var_prop31)},{int(self.var_prop33)},{self.var_prop34},{self.var_prop35}"

################################################################################
################################################################################

class GMIC_FDeform_crease(GMICBaseNode):
    """Crease by Author: David Tschumperlé. Latest Update: 2018/01/22."""
    # fx_crease

    bl_idname = "FDeform_crease"
    bl_label = "Crease"

    node_props = ["var_prop0", "var_prop1", "var_prop2"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=30.0,
        min=0.0, 
        max=300.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Frequency (%)",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_crease {self.var_prop0},{self.var_prop1},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FDeform_distortlens(GMICBaseNode):
    """Distort Lens by Author: David Tschumperlé. Latest Update: 2017/18/02."""
    # fx_distort_lens

    bl_idname = "FDeform_distortlens"
    bl_label = "Distort Lens"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3_x", "var_prop3_y", "var_prop4"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=0.1,
        min=-1.0, 
        max=1.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Aspect Ratio",
        default=0.0,
        min=-2.0, 
        max=2.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Zoom",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop3_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Boundary",
        default="0",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_distort_lens {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3_x},{self.var_prop3_y},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FDeform_dropwater(GMICBaseNode):
    """Drop Water by Author: David Tschumperlé. Latest Update: 2015/21/07."""
    # fx_drop_water

    bl_idname = "FDeform_dropwater"
    bl_label = "Drop Water"

    node_props = ["var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop16", "var_prop17", "var_prop18", "var_prop19", "var_prop21", "var_prop22"]

    var_prop1: EnumProperty(
        name="Shapes",
        default="0",
        items=create_enum(["Procedural", "Opaque Regions on Top Layer"]),
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Density",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Radius",
        default=2.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Variability",
        default=80.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: IntProperty(
        name="Random Seed",
        default=0,
        min=0, 
        max=16384, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Refraction",
        default=3.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Light Angle",
        default=35.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop11: FloatProperty(
        name="Specular Size",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Specular Intensity",
        default=1.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop13: FloatProperty(
        name="Specular Centering",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop16: FloatProperty(
        name="Shadow Size",
        default=0.25,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop17: FloatProperty(
        name="Shadow Intensity",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop18: FloatProperty(
        name="Shadow Smoothness",
        default=0.75,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop19: FloatProperty(
        name="Diffuse Shadow",
        default=0.05,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop21: FloatProperty(
        name="Smoothness",
        default=0.15,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop22: BoolProperty(
        name="Output as Separate Layers",
        default=1,
    ) # type: ignore

    def create_command(self):
        return f"fx_drop_water {self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop16},{self.var_prop17},{self.var_prop18},{self.var_prop19},{self.var_prop21},{int(self.var_prop22)}"

################################################################################
################################################################################

class GMIC_FDeform_equirectangulartonadirzenith(GMICBaseNode):
    """Equirectangular to Nadir-Zenith by Author: David Tschumperlé. Latest Update: 2015/29/12."""
    # fx_equirectangular2nadirzenith

    bl_idname = "FDeform_equirectangulartonadirzenith"
    bl_label = "Equirectangular to Nadir-Zenith"

    node_props = ["var_prop0"]

    var_prop0: EnumProperty(
        name="Mode",
        default="0",
        items=create_enum(["to Nadir / Zenith", "to Equirectangular"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_equirectangular2nadirzenith {self.var_prop0}"

################################################################################
################################################################################

class GMIC_FDeform_euclideanpolar(GMICBaseNode):
    """Euclidean - Polar by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_euclidean2polar

    bl_idname = "FDeform_euclideanpolar"
    bl_label = "Euclidean - Polar"

    node_props = ["var_prop0_x", "var_prop0_y", "var_prop1", "var_prop2", "var_prop3"]

    var_prop0_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop0_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Stretch Factor",
        default=1.0,
        min=0.1, 
        max=10.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Boundary",
        default="1",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop3: BoolProperty(
        name="Inverse Transform",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_euclidean2polar {self.var_prop0_x},{self.var_prop0_y},{self.var_prop1},{self.var_prop2},{int(self.var_prop3)}"

################################################################################
################################################################################

class GMIC_FDeform_flower(GMICBaseNode):
    """Flower by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_flower

    bl_idname = "FDeform_flower"
    bl_label = "Flower"

    node_props = ["var_prop0_x", "var_prop0_y", "var_prop1_x", "var_prop1_y", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop0_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_x: FloatProperty(
        name="Amplitude / Angle X",
        default=75.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_y: FloatProperty(
        name="Amplitude / Angle Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2: IntProperty(
        name="Petals",
        default=6,
        min=2, 
        max=20, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Offset (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_flower {self.var_prop0_x},{self.var_prop0_y},{self.var_prop1_x},{self.var_prop1_y},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FDeform_kaleidoscopeblended(GMICBaseNode):
    """Kaleidoscope [Blended] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_rotoidoscope

    bl_idname = "FDeform_kaleidoscopeblended"
    bl_label = "Kaleidoscope [Blended]"

    node_props = ["var_prop0_x", "var_prop0_y", "var_prop1", "var_prop2", "var_prop3"]

    var_prop0_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop0_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Angular Tiles",
        default=10,
        min=1, 
        max=72, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness",
        default=0.5,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_rotoidoscope {self.var_prop0_x},{self.var_prop0_y},{self.var_prop1},{self.var_prop2},{self.var_prop3}"

################################################################################
################################################################################

class GMIC_FDeform_kaleidoscopepolar(GMICBaseNode):
    """Kaleidoscope [Polar] by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_kaleidoscope

    bl_idname = "FDeform_kaleidoscopepolar"
    bl_label = "Kaleidoscope [Polar]"

    node_props = ["var_prop0_x", "var_prop0_y", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5"]

    var_prop0_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop0_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="X-Offset (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Y-Offset (%)",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Radius Cut",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Angle Cut",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_kaleidoscope {self.var_prop0_x},{self.var_prop0_y},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5}"

################################################################################
################################################################################

class GMIC_FDeform_kaleidoscopereptorianpolar(GMICBaseNode):
    """Kaleidoscope [Reptorian-Polar] by Author: Reptorian. Latest Update: 2019/9/7."""
    # gui_rep_polkal

    bl_idname = "FDeform_kaleidoscopereptorianpolar"
    bl_label = "Kaleidoscope [Reptorian-Polar]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3_x", "var_prop3_y", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop12", "var_prop13"]

    var_prop0: FloatProperty(
        name="Angle Cut",
        default=2.0,
        min=.01, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Radius Cut",
        default=1.0,
        min=.01, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Surface Angle",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop3_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4: BoolProperty(
        name="Flip Angle Direction?",
        default=0,
    ) # type: ignore
    var_prop5: BoolProperty(
        name="Flip Radial Direction?",
        default=0,
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Angle Edge Behaviour",
        default="1",
        items=create_enum(["Repeat", "Alternating"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Radial Edge Behaviour",
        default="2",
        items=create_enum(["None", "Repeat", "Alternating"]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Fit Radial End to Min/Max Dimension",
        default="0",
        items=create_enum(["Minimum Dimension", "Maximum Dimension"]),
    ) # type: ignore
    var_prop9: BoolProperty(
        name="Conical Start at 0?",
        default=1,
    ) # type: ignore
    var_prop12: FloatProperty(
        name="Sublevel",
        default=.5,
        min=0.0, 
        max=3.0, 
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Interpolation",
        default="2",
        items=create_enum(["Nearest", "Average", "Linear", "Grid", "Bicubic", "Lanczos"]),
    ) # type: ignore

    def create_command(self):
        return f"gui_rep_polkal {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3_x},{self.var_prop3_y},{int(self.var_prop4)},{int(self.var_prop5)},{self.var_prop6},{self.var_prop7},{self.var_prop8},{int(self.var_prop9)},{self.var_prop12},{self.var_prop13}"

################################################################################
################################################################################

class GMIC_FDeform_kaleidoscopesymmetry(GMICBaseNode):
    """Kaleidoscope [Symmetry] by Author: David Tschumperlé. Latest Update: 2013/07/01."""
    # fx_symmetrizoscope

    bl_idname = "FDeform_kaleidoscopesymmetry"
    bl_label = "Kaleidoscope [Symmetry]"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3"]

    var_prop0: IntProperty(
        name="Iterations",
        default=4,
        min=1, 
        max=32, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Symmetry Sides",
        default="0",
        items=create_enum(["Backward", "Forward", "Swap"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_symmetrizoscope {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3}"

################################################################################
################################################################################

class GMIC_FDeform_logarithmicdistortion(GMICBaseNode):
    """Logarithmic Distortion by Author: Reptorian. Latest Update: 2019/6/4."""
    # rep_logpindis_gui

    bl_idname = "FDeform_logarithmicdistortion"
    bl_label = "Logarithmic Distortion"

    node_props = ["var_prop2", "var_prop3_x", "var_prop3_y", "var_prop4_x", "var_prop4_y", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10", "var_prop11", "var_prop12", "var_prop13", "var_prop14", "var_prop15", "var_prop16", "var_prop17", "var_prop19"]

    var_prop2: FloatProperty(
        name="Distortion Factor",
        default=1.0,
        min=.1, 
        max=1000.0, 
    ) # type: ignore
    var_prop3_x: FloatProperty(
        name="Preliminary Surface Shift X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3_y: FloatProperty(
        name="Preliminary Surface Shift Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4_x: FloatProperty(
        name="Distortion Surface Position X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4_y: FloatProperty(
        name="Distortion Surface Position Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Preliminary X-Axis Scaling",
        default=1.0,
        min=.1, 
        max=10.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Preliminary Y-Axis Scaling",
        default=1.0,
        min=.1, 
        max=10.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Effect X-Axis Scaling",
        default=1.0,
        min=.1, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Effect Y-Axis Scaling",
        default=1.0,
        min=.1, 
        max=10.0, 
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Distortion Surface Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop10: EnumProperty(
        name="Placement",
        default="0",
        items=create_enum(["Inside-Out", "Outside-In"]),
    ) # type: ignore
    var_prop11: EnumProperty(
        name="Logarithmic Distortion Axis Combination for X-Axis",
        default="0",
        items=create_enum(["Different Axis", "Same Axis"]),
    ) # type: ignore
    var_prop12: EnumProperty(
        name="Logarithmic Distortion Axis combination for y-Axis",
        default="0",
        items=create_enum(["Different Axis", "Same Axis"]),
    ) # type: ignore
    var_prop13: EnumProperty(
        name="Logarithmic Distortion X-Axis Direction",
        default="0",
        items=create_enum(["Negative", "Positive"]),
    ) # type: ignore
    var_prop14: EnumProperty(
        name="Logarithmic Distortion Y-Axis Direction",
        default="0",
        items=create_enum(["Negative", "Positive"]),
    ) # type: ignore
    var_prop15: EnumProperty(
        name="Boundary Condition",
        default="0",
        items=create_enum(["Periodic", "Mirror"]),
    ) # type: ignore
    var_prop16: EnumProperty(
        name="Interpolation",
        default="2",
        items=create_enum(["Nearest", "Linear", "Bicubic"]),
    ) # type: ignore
    var_prop17: IntProperty(
        name="Base Reference Dimension",
        default=1024,
        min=10, 
        max=4096, 
    ) # type: ignore
    var_prop19: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"rep_logpindis_gui {self.var_prop2},{self.var_prop3_x},{self.var_prop3_y},{self.var_prop4_x},{self.var_prop4_y},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10},{self.var_prop11},{self.var_prop12},{self.var_prop13},{self.var_prop14},{self.var_prop15},{self.var_prop16},{self.var_prop17},{self.var_prop19},50,50"

################################################################################
################################################################################

class GMIC_FDeform_moon2panorama(GMICBaseNode):
    """Moon2panorama by """
    # moon2panorama

    bl_idname = "FDeform_moon2panorama"
    bl_label = "Moon2panorama"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop7", "var_prop8", "var_prop9"]

    var_prop0: BoolProperty(
        name="Center Help",
        default=0,
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Center X",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Center Y",
        default=0.0,
        min=-20.0, 
        max=20.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Span",
        default=360.0,
        min=0.0, 
        max=1450.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Shift X",
        default=0.0,
        min=-200.0, 
        max=200.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Shift Y",
        default=0.0,
        min=-200.0, 
        max=200.0, 
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Antialiasing",
        default=1,
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Edge Behavior X",
        default="0",
        items=create_enum(["Blank", "Wrap", "Reflect", "Rotate"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Edge Behavior Y",
        default="0",
        items=create_enum(["Blank", "Wrap", "Reflect", "Rotate"]),
    ) # type: ignore

    def create_command(self):
        return f"moon2panorama {int(self.var_prop0)},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{int(self.var_prop7)},{self.var_prop8},{self.var_prop9}"

################################################################################
################################################################################

class GMIC_FDeform_perspective(GMICBaseNode):
    """Perspective by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_warp_perspective

    bl_idname = "FDeform_perspective"
    bl_label = "Perspective"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3_x", "var_prop3_y", "var_prop4", "var_prop5", "var_prop6"]

    var_prop0: FloatProperty(
        name="X-Angle",
        default=1.73,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Y-Angle",
        default=0.0,
        min=-4.0, 
        max=4.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Zoom",
        default=1.0,
        min=0.1, 
        max=4.0, 
    ) # type: ignore
    var_prop3_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="X-Offset",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Y-Offset",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Boundary",
        default="2",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_warp_perspective {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3_x},{self.var_prop3_y},{self.var_prop4},{self.var_prop5},{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FDeform_pixelpush(GMICBaseNode):
    """Pixel Push by Author: Reptorian. Latest Update: 2020/2/26."""
    # fx_rep_pxpush

    bl_idname = "FDeform_pixelpush"
    bl_label = "Pixel Push"

    node_props = ["var_prop0_x", "var_prop0_y", "var_prop4"]

    var_prop0_x: FloatProperty(
        name="Push Point X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop0_y: FloatProperty(
        name="Push Point Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_rep_pxpush {self.var_prop0_x},{self.var_prop0_y},{self.var_prop4},50,50"

################################################################################
################################################################################

class GMIC_FDeform_pointwarp(GMICBaseNode):
    """Point Warp by Author: Reptorian Latest update: 2020/2/26."""
    # gui_rep_pw

    bl_idname = "FDeform_pointwarp"
    bl_label = "Point Warp"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3_x", "var_prop3_y", "var_prop4", "var_prop5", "var_prop7"]

    var_prop0: FloatProperty(
        name="Point Width",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Distance",
        default=100.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Radial Influence",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop3_x: FloatProperty(
        name="Placement of Distortion X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3_y: FloatProperty(
        name="Placement of Distortion Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Distortion Angle",
        default=0.0,
        min=-180.0, 
        max=180.0, 
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Boundary Condition",
        default="3",
        items=create_enum(["None", "Neumann", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"gui_rep_pw {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3_x},{self.var_prop3_y},{self.var_prop4},{self.var_prop5},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FDeform_polartransform(GMICBaseNode):
    """Polar Transform by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_transform_polar

    bl_idname = "FDeform_polartransform"
    bl_label = "Polar Transform"

    node_props = ["var_prop0", "var_prop1_x", "var_prop1_y", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: EnumProperty(
        name="Preset",
        default="0",
        items=create_enum(["Custom Transform", "Inverse Radius", "Swap Radius / Angle"]),
    ) # type: ignore
    var_prop1_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2: StringProperty(
        name="Radius",
        default="r + R/10*cos(a*5)",
    ) # type: ignore
    var_prop3: StringProperty(
        name="Angle",
        default="a",
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_transform_polar {self.var_prop0},{self.var_prop1_x},{self.var_prop1_y},\\\"{self.var_prop2}\\\",\\\"{self.var_prop3}\\\",{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FDeform_quadrangle(GMICBaseNode):
    """Quadrangle by Author: David Tschumperlé. Latest Update: 2017/10/11."""
    # fx_quadrangle

    bl_idname = "FDeform_quadrangle"
    bl_label = "Quadrangle"

    node_props = ["var_prop0_x", "var_prop0_y", "var_prop1_x", "var_prop1_y", "var_prop2_x", "var_prop2_y", "var_prop3_x", "var_prop3_y", "var_prop4", "var_prop5", "var_prop6"]

    var_prop0_x: FloatProperty(
        name="Top-Left Vertex (%) X",
        default=5.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop0_y: FloatProperty(
        name="Top-Left Vertex (%) Y",
        default=5.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_x: FloatProperty(
        name="Top-Right Vertex (%) X",
        default=95.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_y: FloatProperty(
        name="Top-Right Vertex (%) Y",
        default=25.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2_x: FloatProperty(
        name="Bottom-Right Vertex (%) X",
        default=60.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2_y: FloatProperty(
        name="Bottom-Right Vertex (%) Y",
        default=95.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3_x: FloatProperty(
        name="Bottom-Left Vertex (%) X",
        default=40.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3_y: FloatProperty(
        name="Bottom-Left Vertex (%) Y",
        default=95.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Interpolation",
        default="1",
        items=create_enum(["Nearest Neighbor", "Linear"]),
    ) # type: ignore
    var_prop5: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="1",
        items=create_enum(["Input", "Output", "Both"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_quadrangle {self.var_prop0_x},{self.var_prop0_y},{self.var_prop1_x},{self.var_prop1_y},{self.var_prop2_x},{self.var_prop2_y},{self.var_prop3_x},{self.var_prop3_y},{self.var_prop4},{self.var_prop5},{self.var_prop6}"

################################################################################
################################################################################

class GMIC_FDeform_raindrops(GMICBaseNode):
    """Raindrops by Author: David Tschumperlé. Latest Update: 2012/28/11."""
    # raindrops

    bl_idname = "FDeform_raindrops"
    bl_label = "Raindrops"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=80.0,
        min=0.0, 
        max=300.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Density",
        default=0.1,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Wavelength",
        default=1.0,
        min=0.0, 
        max=2.0, 
    ) # type: ignore
    var_prop3: IntProperty(
        name="Merging Steps",
        default=0,
        min=0, 
        max=20, 
    ) # type: ignore

    def create_command(self):
        return f"raindrops {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3}"

################################################################################
################################################################################

class GMIC_FDeform_random(GMICBaseNode):
    """Random by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # deform

    bl_idname = "FDeform_random"
    bl_label = "Random"

    node_props = ["var_prop0"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=10.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore

    def create_command(self):
        return f"deform {self.var_prop0}"

################################################################################
################################################################################

class GMIC_FDeform_reflection(GMICBaseNode):
    """Reflection by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_reflect

    bl_idname = "FDeform_reflection"
    bl_label = "Reflection"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8"]

    var_prop0: FloatProperty(
        name="Height",
        default=50.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Attenuation",
        default=1.0,
        min=0.1, 
        max=4.0, 
    ) # type: ignore
    var_prop2: FloatVectorProperty(
        name="Color",
        default=(0.43137254901960786,0.6274509803921569,0.7450980392156863),
        min=0.0, 
        max=1.0, 
        subtype="COLOR",
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Waves Amplitude",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Waves Smoothness",
        default=1.5,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="X-Angle",
        default=0.0,
        min=-10.0, 
        max=10.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Y-Angle",
        default=-3.30,
        min=-10.0, 
        max=10.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Focale",
        default=7.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop8: FloatProperty(
        name="Zoom",
        default=1.5,
        min=1.0, 
        max=5.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_reflect {self.var_prop0},{self.var_prop1},{self.var_prop2[0]*255},{self.var_prop2[1]*255},{self.var_prop2[2]*255},255,{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8}"

################################################################################
################################################################################

class GMIC_FDeform_lylejkripple(GMICBaseNode):
    """Lylejk Ripple by Author: &lt;a href&#x3D;&quot;https://goo.gl/Ryf7Cv&quot;&gt;David Tschumperlé&lt;/a&gt;. Latest update: 2011/23/08."""
    # ripple

    bl_idname = "FDeform_lylejkripple"
    bl_label = "Lylejk Ripple"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=10.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Bandwidth",
        default=20.0,
        min=1.0, 
        max=300.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Shape",
        default="2",
        items=create_enum(["Bloc", "Triangle", "Sine", "Sine+", "Random"]),
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Angle",
        default=0.0,
        min=-360.0, 
        max=360.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Offset",
        default=0.0,
        min=-500.0, 
        max=500.0, 
    ) # type: ignore

    def create_command(self):
        return f"ripple {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4}"

################################################################################
################################################################################

class GMIC_FDeform_sinusoidalwaterdistortion(GMICBaseNode):
    """Sinusoidal Water Distortion by Author: Reptorian. Latest Update: 2019/6/4."""
    # rep_sinowaterdist_gui

    bl_idname = "FDeform_sinusoidalwaterdistortion"
    bl_label = "Sinusoidal Water Distortion"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6"]

    var_prop0: FloatProperty(
        name="X-Balance",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Y-Balance",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Scale",
        default=.5,
        min=.1, 
        max=100.0, 
    ) # type: ignore
    var_prop3: EnumProperty(
        name="Interpolation",
        default="2",
        items=create_enum(["Nearest", "Linear", "Bicubic"]),
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Boundary Condition",
        default="0",
        items=create_enum(["Periodic", "Mirror"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"rep_sinowaterdist_gui {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},50,50"

################################################################################
################################################################################

class GMIC_FDeform_sphere(GMICBaseNode):
    """Sphere by Author: David Tschumperlé. Latest Update: 2011/07/11."""
    # fx_map_sphere

    bl_idname = "FDeform_sphere"
    bl_label = "Sphere"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7", "var_prop8", "var_prop9", "var_prop10"]

    var_prop0: IntProperty(
        name="Width",
        default=512,
        min=1, 
        max=4096, 
    ) # type: ignore
    var_prop1: IntProperty(
        name="Height",
        default=512,
        min=1, 
        max=4096, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Radius",
        default=90.0,
        min=0.0, 
        max=400.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Dilation",
        default=0.5,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Angle",
        default=0.0,
        min=-50.0, 
        max=50.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Border Smoothness",
        default=0.0,
        min=0.0, 
        max=200.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="Border Width",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Orientation",
        default="0",
        items=create_enum(["0 deg.", "90 deg.", "180 deg.", "270 deg."]),
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Background",
        default="0",
        items=create_enum(["Transparent", "Mean Color"]),
    ) # type: ignore
    var_prop9: FloatProperty(
        name="Fading",
        default=0.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop10: FloatProperty(
        name="Fading Shape",
        default=0.5,
        min=0.0, 
        max=3.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_map_sphere {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},{self.var_prop8},{self.var_prop9},{self.var_prop10}"

################################################################################
################################################################################

class GMIC_FDeform_spherize(GMICBaseNode):
    """Spherize by Author: David Tschumperlé. Latest Update: 2017/10/03."""
    # fx_spherize

    bl_idname = "FDeform_spherize"
    bl_label = "Spherize"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3_x", "var_prop3_y", "var_prop4", "var_prop5", "var_prop6", "var_prop7"]

    var_prop0: FloatProperty(
        name="Radius (%)",
        default=50.0,
        min=0.0, 
        max=300.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Strength",
        default=1.0,
        min=-10.0, 
        max=10.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Smoothness (%)",
        default=0.0,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop3_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Ratio",
        default=0.0,
        min=-2.0, 
        max=2.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Angle",
        default=0.0,
        min=-90.0, 
        max=90.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Interpolation",
        default="2",
        items=create_enum(["Nearest Neighbor", "Linear", "Cubic"]),
    ) # type: ignore
    var_prop7: BoolProperty(
        name="Preview Grid",
        default=0,
    ) # type: ignore

    def create_command(self):
        return f"fx_spherize {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3_x},{self.var_prop3_y},{self.var_prop4},{self.var_prop5},{self.var_prop6},{int(self.var_prop7)}"

################################################################################
################################################################################

class GMIC_FDeform_squaretocircle(GMICBaseNode):
    """Square to Circle by Author: David Tschumperlé. Latest Update: 2017/10/30."""
    # fx_square_circle

    bl_idname = "FDeform_squaretocircle"
    bl_label = "Square to Circle"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop4", "var_prop5", "var_prop6", "var_prop7"]

    var_prop0: EnumProperty(
        name="Mode",
        default="0",
        items=create_enum(["Square to Circle", "Circle to Square"]),
    ) # type: ignore
    var_prop1: EnumProperty(
        name="Interpolation",
        default="1",
        items=create_enum(["Nearest Neighbor", "Linear"]),
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Boundary",
        default="0",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore
    var_prop4: FloatProperty(
        name="X-Factor (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Y-Factor (%)",
        default=0.0,
        min=-100.0, 
        max=100.0, 
    ) # type: ignore
    var_prop6: FloatProperty(
        name="X-Offset (%)",
        default=0.0,
        min=-300.0, 
        max=300.0, 
    ) # type: ignore
    var_prop7: FloatProperty(
        name="Y-Offset (%)",
        default=0.0,
        min=-300.0, 
        max=300.0, 
    ) # type: ignore

    def create_command(self):
        return f"fx_square_circle {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7}"

################################################################################
################################################################################

class GMIC_FDeform_stereographicprojection(GMICBaseNode):
    """Stereographic Projection by Author: David Tschumperlé. Latest Update: 2018/07/04."""
    # fx_project_stereographic

    bl_idname = "FDeform_stereographicprojection"
    bl_label = "Stereographic Projection"

    node_props = ["var_prop0", "var_prop1_x", "var_prop1_y", "var_prop2_x", "var_prop2_y", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop7"]

    var_prop0: EnumProperty(
        name="Transform",
        default="0",
        items=create_enum(["Direct", "Inverse"]),
    ) # type: ignore
    var_prop1_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2_x: FloatProperty(
        name="Radius / Angle X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2_y: FloatProperty(
        name="Radius / Angle Y",
        default=75.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Horizon Leveling (deg)",
        default=0.0,
        min=-10.0, 
        max=10.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Left / Right Blur (%)",
        default=0.0,
        min=0.0, 
        max=20.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Dilation",
        default=0.0,
        min=-2.0, 
        max=2.0, 
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Mirror",
        default="0",
        items=create_enum(["None", "X-Axis", "Y-Axis", "XY-Axis"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Boundary",
        default="0",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_project_stereographic {self.var_prop0},{self.var_prop1_x},{self.var_prop1_y},{self.var_prop2_x},{self.var_prop2_y},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop7},50,50"

################################################################################
################################################################################

class GMIC_FDeform_texturedglass(GMICBaseNode):
    """Textured Glass by Author: David Tschumperlé. Latest Update: 2013/21/11."""
    # fx_textured_glass

    bl_idname = "FDeform_texturedglass"
    bl_label = "Textured Glass"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop5", "var_prop6", "var_prop8"]

    var_prop0: FloatProperty(
        name="X-Amplitude",
        default=40.0,
        min=0.0, 
        max=400.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Y-Amplitude",
        default=40.0,
        min=0.0, 
        max=400.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="X-Smoothness",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Y-Smoothness",
        default=1.0,
        min=0.0, 
        max=5.0, 
    ) # type: ignore
    var_prop4: FloatProperty(
        name="Edge Attenuation",
        default=0.0,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop5: FloatProperty(
        name="Edge Influence",
        default=2.0,
        min=0.0, 
        max=10.0, 
    ) # type: ignore
    var_prop6: IntProperty(
        name="Noise Scale",
        default=0,
        min=0, 
        max=16, 
    ) # type: ignore
    var_prop8: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_textured_glass {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop5},{self.var_prop6},{self.var_prop8},50,50"

################################################################################
################################################################################

class GMIC_FDeform_twirl(GMICBaseNode):
    """Twirl by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_twirl

    bl_idname = "FDeform_twirl"
    bl_label = "Twirl"

    node_props = ["var_prop0", "var_prop1_x", "var_prop1_y", "var_prop2"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=1.0,
        min=-5.0, 
        max=5.0, 
    ) # type: ignore
    var_prop1_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Boundary",
        default="3",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_twirl {self.var_prop0},{self.var_prop1_x},{self.var_prop1_y},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FDeform_water(GMICBaseNode):
    """Water by Author: David Tschumperlé. Latest Update: 2016/07/10."""
    # water

    bl_idname = "FDeform_water"
    bl_label = "Water"

    node_props = ["var_prop0", "var_prop1", "var_prop2"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=30.0,
        min=0.0, 
        max=300.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Smoothness",
        default=1.5,
        min=0.0, 
        max=4.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Angle",
        default=45.0,
        min=0.0, 
        max=180.0, 
    ) # type: ignore

    def create_command(self):
        return f"water {self.var_prop0},{self.var_prop1},{self.var_prop2}"

################################################################################
################################################################################

class GMIC_FDeform_wave(GMICBaseNode):
    """Wave by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # wave

    bl_idname = "FDeform_wave"
    bl_label = "Wave"

    node_props = ["var_prop0", "var_prop1", "var_prop2_x", "var_prop2_y"]

    var_prop0: FloatProperty(
        name="Amplitude",
        default=10.0,
        min=0.0, 
        max=30.0, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Frequency",
        default=0.4,
        min=0.0, 
        max=2.0, 
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

    def create_command(self):
        return f"wave {self.var_prop0},{self.var_prop1},{self.var_prop2_x},{self.var_prop2_y}"

################################################################################
################################################################################

class GMIC_FDeform_wind(GMICBaseNode):
    """Wind by Author: David Tschumperlé. Latest Update: 2023/05/26."""
    # fx_wind

    bl_idname = "FDeform_wind"
    bl_label = "Wind"

    node_props = ["var_prop0", "var_prop1", "var_prop2", "var_prop3", "var_prop4", "var_prop6", "var_prop7", "var_prop9"]

    var_prop0: IntProperty(
        name="Amplitude",
        default=20,
        min=0, 
        max=500, 
    ) # type: ignore
    var_prop1: FloatProperty(
        name="Angle",
        default=0.0,
        min=0.0, 
        max=360.0, 
    ) # type: ignore
    var_prop2: FloatProperty(
        name="Attenuation",
        default=0.7,
        min=0.0, 
        max=1.0, 
    ) # type: ignore
    var_prop3: FloatProperty(
        name="Threshold",
        default=20.0,
        min=0.0, 
        max=100.0, 
    ) # type: ignore
    var_prop4: EnumProperty(
        name="Mode",
        default="1",
        items=create_enum(["Darker", "Brighter"]),
    ) # type: ignore
    var_prop6: EnumProperty(
        name="Channel(s)",
        default="0",
        items=create_enum(["All", "RGBA [All]", "RGB [All]", "RGB [Red]", "RGB [Green]", "RGB [Blue]", "RGBA [Alpha]", "Linear RGB [All]", "Linear RGB [Red]", "Linear RGB [Green]", "Linear RGB [Blue]", "YCbCr [Luminance]", "YCbCr [Blue-Red Chrominances]", "YCbCr [Blue Chrominance]", "YCbCr [Red Chrominance]", "YCbCr [Green Chrominance]", "Lab [Lightness]", "Lab [ab-Chrominances]", "Lab [a-Chrominance]", "Lab [b-Chrominance]", "Lch [ch-Chrominances]", "Lch [c-Chrominance]", "Lch [h-Chrominance]", "HSV [Hue]", "HSV [Saturation]", "HSV [Value]", "HSI [Intensity]", "HSL [Lightness]", "CMYK [Cyan]", "CMYK [Magenta]", "CMYK [Yellow]", "CMYK [Key]", "YIQ [Luma]", "YIQ [Chromas]", "RYB [All]", "RYB [Red]", "RYB [Yellow]", "RYB [Blue]"]),
    ) # type: ignore
    var_prop7: EnumProperty(
        name="Value Action",
        default="0",
        items=create_enum(["None", "Cut", "Normalize"]),
    ) # type: ignore
    var_prop9: EnumProperty(
        name="Preview Type",
        default="0",
        items=create_enum(["Full", "Forward Horizontal", "Forward Vertical", "Backward Horizontal", "Backward Vertical", "Duplicate Top", "Duplicate Left", "Duplicate Bottom", "Duplicate Right", "Duplicate Horizontal", "Duplicate Vertical", "Checkered", "Checkered Inverse"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_wind {self.var_prop0},{self.var_prop1},{self.var_prop2},{self.var_prop3},{self.var_prop4},{self.var_prop6},{self.var_prop7},{self.var_prop9},50,50"

################################################################################
################################################################################

class GMIC_FDeform_zoom(GMICBaseNode):
    """Zoom by Author: David Tschumperlé. Latest Update: 2010/29/12."""
    # fx_zoom

    bl_idname = "FDeform_zoom"
    bl_label = "Zoom"

    node_props = ["var_prop0", "var_prop1_x", "var_prop1_y", "var_prop2"]

    var_prop0: FloatProperty(
        name="Factor",
        default=2.0,
        min=0.01, 
        max=10.0, 
    ) # type: ignore
    var_prop1_x: FloatProperty(
        name="Center (%) X",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop1_y: FloatProperty(
        name="Center (%) Y",
        default=50.0,
        min=0.0, 
        max=10000.0, 
    ) # type: ignore
    var_prop2: EnumProperty(
        name="Boundary",
        default="0",
        items=create_enum(["Transparent", "Nearest", "Periodic", "Mirror"]),
    ) # type: ignore

    def create_command(self):
        return f"fx_zoom {self.var_prop0},{self.var_prop1_x},{self.var_prop1_y},{self.var_prop2}"

################################################################################
################################################################################

node_classes = [
    GMIC_FDeform_breaks, GMIC_FDeform_cartesiantransform, GMIC_FDeform_continuousdroste, GMIC_FDeform_crease, GMIC_FDeform_distortlens, GMIC_FDeform_dropwater, GMIC_FDeform_equirectangulartonadirzenith, GMIC_FDeform_euclideanpolar, GMIC_FDeform_flower, GMIC_FDeform_kaleidoscopeblended,
    GMIC_FDeform_kaleidoscopepolar, GMIC_FDeform_kaleidoscopereptorianpolar, GMIC_FDeform_kaleidoscopesymmetry, GMIC_FDeform_logarithmicdistortion, GMIC_FDeform_moon2panorama, GMIC_FDeform_perspective, GMIC_FDeform_pixelpush, GMIC_FDeform_pointwarp, GMIC_FDeform_polartransform, GMIC_FDeform_quadrangle,
    GMIC_FDeform_raindrops, GMIC_FDeform_random, GMIC_FDeform_reflection, GMIC_FDeform_lylejkripple, GMIC_FDeform_sinusoidalwaterdistortion, GMIC_FDeform_sphere, GMIC_FDeform_spherize, GMIC_FDeform_squaretocircle, GMIC_FDeform_stereographicprojection, GMIC_FDeform_texturedglass,
    GMIC_FDeform_twirl, GMIC_FDeform_water, GMIC_FDeform_wave, GMIC_FDeform_wind, GMIC_FDeform_zoom
]

################################################################################