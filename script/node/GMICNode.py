import bpy

class GMICNode(bpy.types.Node):
    """GMIC Node"""
    bl_idname = "GMICNode"
    bl_label = "GMIC Node"
    bl_icon = "NODE"

    def default_in(self):
        self.inputs.new("NodeSocketString", "in")
        self.inputs["in"].hide_value = True

    def default_out(self):
        self.outputs.new("NodeSocketString", "out")

    def get_input_value(self, input_name):
        input_socket = self.inputs.get(input_name)
        if input_socket and input_socket.is_linked:
            from_node = input_socket.links[0].from_node
            if hasattr(from_node, "execute"):
                return from_node.execute()
        else:
            return self.inputs[input_name].default_value
        return ""