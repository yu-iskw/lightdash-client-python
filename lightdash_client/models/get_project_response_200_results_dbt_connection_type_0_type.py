from enum import Enum


class GetProjectResponse200ResultsDbtConnectionType0Type(str, Enum):
    DBT = "dbt"

    def __str__(self) -> str:
        return str(self.value)
