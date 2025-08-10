import importlib
from pathlib import Path

SCRIPT_PATH = Path(__file__)
KEYMAP_PATH = SCRIPT_PATH.parent.parent / "KeyMap.toml"

DEBUG_MODE = False


def handleKeyPress(uievent):
    import rtoml
    from networkcontext import NetworkType

    keymap_dict = rtoml.load(KEYMAP_PATH)
    key = uievent.rawkey.lower()
    key = key.replace("+", "_")

    if DEBUG_MODE:
        from pprint import pp

        pp(keymap_dict)

    parent_node = uievent.editor.pwd()
    context = NetworkType.get_context(parent_node)
    try:
        event_data = keymap_dict[context.value][key]
    except KeyError:
        event_data = keymap_dict["global"][key]
    event = importlib.import_module(f"flow-events.{event_data['event']}")
    event.run(uievent, **event_data)


# if __name__ == "__main__":
#     import sys

#     sys.path.append(SCRIPT_PATH.parent)
#     print("Keymap Existence: " + str(KEYMAP_PATH.exists()))

#     event = importlib.import_module("flow-events.exampleEvent")
#     data = {
#         "data1": "data1_value",
#         "data2": "data2_value",
#     }
#     event.run("fakeuievent", **data)

#     import rtoml

#     data = rtoml.load(KEYMAP_PATH)
#     print(data["sop"]["t"])
