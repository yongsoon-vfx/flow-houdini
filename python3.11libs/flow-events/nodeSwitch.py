import hou


def run(uievent, **kwargs):
    action = kwargs.get("action", "set")
    index_str = uievent.rawkey.lower().lstrip("shift+")
    index = int(index_str) if index_str.isdigit() else None

    match action:
        case "save":
            save(index)

        case "set":
            set(index)


def save(index):
    hou.session.__FlowQuickNodes[index] = hou.selectedNodes()[-1]
    pass


def set(index):
    node = hou.session.__FlowQuickNodes[index]
    if node:
        node.setGenericFlag(hou.nodeFlag.Display, True)
        node.setGenericFlag(hou.nodeFlag.Render, True)
    else:
        print(f"No node saved at index {index}")
    pass
