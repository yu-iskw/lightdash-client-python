from enum import Enum


class MetricType(str, Enum):
    AVERAGE = "average"
    BOOLEAN = "boolean"
    COUNT = "count"
    COUNT_DISTINCT = "count_distinct"
    DATE = "date"
    MAX = "max"
    MEDIAN = "median"
    MIN = "min"
    NUMBER = "number"
    PERCENTILE = "percentile"
    STRING = "string"
    SUM = "sum"
    TIMESTAMP = "timestamp"

    def __str__(self) -> str:
        return str(self.value)
