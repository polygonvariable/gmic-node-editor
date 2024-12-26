import os
import tempfile

import bpy

class OP_ExecuteRenderLayer(bpy.types.Operator):
    """Execute Render Layer"""
    bl_idname = "node.execute_render_layer"
    bl_label = "Execute Render Layer"

    def execute(self, context):
        
        scene = bpy.context.scene

        original_compositing = scene.render.use_compositing
            
        try:
            
            scene.render.use_compositing = False
            
            for view_layer in scene.view_layers:
                
                for vl in scene.view_layers:
                    vl.use = False
                
                view_layer.use = True
                
                output_path = os.path.join(tempfile.gettempdir(), f"{view_layer.name}.png")
                scene.render.filepath = output_path
                
                bpy.ops.render.render(write_still=True)
                
                existing_image = bpy.data.images.get(f"Layer {view_layer.name}")
                if existing_image:
                    existing_image.reload()

                else:
                    new_image = bpy.data.images.load(output_path)
                    new_image.name = f"Layer {view_layer.name}"
                    
            self.report({'INFO'}, f"Render finished")

        except:
            self.report({'ERROR'}, f"Render failed")

        finally:

            for vl in scene.view_layers:
                vl.use = True
            scene.render.use_compositing = original_compositing

        return {'FINISHED'}

classes = [ OP_ExecuteRenderLayer ]