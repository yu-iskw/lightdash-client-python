from enum import Enum


class ThresholdOperator(str, Enum):
    DECREASEDBY = "decreasedBy"
    GREATERTHAN = "greaterThan"
    INCREASEDBY = "increasedBy"
    LESSTHAN = "lessThan"

    def __str__(self) -> str:
        return str(self.value)
