from enum import Enum


class WarehouseTypesBIGQUERY(str, Enum):
    BIGQUERY = "bigquery"

    def __str__(self) -> str:
        return str(self.value)
