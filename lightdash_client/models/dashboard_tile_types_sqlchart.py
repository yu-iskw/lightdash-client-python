from enum import Enum


class DashboardTileTypesSQLCHART(str, Enum):
    SQL_CHART = "sql_chart"

    def __str__(self) -> str:
        return str(self.value)
