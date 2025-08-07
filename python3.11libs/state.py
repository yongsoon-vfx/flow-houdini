from dataclasses import dataclass


@dataclass
class SpaceBarState:
    pressed: bool = False
