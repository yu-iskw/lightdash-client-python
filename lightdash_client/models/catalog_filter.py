from enum import Enum


class CatalogFilter(str, Enum):
    DIMENSIONS = "dimensions"
    METRICS = "metrics"
    TABLES = "tables"

    def __str__(self) -> str:
        return str(self.value)
