from enum import Enum


class ProjectWarehouseConnectionType4Type(str, Enum):
    DATABRICKS = "databricks"

    def __str__(self) -> str:
        return str(self.value)
