from enum import Enum


class SchedulerBaseFormat(str, Enum):
    CSV = "csv"
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
