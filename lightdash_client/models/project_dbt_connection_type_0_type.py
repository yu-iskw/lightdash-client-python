from enum import Enum


class ProjectDbtConnectionType0Type(str, Enum):
    DBT = "dbt"

    def __str__(self) -> str:
        return str(self.value)
