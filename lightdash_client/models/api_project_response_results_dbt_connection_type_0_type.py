from enum import Enum


class ApiProjectResponseResultsDbtConnectionType0Type(str, Enum):
    DBT = "dbt"

    def __str__(self) -> str:
        return str(self.value)
