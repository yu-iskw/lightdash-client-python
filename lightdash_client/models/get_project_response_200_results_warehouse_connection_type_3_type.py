from enum import Enum


class GetProjectResponse200ResultsWarehouseConnectionType3Type(str, Enum):
    BIGQUERY = "bigquery"

    def __str__(self) -> str:
        return str(self.value)
