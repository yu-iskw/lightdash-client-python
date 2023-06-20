from enum import Enum


class ApiPinnedItemsResultsItemType1Type(str, Enum):
    CHART = "chart"

    def __str__(self) -> str:
        return str(self.value)
