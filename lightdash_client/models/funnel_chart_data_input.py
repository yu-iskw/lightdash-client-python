from enum import Enum


class FunnelChartDataInput(str, Enum):
    COLUMN = "column"
    ROW = "row"

    def __str__(self) -> str:
        return str(self.value)
