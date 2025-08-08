def run(uievent, **kwargs):
    node_name = kwargs.get("node_name")
    if node_name is None:
        print("No node name provided")
        return
    editor = uievent.editor
    position = editor.posFromScreen(uievent.mousepos)
    new_node = editor.pwd().createNode(node_name)

    new_node.setPosition(position - new_node.size() * 0.5)
