from .gmic_tree import register as register_tree, unregister as unregister_tree
from .gmic_node import register as register_node, unregister as unregister_node
from .gmic_preference import register as register_preference, unregister as unregister_preference
from .gmic_category import register as register_category, unregister as unregister_category

def register():
    register_tree()
    register_node()
    register_preference()
    register_category()

def unregister():
    unregister_tree()
    unregister_node()
    unregister_preference()
    unregister_category()