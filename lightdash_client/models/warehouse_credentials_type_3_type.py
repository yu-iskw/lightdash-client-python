from enum import Enum


class WarehouseCredentialsType3Type(str, Enum):
    BIGQUERY = "bigquery"

    def __str__(self) -> str:
        return str(self.value)
