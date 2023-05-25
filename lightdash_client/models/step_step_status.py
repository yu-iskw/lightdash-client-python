from enum import Enum


class StepStepStatus(str, Enum):
    DONE = "DONE"
    ERROR = "ERROR"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SKIPPED = "SKIPPED"

    def __str__(self) -> str:
        return str(self.value)
