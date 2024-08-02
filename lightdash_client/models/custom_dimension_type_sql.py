from enum import Enum


class CustomDimensionTypeSQL(str, Enum):
    SQL = "sql"

    def __str__(self) -> str:
        return str(self.value)
