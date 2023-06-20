from enum import Enum


class ProjectWarehouseConnectionType5Type(str, Enum):
    TRINO = "trino"

    def __str__(self) -> str:
        return str(self.value)
