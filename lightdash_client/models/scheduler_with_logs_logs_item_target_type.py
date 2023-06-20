from enum import Enum


class SchedulerWithLogsLogsItemTargetType(str, Enum):
    EMAIL = "email"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
