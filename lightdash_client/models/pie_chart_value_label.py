from enum import Enum


class PieChartValueLabel(str, Enum):
    HIDDEN = "hidden"
    INSIDE = "inside"
    OUTSIDE = "outside"

    def __str__(self) -> str:
        return str(self.value)
