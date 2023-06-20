from enum import Enum


class PostRunUnderlyingDataQueryResponse200ResultsMetricQueryTableCalculationsItemFormatSeparator(str, Enum):
    COMMAPERIOD = "commaPeriod"
    NOSEPARATORPERIOD = "noSeparatorPeriod"
    PERIODCOMMA = "periodComma"
    SPACEPERIOD = "spacePeriod"

    def __str__(self) -> str:
        return str(self.value)
