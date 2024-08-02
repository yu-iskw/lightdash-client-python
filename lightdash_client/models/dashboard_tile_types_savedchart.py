from enum import Enum


class DashboardTileTypesSAVEDCHART(str, Enum):
    SAVED_CHART = "saved_chart"

    def __str__(self) -> str:
        return str(self.value)
