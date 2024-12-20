import bpy

class GMICNodeTree(bpy.types.NodeTree):
    """GMIC Node Graph"""
    bl_idname = "GMIC_NodeTree"
    bl_label = "G'MIC Node Graph"
    bl_icon = "NODETREE"

classes = [GMICNodeTree]