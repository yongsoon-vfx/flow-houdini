import importlib
from pathlib import Path

SCRIPT_PATH = Path(__file__)
KEYMAP_PATH = SCRIPT_PATH.parent.parent / "KeyMap.toml"


def handleKeyPress(uievent):
    key = uievent.rawkey.lower()

    if key == "t":
        data = {
            "event": "createNode",
            "node_name": "xform",
        }
        event = importlib.import_module(f"flow-events.{data['event']}")
        event.run(uievent, **data)


if __name__ == "__main__":
    import sys

    sys.path.append(SCRIPT_PATH.parent)
    print("Keymap Existence: " + str(KEYMAP_PATH.exists()))

    event = importlib.import_module("flow-events.exampleEvent")
    data = {
        "data1": "data1_value",
        "data2": "data2_value",
    }
    event.run("fakeuievent", **data)
