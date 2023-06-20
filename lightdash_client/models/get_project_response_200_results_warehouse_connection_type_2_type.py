from enum import Enum


class GetProjectResponse200ResultsWarehouseConnectionType2Type(str, Enum):
    POSTGRES = "postgres"

    def __str__(self) -> str:
        return str(self.value)
