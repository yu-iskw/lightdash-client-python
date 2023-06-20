from enum import Enum


class ApiPinnedItemsResultsItemType2Type(str, Enum):
    SPACE = "space"

    def __str__(self) -> str:
        return str(self.value)
