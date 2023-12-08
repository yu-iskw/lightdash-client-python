from enum import Enum


class ResourceItemCategory(str, Enum):
    MOSTPOPULAR = "mostPopular"
    PINNED = "pinned"
    RECENTLYUPDATED = "recentlyUpdated"

    def __str__(self) -> str:
        return str(self.value)
