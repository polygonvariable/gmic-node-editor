import bpy

class OP_ExecuteRunGMIC(bpy.types.Operator):
    """Execute Run GMIC Operator"""
    bl_idname = "node.execute_run_gmic"
    bl_label = "Execute Run GMIC"

    def execute(self, context):
        node = context.active_node
        if node and node.bl_idname == "GMIC_IO_OutputNode":
            result = node.execute()
            self.report({'INFO'}, f"Output Node Result: {result}")
        else:
            self.report({'WARNING'}, "Active node is not an Output Node")
        return {'FINISHED'}

classes = [ OP_ExecuteRunGMIC ]