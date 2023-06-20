from enum import Enum


class PickValidationResponseBaseExcludeKeyofValidationResponseBaseNameSource(str, Enum):
    CHART = "chart"
    DASHBOARD = "dashboard"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
