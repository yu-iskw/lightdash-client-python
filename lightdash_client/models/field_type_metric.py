from enum import Enum


class FieldTypeMETRIC(str, Enum):
    METRIC = "metric"

    def __str__(self) -> str:
        return str(self.value)
