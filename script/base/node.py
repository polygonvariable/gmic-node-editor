import bpy

class GMICBaseNode(bpy.types.Node):
    """GMIC Base Node"""
    bl_idname = "GMICBaseNode"
    bl_label = "GMIC Base Node"
    bl_icon = "FILE_SCRIPT"
    bl_width_default = 225
    node_props = []

    def default_in(self):
        self.inputs.new("NodeSocketString", "in")
        self.inputs["in"].hide_value = True

    def default_out(self):
        self.outputs.new("NodeSocketString", "out")

    def init(self, context):
        self.default_in()
        self.default_out()

    def get_input_value(self, input_name):
        input_socket = self.inputs.get(input_name)
        if input_socket and input_socket.is_linked:
            from_node = input_socket.links[0].from_node
            if hasattr(from_node, "execute"):
                return from_node.execute()
        return ""
    
    def draw_buttons(self, context, layout):
        for prop in self.node_props:
            layout.prop(self, prop)
    
    def create_command(self):
        return ""
    
    def finalize_command(self):
        temp_cmd = self.get_input_value("in")
        temp_cmd += " -" + self.create_command()
        return temp_cmd
    
    def execute(self):
        return self.finalize_command()
