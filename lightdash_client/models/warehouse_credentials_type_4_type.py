from enum import Enum


class WarehouseCredentialsType4Type(str, Enum):
    DATABRICKS = "databricks"

    def __str__(self) -> str:
        return str(self.value)
