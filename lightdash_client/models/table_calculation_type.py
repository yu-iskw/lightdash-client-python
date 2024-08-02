from enum import Enum


class TableCalculationType(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    NUMBER = "number"
    STRING = "string"
    TIMESTAMP = "timestamp"

    def __str__(self) -> str:
        return str(self.value)
