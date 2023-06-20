from enum import Enum


class GetProjectResponse200ResultsWarehouseConnectionType0Type(str, Enum):
    SNOWFLAKE = "snowflake"

    def __str__(self) -> str:
        return str(self.value)
