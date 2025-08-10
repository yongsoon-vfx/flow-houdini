import hou
from state import SpaceBarState

hou.session.SpaceBarState = SpaceBarState()
hou.session.__FlowQuickNodes = [None] * 9

context_symbol = "h.pane.wsheet"


# Define a new hotkey symbol (command)
hotkey_symbol = f"{context_symbol}.flow_state"
hotkey_label = "Enter Flow State"
hotkey_description = "Switches to the houdini-flow state for rapid node creation"


hou.hotkeys.addCommand(hotkey_symbol, hotkey_label, hotkey_description)


# You can also assign a default hotkey programmatically
# hou.hotkeys.addAssignment(context_symbol, hotkey_symbol, "alt+h")

print(f"Custom hotkey '{hotkey_label}' registered with symbol '{hotkey_symbol}'")
