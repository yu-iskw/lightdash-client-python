from enum import Enum


class CustomDimensionTypeBIN(str, Enum):
    BIN = "bin"

    def __str__(self) -> str:
        return str(self.value)
