from enum import Enum


class ValidationErrorType(str, Enum):
    CHART = "chart"
    CUSTOM_METRIC = "custom metric"
    DIMENSION = "dimension"
    FILTER = "filter"
    METRIC = "metric"
    MODEL = "model"
    SORTING = "sorting"

    def __str__(self) -> str:
        return str(self.value)
