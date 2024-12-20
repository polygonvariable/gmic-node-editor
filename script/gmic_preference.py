from bpy.types import AddonPreferences
from bpy.props import StringProperty

class GMICPreference(AddonPreferences):

    bl_idname = "gmic-node-editor"
    gmic_path: StringProperty(name="G'MIC Path", description="Path of g'mic binary file", default="gmic")

    def draw(self, context):
        layout = self.layout
        layout.label(text="Settings")
        layout.prop(self, "gmic_path")