from enum import Enum


class DateGranularity(str, Enum):
    DAY = "Day"
    MONTH = "Month"
    QUARTER = "Quarter"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
