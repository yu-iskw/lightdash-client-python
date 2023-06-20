from enum import Enum


class DbtLocalProjectConfigType(str, Enum):
    DBT = "dbt"

    def __str__(self) -> str:
        return str(self.value)
