from enum import Enum


class MetricTotalComparisonType(str, Enum):
    NONE = "none"
    PREVIOUS_PERIOD = "previous_period"

    def __str__(self) -> str:
        return str(self.value)
