from enum import Enum


class SchedulerType0Format(str, Enum):
    CSV = "csv"
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
