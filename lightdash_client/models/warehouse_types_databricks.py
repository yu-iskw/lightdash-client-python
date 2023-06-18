from enum import Enum


class WarehouseTypesDATABRICKS(str, Enum):
    DATABRICKS = "databricks"

    def __str__(self) -> str:
        return str(self.value)
