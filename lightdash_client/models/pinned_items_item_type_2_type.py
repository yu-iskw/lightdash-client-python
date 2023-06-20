from enum import Enum


class PinnedItemsItemType2Type(str, Enum):
    SPACE = "space"

    def __str__(self) -> str:
        return str(self.value)
