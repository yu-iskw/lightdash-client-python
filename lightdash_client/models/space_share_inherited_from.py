from enum import Enum


class SpaceShareInheritedFrom(str, Enum):
    GROUP = "group"
    ORGANIZATION = "organization"
    PROJECT = "project"
    SPACE_GROUP = "space_group"

    def __str__(self) -> str:
        return str(self.value)
