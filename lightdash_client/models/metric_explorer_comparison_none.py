from enum import Enum


class MetricExplorerComparisonNONE(str, Enum):
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
