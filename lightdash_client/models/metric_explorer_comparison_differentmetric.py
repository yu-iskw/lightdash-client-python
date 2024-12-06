from enum import Enum


class MetricExplorerComparisonDIFFERENTMETRIC(str, Enum):
    DIFFERENT_METRIC = "different_metric"

    def __str__(self) -> str:
        return str(self.value)
