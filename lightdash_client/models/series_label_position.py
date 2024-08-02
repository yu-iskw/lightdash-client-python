from enum import Enum


class SeriesLabelPosition(str, Enum):
    BOTTOM = "bottom"
    INSIDE = "inside"
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
