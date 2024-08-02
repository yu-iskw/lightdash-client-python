from enum import Enum


class CatalogTypeField(str, Enum):
    FIELD = "field"

    def __str__(self) -> str:
        return str(self.value)
