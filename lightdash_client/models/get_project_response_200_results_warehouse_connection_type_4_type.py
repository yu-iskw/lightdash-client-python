from enum import Enum


class GetProjectResponse200ResultsWarehouseConnectionType4Type(str, Enum):
    DATABRICKS = "databricks"

    def __str__(self) -> str:
        return str(self.value)
