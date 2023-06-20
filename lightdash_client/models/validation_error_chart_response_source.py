from enum import Enum


class ValidationErrorChartResponseSource(str, Enum):
    CHART = "chart"
    DASHBOARD = "dashboard"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
