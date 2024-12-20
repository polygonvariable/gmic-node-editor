import bpy

class GMICNodeTree(bpy.types.NodeTree):
    """G'MIC Node Editor"""
    bl_idname = "GMIC_NodeTree"
    bl_label = "G'MIC Node Editor"
    bl_icon = "NODETREE"