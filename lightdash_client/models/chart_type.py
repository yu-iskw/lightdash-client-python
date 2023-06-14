from enum import Enum


class ChartType(str, Enum):
    BIG_NUMBER = "big_number"
    CARTESIAN = "cartesian"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
