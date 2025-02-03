from enum import Enum


class SpotlightTableColumns(str, Enum):
    CATEGORIES = "categories"
    CHARTUSAGE = "chartUsage"
    DESCRIPTION = "description"
    LABEL = "label"
    TABLELABEL = "tableLabel"

    def __str__(self) -> str:
        return str(self.value)
