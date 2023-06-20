from enum import Enum


class DbtProjectConfigType6Type(str, Enum):
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
