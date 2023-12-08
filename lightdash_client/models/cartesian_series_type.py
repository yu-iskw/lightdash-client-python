from enum import Enum


class CartesianSeriesType(str, Enum):
    AREA = "area"
    BAR = "bar"
    LINE = "line"
    SCATTER = "scatter"

    def __str__(self) -> str:
        return str(self.value)
