from enum import Enum


class ApiSchedulerLogsResponseResultsLogsItemTargetType(str, Enum):
    EMAIL = "email"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
