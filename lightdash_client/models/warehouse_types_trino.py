from enum import Enum


class WarehouseTypesTRINO(str, Enum):
    TRINO = "trino"

    def __str__(self) -> str:
        return str(self.value)
