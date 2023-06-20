from enum import Enum


class WarehouseCredentialsType1Type(str, Enum):
    REDSHIFT = "redshift"

    def __str__(self) -> str:
        return str(self.value)
