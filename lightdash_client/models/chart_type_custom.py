from enum import Enum


class ChartTypeCUSTOM(str, Enum):
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
