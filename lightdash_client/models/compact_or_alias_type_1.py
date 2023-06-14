from enum import Enum


class CompactOrAliasType1(str, Enum):
    B = "B"
    BILLION = "billion"
    K = "K"
    M = "M"
    MILLION = "million"
    T = "T"
    THOUSAND = "thousand"
    TRILLION = "trillion"

    def __str__(self) -> str:
        return str(self.value)
