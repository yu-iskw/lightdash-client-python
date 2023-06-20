from enum import Enum


class PinnedItemsItemType0Type(str, Enum):
    DASHBOARD = "dashboard"

    def __str__(self) -> str:
        return str(self.value)
