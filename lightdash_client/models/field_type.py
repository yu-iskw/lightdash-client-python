from enum import Enum


class FieldType(str, Enum):
    DIMENSION = "dimension"
    METRIC = "metric"

    def __str__(self) -> str:
        return str(self.value)
