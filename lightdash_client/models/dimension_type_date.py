from enum import Enum


class DimensionTypeDATE(str, Enum):
    DATE = "date"

    def __str__(self) -> str:
        return str(self.value)
