from enum import Enum


class MetricQueryResponseTableCalculationsItemFormatSeparator(str, Enum):
    COMMAPERIOD = "commaPeriod"
    DEFAULT = "default"
    NOSEPARATORPERIOD = "noSeparatorPeriod"
    PERIODCOMMA = "periodComma"
    SPACEPERIOD = "spacePeriod"

    def __str__(self) -> str:
        return str(self.value)
