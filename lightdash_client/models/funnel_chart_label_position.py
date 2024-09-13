from enum import Enum


class FunnelChartLabelPosition(str, Enum):
    HIDDEN = "hidden"
    INSIDE = "inside"
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
