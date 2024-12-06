from enum import Enum


class ExploreType(str, Enum):
    DEFAULT = "default"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
