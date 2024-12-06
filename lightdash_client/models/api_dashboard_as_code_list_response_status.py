from enum import Enum


class ApiDashboardAsCodeListResponseStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
