from .generated.fdegradation_gen import node_classes as gen_classes
from .custom.fdegradation import node_classes

classes = []
classes = node_classes + gen_classes