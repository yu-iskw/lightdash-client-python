from enum import Enum


class ResourceViewItemTypeDASHBOARD(str, Enum):
    DASHBOARD = "dashboard"

    def __str__(self) -> str:
        return str(self.value)
