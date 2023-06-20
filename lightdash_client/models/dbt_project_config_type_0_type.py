from enum import Enum


class DbtProjectConfigType0Type(str, Enum):
    DBT = "dbt"

    def __str__(self) -> str:
        return str(self.value)
