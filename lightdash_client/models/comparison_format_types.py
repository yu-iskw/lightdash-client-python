from enum import Enum


class ComparisonFormatTypes(str, Enum):
    PERCENTAGE = "percentage"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
