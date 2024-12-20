import bpy
from nodeitems_utils import NodeCategory, NodeItem, register_node_categories, unregister_node_categories

from .base import tree
from .node import farray
from .node import fdegradation

classes = []
classes = tree.classes + farray.classes + fdegradation.classes

class GMICCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == tree.GMICNodeTree.bl_idname

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    node_categories = [
        GMICCategory("GMIC_NODES", "Nodes", items=[
            NodeItem(farray.FArrayMirrored.bl_idname),
            NodeItem(fdegradation.FBlur.bl_idname),
        ]),
    ]
    register_node_categories("GMIC_NODES", node_categories)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    unregister_node_categories("GMIC_NODES")