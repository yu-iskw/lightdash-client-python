from enum import Enum


class EchartsLegendAlign(str, Enum):
    AUTO = "auto"
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
