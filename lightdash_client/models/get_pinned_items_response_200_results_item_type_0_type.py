from enum import Enum


class GetPinnedItemsResponse200ResultsItemType0Type(str, Enum):
    DASHBOARD = "dashboard"

    def __str__(self) -> str:
        return str(self.value)
