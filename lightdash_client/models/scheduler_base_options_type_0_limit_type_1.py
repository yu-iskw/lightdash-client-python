from enum import Enum


class SchedulerBaseOptionsType0LimitType1(str, Enum):
    ALL = "all"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
