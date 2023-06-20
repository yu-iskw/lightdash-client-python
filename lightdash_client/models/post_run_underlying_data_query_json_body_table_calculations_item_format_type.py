from enum import Enum


class PostRunUnderlyingDataQueryJsonBodyTableCalculationsItemFormatType(str, Enum):
    DEFAULT = "default"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
