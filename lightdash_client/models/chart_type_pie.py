from enum import Enum


class ChartTypePIE(str, Enum):
    PIE = "pie"

    def __str__(self) -> str:
        return str(self.value)
