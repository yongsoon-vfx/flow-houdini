import hou
from canvaseventtypes import *


def createEventHandler(uievent, pending_actions):
    if isinstance(uievent, KeyboardEvent):
        if uievent.key == "Space":
            hou.session.SpaceBarState.pressed = True
            return None, False

        if hou.session.SpaceBarState.pressed is False:
            return None, False

        if hou.session.SpaceBarState.pressed is True:
            import flow

            flow.handleKeyPress(uievent)
            hou.session.SpaceBarState.pressed = False

            return None, True

    return None, False
