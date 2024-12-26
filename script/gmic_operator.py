import bpy

from .operator import exec_rungmic
from .operator import exec_render

classes = []
classes += exec_rungmic.classes + exec_render.classes

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)