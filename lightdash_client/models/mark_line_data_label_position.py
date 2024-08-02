from enum import Enum


class MarkLineDataLabelPosition(str, Enum):
    END = "end"
    MIDDLE = "middle"
    START = "start"

    def __str__(self) -> str:
        return str(self.value)
