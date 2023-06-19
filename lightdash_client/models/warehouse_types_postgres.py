from enum import Enum


class WarehouseTypesPOSTGRES(str, Enum):
    POSTGRES = "postgres"

    def __str__(self) -> str:
        return str(self.value)
