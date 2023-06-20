from enum import Enum


class ProjectWarehouseConnectionType3Type(str, Enum):
    BIGQUERY = "bigquery"

    def __str__(self) -> str:
        return str(self.value)
