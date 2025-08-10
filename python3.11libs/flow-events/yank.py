from enum import Enum

import hou


class YankState(Enum):
    NODE_SELECTED = 1
    NO_NODE_SELECTED = 2


def run(uievent, **kwargs):
    action = kwargs.get("action", "copy")
    match action:
        case "copy":
            copy(uievent.editor, **kwargs)
        case "paste":
            position = uievent.editor.posFromScreen(uievent.mousepos)
            paste(uievent.editor, pos=position, **kwargs)
        case _:
            print(f"Unknown action: {action}")


def copy(editor, **kwargs):
    selectedNodes = hou.selectedNodes()

    yankState = YankState.NO_NODE_SELECTED
    if len(selectedNodes) > 0:
        yankState = YankState.NODE_SELECTED

    match yankState:
        case YankState.NODE_SELECTED:
            hou.session.__YankedNodes = selectedNodes

        case YankState.NO_NODE_SELECTED:
            editor.flashMessage("", "No nodes selected to yank", 0.25)
    pass


def paste(editor, **kwargs):
    yankBuffer = hou.session.__YankedNodes
    pos = kwargs.get("pos", None)
    if not yankBuffer:
        editor.flashMessage("", "No nodes in yank buffer", 0.25)
        return

    network = editor.pwd()
    obj_merge = network.createNode("object_merge")
    obj_merge.parm("objpath1").set(yankBuffer[0].path())
    if pos:
        obj_merge.setPosition(pos - obj_merge.size() * 0.5)

    pass
