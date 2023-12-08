from enum import Enum


class EchartsLegendOrient(str, Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    def __str__(self) -> str:
        return str(self.value)
