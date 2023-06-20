from enum import Enum


class ResourceViewSpaceItemType(str, Enum):
    SPACE = "space"

    def __str__(self) -> str:
        return str(self.value)
