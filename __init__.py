bl_info = {
    "name": "G'MIC Node Editor",
    "author": "polygonvariable",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "Editor Type > G'MIC Node Editor",
    "description": "Manipulate images using G'MIC",
    "warning": "",
    "doc_url": "https://github.com/polygonvariable/gmic-node-editor",
    "category": "Utility",
}

from .script import gmic_app

def register():
    gmic_app.register()

def unregister():
    gmic_app.unregister()

if __name__ == "__main__":
    gmic_app.register()