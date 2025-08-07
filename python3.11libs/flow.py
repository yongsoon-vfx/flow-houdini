import hou


def handleKeyPress(uievent):
    key = uievent.rawkey.lower()

    if key == "t":
        nodeCreation("xform", uievent)


def nodeCreation(node_name, uievent):
    editor = uievent.editor
    position = editor.posFromScreen(uievent.mousepos)
    new_node = editor.pwd().createNode(node_name)

    new_node.setPosition(position - new_node.size() * 0.5)
