from enum import Enum


class GetProjectResponse200ResultsWarehouseConnectionType5Type(str, Enum):
    TRINO = "trino"

    def __str__(self) -> str:
        return str(self.value)
