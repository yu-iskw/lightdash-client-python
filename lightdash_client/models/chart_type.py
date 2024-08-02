from enum import Enum


class ChartType(str, Enum):
    BIG_NUMBER = "big_number"
    CARTESIAN = "cartesian"
    CUSTOM = "custom"
    FUNNEL = "funnel"
    PIE = "pie"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
