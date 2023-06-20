from enum import Enum


class GetProjectResponse200ResultsWarehouseConnectionType1Type(str, Enum):
    REDSHIFT = "redshift"

    def __str__(self) -> str:
        return str(self.value)
