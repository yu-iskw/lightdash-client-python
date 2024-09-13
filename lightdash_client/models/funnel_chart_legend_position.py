from enum import Enum


class FunnelChartLegendPosition(str, Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    def __str__(self) -> str:
        return str(self.value)
