from enum import Enum


class CreatePullRequestForChartFieldsResponse200Status(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
