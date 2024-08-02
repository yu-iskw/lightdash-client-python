from enum import Enum


class DbtModelJoinType(str, Enum):
    FULL = "full"
    INNER = "inner"
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
