import bpy

from .base.tree import GMICNodeTree

def register():
    bpy.utils.register_class(GMICNodeTree)

def unregister():
    bpy.utils.unregister_class(GMICNodeTree)