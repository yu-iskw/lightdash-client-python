from enum import Enum


class UpdatePinnedItemOrderType(str, Enum):
    CHART = "chart"
    DASHBOARD = "dashboard"
    SPACE = "space"

    def __str__(self) -> str:
        return str(self.value)
