from enum import Enum


class WarehouseCredentialsType5Type(str, Enum):
    TRINO = "trino"

    def __str__(self) -> str:
        return str(self.value)
