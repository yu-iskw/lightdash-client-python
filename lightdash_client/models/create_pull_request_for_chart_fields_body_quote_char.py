from enum import Enum


class CreatePullRequestForChartFieldsBodyQuoteChar(str, Enum):
    VALUE_0 = '"'
    VALUE_1 = "'"

    def __str__(self) -> str:
        return str(self.value)
