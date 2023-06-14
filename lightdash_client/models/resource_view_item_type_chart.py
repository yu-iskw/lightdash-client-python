from enum import Enum


class ResourceViewItemTypeCHART(str, Enum):
    CHART = "chart"

    def __str__(self) -> str:
        return str(self.value)
