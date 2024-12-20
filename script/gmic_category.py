from nodeitems_utils import NodeCategory, NodeItem, register_node_categories, unregister_node_categories

from .base import tree
from .node import farray
from .node import fdegradation
from .node import io

class GMICCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == tree.GMICNodeTree.bl_idname

def register():
    node_categories = [
        GMICCategory("GMIC_NODES_ARRAY", "Array", items=[
            NodeItem(farray.FArrayMirrored.bl_idname),
        ]),
        GMICCategory("GMIC_NODES_DEGRADE", "Degradation", items=[
            NodeItem(fdegradation.FBlur.bl_idname),
        ]),
        GMICCategory("GMIC_NODES_IO", "IO", items=[
            NodeItem(io.OutputNode.bl_idname),
        ]),
    ]
    register_node_categories("GMIC_NODES", node_categories)


def unregister():
    unregister_node_categories("GMIC_NODES")