from enum import Enum


class CustomFormatType(str, Enum):
    CURRENCY = "currency"
    DATE = "date"
    DEFAULT = "default"
    ID = "id"
    NUMBER = "number"
    PERCENT = "percent"
    TIMESTAMP = "timestamp"

    def __str__(self) -> str:
        return str(self.value)
