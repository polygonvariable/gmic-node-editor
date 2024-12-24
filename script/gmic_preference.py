import bpy
from bpy.types import AddonPreferences
from bpy.props import ( StringProperty, BoolProperty )

from .base.library import get_package_name

class GMICPreference(AddonPreferences):

    bl_idname = get_package_name()
    gmic_path: StringProperty(name="G'MIC Path", description="Path of g'mic binary file", default="gmic", subtype="FILE_PATH") # type: ignore
    #graph_layout: BoolProperty(name="Force RTL",  default=True) # type: ignore
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Settings")
        layout.prop(self, "gmic_path")
        #layout.prop(self, "graph_layout")

def register():
    bpy.utils.register_class(GMICPreference)

def unregister():
    bpy.utils.unregister_class(GMICPreference)