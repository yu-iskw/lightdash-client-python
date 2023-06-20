from enum import Enum


class DbtNoneProjectConfigType(str, Enum):
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
