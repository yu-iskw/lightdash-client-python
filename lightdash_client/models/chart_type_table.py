from enum import Enum


class ChartTypeTABLE(str, Enum):
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
