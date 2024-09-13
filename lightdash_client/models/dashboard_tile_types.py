from enum import Enum


class DashboardTileTypes(str, Enum):
    LOOM = "loom"
    MARKDOWN = "markdown"
    SAVED_CHART = "saved_chart"
    SQL_CHART = "sql_chart"

    def __str__(self) -> str:
        return str(self.value)
