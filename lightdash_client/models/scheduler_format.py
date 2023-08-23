from enum import Enum


class SchedulerFormat(str, Enum):
    CSV = "csv"
    GSHEETS = "gsheets"
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
