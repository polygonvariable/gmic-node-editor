from nodeitems_utils import NodeCategory, NodeItem, register_node_categories, unregister_node_categories

from .base import tree
from .node import farray
from .node import fartistic
from .node import fcolor
from .node import fdegradation
from .node import io

class GMICCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == tree.GMICNodeTree.bl_idname

def CreateCategoryItems(classes):
    categories = []
    for cls in classes:
        categories.append(NodeItem(cls.bl_idname))
    return categories

def register():
    node_categories = [
        GMICCategory("GMIC_NODES_ARRAY", "Array & Tiles", items=CreateCategoryItems(farray.classes)),
        GMICCategory("GMIC_NODES_ARTISTIC", "Artistic", items=CreateCategoryItems(fartistic.classes)),
        GMICCategory("GMIC_NODES_COLOR", "Color", items=CreateCategoryItems(fcolor.classes)),
        GMICCategory("GMIC_NODES_DEGRADE", "Degradation", items=CreateCategoryItems(fdegradation.classes)),
        GMICCategory("GMIC_NODES_IO", "IO", items=[
            NodeItem(io.OutputNode.bl_idname)
        ]),
    ]
    register_node_categories("GMIC_NODES", node_categories)


def unregister():
    unregister_node_categories("GMIC_NODES")