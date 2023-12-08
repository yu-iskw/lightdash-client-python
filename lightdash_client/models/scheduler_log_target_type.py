from enum import Enum


class SchedulerLogTargetType(str, Enum):
    EMAIL = "email"
    GSHEETS = "gsheets"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
