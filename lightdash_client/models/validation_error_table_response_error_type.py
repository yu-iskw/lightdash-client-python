from enum import Enum


class ValidationErrorTableResponseErrorType(str, Enum):
    CHART = "chart"
    DIMENSION = "dimension"
    FILTER = "filter"
    METRIC = "metric"
    MODEL = "model"
    SORTING = "sorting"

    def __str__(self) -> str:
        return str(self.value)
