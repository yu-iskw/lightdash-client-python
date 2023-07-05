from enum import Enum


class ValidationResponseType0ChartType(str, Enum):
    AREA = "area"
    BIG_NUMBER = "big_number"
    HORIZONTAL_BAR = "horizontal_bar"
    LINE = "line"
    MIXED = "mixed"
    PIE = "pie"
    SCATTER = "scatter"
    TABLE = "table"
    VERTICAL_BAR = "vertical_bar"

    def __str__(self) -> str:
        return str(self.value)
