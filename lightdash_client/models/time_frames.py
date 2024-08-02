from enum import Enum


class TimeFrames(str, Enum):
    DAY = "DAY"
    DAY_OF_MONTH_NUM = "DAY_OF_MONTH_NUM"
    DAY_OF_WEEK_INDEX = "DAY_OF_WEEK_INDEX"
    DAY_OF_WEEK_NAME = "DAY_OF_WEEK_NAME"
    DAY_OF_YEAR_NUM = "DAY_OF_YEAR_NUM"
    HOUR = "HOUR"
    HOUR_OF_DAY_NUM = "HOUR_OF_DAY_NUM"
    MILLISECOND = "MILLISECOND"
    MINUTE = "MINUTE"
    MINUTE_OF_HOUR_NUM = "MINUTE_OF_HOUR_NUM"
    MONTH = "MONTH"
    MONTH_NAME = "MONTH_NAME"
    MONTH_NUM = "MONTH_NUM"
    QUARTER = "QUARTER"
    QUARTER_NAME = "QUARTER_NAME"
    QUARTER_NUM = "QUARTER_NUM"
    RAW = "RAW"
    SECOND = "SECOND"
    WEEK = "WEEK"
    WEEK_NUM = "WEEK_NUM"
    YEAR = "YEAR"
    YEAR_NUM = "YEAR_NUM"

    def __str__(self) -> str:
        return str(self.value)
