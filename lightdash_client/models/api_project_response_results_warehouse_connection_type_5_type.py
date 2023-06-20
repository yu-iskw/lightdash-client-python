from enum import Enum


class ApiProjectResponseResultsWarehouseConnectionType5Type(str, Enum):
    TRINO = "trino"

    def __str__(self) -> str:
        return str(self.value)
