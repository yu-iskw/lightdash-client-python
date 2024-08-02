from enum import Enum


class DashboardTileTypesLOOM(str, Enum):
    LOOM = "loom"

    def __str__(self) -> str:
        return str(self.value)
