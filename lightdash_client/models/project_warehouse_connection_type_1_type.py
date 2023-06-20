from enum import Enum


class ProjectWarehouseConnectionType1Type(str, Enum):
    REDSHIFT = "redshift"

    def __str__(self) -> str:
        return str(self.value)
