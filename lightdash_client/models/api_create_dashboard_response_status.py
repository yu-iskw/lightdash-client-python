from enum import Enum


class ApiCreateDashboardResponseStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
