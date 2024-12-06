from enum import Enum


class MetricExplorerComparisonPREVIOUSPERIOD(str, Enum):
    PREVIOUS_PERIOD = "previous_period"

    def __str__(self) -> str:
        return str(self.value)
