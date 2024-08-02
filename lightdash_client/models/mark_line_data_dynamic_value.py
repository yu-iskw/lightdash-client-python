from enum import Enum


class MarkLineDataDynamicValue(str, Enum):
    AVERAGE = "average"

    def __str__(self) -> str:
        return str(self.value)
