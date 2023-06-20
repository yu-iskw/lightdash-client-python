from enum import Enum


class WarehouseCredentialsType0Type(str, Enum):
    SNOWFLAKE = "snowflake"

    def __str__(self) -> str:
        return str(self.value)
