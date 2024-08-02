from enum import Enum


class ChartTypeBIGNUMBER(str, Enum):
    BIG_NUMBER = "big_number"

    def __str__(self) -> str:
        return str(self.value)
