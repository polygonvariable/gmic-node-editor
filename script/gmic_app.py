from .gmic_tree import register as register_tree, unregister as unregister_tree
from .gmic_node import register as register_node, unregister as unregister_node
from .gmic_operator import register as register_operator, unregister as unregister_operator
from .gmic_category import register as register_category, unregister as unregister_category
from .gmic_preference import register as register_preference, unregister as unregister_preference

def register():
    register_tree()
    register_node()
    register_operator()
    register_category()
    register_preference()

def unregister():
    unregister_tree()
    unregister_node()
    unregister_operator()
    unregister_category()
    unregister_preference()