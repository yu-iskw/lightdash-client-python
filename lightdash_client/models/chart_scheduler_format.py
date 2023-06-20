from enum import Enum


class ChartSchedulerFormat(str, Enum):
    CSV = "csv"
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
