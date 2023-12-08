from enum import Enum


class EchartsLegendIcon(str, Enum):
    ARROW = "arrow"
    CIRCLE = "circle"
    DIAMOND = "diamond"
    NONE = "none"
    PIN = "pin"
    RECT = "rect"
    ROUNDRECT = "roundRect"
    TRIANGLE = "triangle"

    def __str__(self) -> str:
        return str(self.value)
