from enum import Enum


class ApiChartAsCodeUpsertResponseStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
