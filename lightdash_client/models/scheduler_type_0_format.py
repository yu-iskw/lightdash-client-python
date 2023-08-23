from enum import Enum


class SchedulerType0Format(str, Enum):
    CSV = "csv"
    GSHEETS = "gsheets"
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
