from enum import Enum


class ApiProjectResponseResultsWarehouseConnectionType2Type(str, Enum):
    POSTGRES = "postgres"

    def __str__(self) -> str:
        return str(self.value)
