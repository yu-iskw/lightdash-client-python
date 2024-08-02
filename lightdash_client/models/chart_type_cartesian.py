from enum import Enum


class ChartTypeCARTESIAN(str, Enum):
    CARTESIAN = "cartesian"

    def __str__(self) -> str:
        return str(self.value)
