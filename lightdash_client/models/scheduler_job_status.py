from enum import Enum


class SchedulerJobStatus(str, Enum):
    COMPLETED = "completed"
    ERROR = "error"
    SCHEDULED = "scheduled"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
