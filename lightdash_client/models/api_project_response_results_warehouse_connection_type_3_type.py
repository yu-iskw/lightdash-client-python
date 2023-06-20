from enum import Enum


class ApiProjectResponseResultsWarehouseConnectionType3Type(str, Enum):
    BIGQUERY = "bigquery"

    def __str__(self) -> str:
        return str(self.value)
