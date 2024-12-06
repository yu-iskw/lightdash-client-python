from enum import Enum


class FieldTypeDIMENSION(str, Enum):
    DIMENSION = "dimension"

    def __str__(self) -> str:
        return str(self.value)
