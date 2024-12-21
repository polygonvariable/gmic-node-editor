import bpy

class GMICNodeTree(bpy.types.NodeTree):
    """GMIC Node Tree"""
    bl_idname = "GMIC_NodeTree"
    bl_label = "G'MIC Node Editor"
    bl_icon = "EXPERIMENTAL"

classes = [GMICNodeTree]