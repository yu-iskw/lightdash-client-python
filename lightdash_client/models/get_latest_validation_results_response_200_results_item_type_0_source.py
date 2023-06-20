from enum import Enum


class GetLatestValidationResultsResponse200ResultsItemType0Source(str, Enum):
    CHART = "chart"
    DASHBOARD = "dashboard"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
