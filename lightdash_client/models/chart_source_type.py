from enum import Enum


class ChartSourceType(str, Enum):
    DBT_EXPLORE = "dbt_explore"
    SEMANTIC_LAYER = "semantic_layer"
    SQL = "sql"

    def __str__(self) -> str:
        return str(self.value)
