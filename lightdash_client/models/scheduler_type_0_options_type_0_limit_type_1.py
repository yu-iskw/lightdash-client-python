from enum import Enum


class SchedulerType0OptionsType0LimitType1(str, Enum):
    ALL = "all"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
