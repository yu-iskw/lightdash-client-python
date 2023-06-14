from enum import Enum


class SchedulerCsvOptionsLimitType1(str, Enum):
    ALL = "all"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
