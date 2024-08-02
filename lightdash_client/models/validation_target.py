from enum import Enum


class ValidationTarget(str, Enum):
    CHARTS = "charts"
    DASHBOARDS = "dashboards"
    TABLES = "tables"

    def __str__(self) -> str:
        return str(self.value)
