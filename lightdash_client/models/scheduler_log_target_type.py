from enum import Enum


class SchedulerLogTargetType(str, Enum):
    EMAIL = "email"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
