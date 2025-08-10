import hou
import nodegraphdisplay as display
from canvaseventtypes import *

DEBUG_MODE = False


def displayPrompt():
    hou.session.__FlowEditor.flashMessage("", "Flow State", 0.25)
    return


def createEventHandler(uievent, pending_actions):
    editor = uievent.editor

    # I don't know how to append to the original volatile hotkeys list, so I just copy over the existing ones from nodegraph.py
    volatile_hotkeys = []
    volatile_hotkeys.append("h.pane.wsheet.view_mode")
    volatile_hotkeys.append("h.pane.wsheet.select_mode")
    volatile_hotkeys.append("h.pane.wsheet.layout_mode")
    volatile_hotkeys.append("h.pane.wsheet.flag1_mode")
    volatile_hotkeys.append("h.pane.wsheet.flag2_mode")
    volatile_hotkeys.append("h.pane.wsheet.flag3_mode")
    volatile_hotkeys.append("h.pane.wsheet.flag4_mode")
    volatile_hotkeys.append("h.pane.wsheet.bypass_mode")
    volatile_hotkeys.append("h.pane.wsheet.visualize_mode")
    volatile_hotkeys.append("h.pane.wsheet.cut_wires_mode")
    volatile_hotkeys.append("h.pane.wsheet.stitch_mode")
    volatile_hotkeys.append("h.pane.wsheet.drop_on_wire_mode")
    volatile_hotkeys.append("h.pane.wsheet.flow_state")
    editor.setVolatileHotkeys(volatile_hotkeys)

    if isinstance(uievent, KeyboardEvent):
        if uievent.key == "h.pane.wsheet.flow_state":
            if DEBUG_MODE:
                from pprint import pp

                pp(uievent)

            if uievent.eventtype == "keydown":
                hou.session.SpaceBarState.pressed = True
                hou.session.__FlowEditor = uievent.editor
                hou.ui.addEventLoopCallback(displayPrompt)

                return None, True
            if uievent.eventtype == "keyup":
                hou.session.SpaceBarState.pressed = False
                hou.ui.removeEventLoopCallback(displayPrompt)
                return None, True

        if hou.session.SpaceBarState.pressed is True:
            import flow

            flow.handleKeyPress(uievent)
            return None, True

        try:
            hou.ui.removeEventLoopCallback(displayPrompt)
        except:
            pass

    return None, False
