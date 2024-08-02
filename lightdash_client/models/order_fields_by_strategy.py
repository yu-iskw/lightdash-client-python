from enum import Enum


class OrderFieldsByStrategy(str, Enum):
    INDEX = "INDEX"
    LABEL = "LABEL"

    def __str__(self) -> str:
        return str(self.value)
