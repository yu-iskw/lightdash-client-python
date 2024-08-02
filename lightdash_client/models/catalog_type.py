from enum import Enum


class CatalogType(str, Enum):
    FIELD = "field"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
