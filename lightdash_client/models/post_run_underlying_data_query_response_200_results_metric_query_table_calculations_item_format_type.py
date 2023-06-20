from enum import Enum


class PostRunUnderlyingDataQueryResponse200ResultsMetricQueryTableCalculationsItemFormatType(str, Enum):
    DEFAULT = "default"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
