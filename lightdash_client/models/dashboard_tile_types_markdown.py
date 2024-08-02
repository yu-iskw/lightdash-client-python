from enum import Enum


class DashboardTileTypesMARKDOWN(str, Enum):
    MARKDOWN = "markdown"

    def __str__(self) -> str:
        return str(self.value)
