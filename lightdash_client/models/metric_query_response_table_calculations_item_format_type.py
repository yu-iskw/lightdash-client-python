from enum import Enum


class MetricQueryResponseTableCalculationsItemFormatType(str, Enum):
    DEFAULT = "default"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
