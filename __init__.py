bl_info = {
    "name": "G'MIC Node Graph",
    "author": "polygonvariable",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "Editor Type > G'MIC Node Graph",
    "description": "Manipulate images using G'MIC",
    "warning": "",
    "doc_url": "",
    "category": "Utility",
}

if "bpy" in locals():
    import importlib
    importlib.reload(gmic_nde)
else:
    from .script import gmic_nde

def register():
    gmic_nde.register()

def unregister():
    gmic_nde.unregister()