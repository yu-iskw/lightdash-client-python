from enum import Enum


class ChartSourceType(str, Enum):
    DBT_EXPLORE = "dbt_explore"
    SQL = "sql"

    def __str__(self) -> str:
        return str(self.value)
