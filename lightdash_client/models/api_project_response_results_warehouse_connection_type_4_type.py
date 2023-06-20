from enum import Enum


class ApiProjectResponseResultsWarehouseConnectionType4Type(str, Enum):
    DATABRICKS = "databricks"

    def __str__(self) -> str:
        return str(self.value)
