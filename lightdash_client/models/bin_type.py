from enum import Enum


class BinType(str, Enum):
    CUSTOM_RANGE = "custom_range"
    FIXED_NUMBER = "fixed_number"
    FIXED_WIDTH = "fixed_width"

    def __str__(self) -> str:
        return str(self.value)
