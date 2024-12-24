import bpy

from .node import farray
from .node import fartistic
from .node import fbnw
from .node import fcontours
from .node import fcolor
from .node import fdegradation
from .node import fdeformation
from .node import fdetail
from .node import fframe
from .node import flight
from .node import fpattern
from .node import io

classes = []
classes += farray.classes + fdegradation.classes + fartistic.classes + fcontours.classes + fcolor.classes + io.classes
classes += fbnw.classes + fdeformation.classes + fdetail.classes + fframe.classes + flight.classes + fpattern.classes

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)