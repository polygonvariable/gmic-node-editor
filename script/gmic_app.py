import bpy

from .base import tree
from .node import farray
from .node import fdegradation
from .node import fartistic
from .node import fcolor
from .node import io

from .gmic_preference import GMICPreference
from .gmic_category import register as register_category, unregister as unregister_category

classes = []
classes = tree.classes + io.classes + farray.classes + fdegradation.classes + fartistic.classes + fcolor.classes + [GMICPreference]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    register_category()

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    unregister_category()