from enum import Enum


class GetSchedulerLogsResponse200ResultsLogsItemTargetType(str, Enum):
    EMAIL = "email"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
