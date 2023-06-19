from enum import Enum


class DbtProjectTypeDBT(str, Enum):
    DBT = "dbt"

    def __str__(self) -> str:
        return str(self.value)
