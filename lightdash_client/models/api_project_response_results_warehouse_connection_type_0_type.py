from enum import Enum


class ApiProjectResponseResultsWarehouseConnectionType0Type(str, Enum):
    SNOWFLAKE = "snowflake"

    def __str__(self) -> str:
        return str(self.value)
