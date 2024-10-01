from enum import Enum


class DashboardTileTypesSEMANTICVIEWERCHART(str, Enum):
    SEMANTIC_VIEWER_CHART = "semantic_viewer_chart"

    def __str__(self) -> str:
        return str(self.value)
