from enum import Enum


class CatalogTypeTable(str, Enum):
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
