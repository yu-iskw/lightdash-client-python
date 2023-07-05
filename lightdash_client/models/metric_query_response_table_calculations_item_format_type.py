from enum import Enum


class MetricQueryResponseTableCalculationsItemFormatType(str, Enum):
    CURRENCY = "currency"
    DEFAULT = "default"
    NUMBER = "number"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
