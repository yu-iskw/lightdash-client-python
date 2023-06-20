from enum import Enum


class ProjectWarehouseConnectionType2Type(str, Enum):
    POSTGRES = "postgres"

    def __str__(self) -> str:
        return str(self.value)
