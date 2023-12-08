from enum import Enum


class EchartsLegendType(str, Enum):
    PLAIN = "plain"
    SCROLL = "scroll"

    def __str__(self) -> str:
        return str(self.value)
