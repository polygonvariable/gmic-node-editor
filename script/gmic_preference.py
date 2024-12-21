from bpy.types import AddonPreferences
from bpy.props import StringProperty

from .base.library import GetPackageName

class GMICPreference(AddonPreferences):

    bl_idname = GetPackageName()
    gmic_path: StringProperty(name="G'MIC Path", description="Path of g'mic binary file", default="gmic", subtype="FILE_PATH") # type: ignore
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Settings")
        layout.prop(self, "gmic_path")
        