from enum import Enum


class WarehouseTypesSNOWFLAKE(str, Enum):
    SNOWFLAKE = "snowflake"

    def __str__(self) -> str:
        return str(self.value)
