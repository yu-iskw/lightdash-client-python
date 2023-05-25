from enum import Enum


class JobJobStatus(str, Enum):
    DONE = "DONE"
    ERROR = "ERROR"
    RUNNING = "RUNNING"
    STARTED = "STARTED"

    def __str__(self) -> str:
        return str(self.value)
