from enum import Enum


class DeleteSchedulerResponse201Status(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
