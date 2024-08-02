from enum import Enum


class ChartTypeFUNNEL(str, Enum):
    FUNNEL = "funnel"

    def __str__(self) -> str:
        return str(self.value)
