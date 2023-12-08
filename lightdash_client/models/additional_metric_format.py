from enum import Enum


class AdditionalMetricFormat(str, Enum):
    EUR = "eur"
    GBP = "gbp"
    ID = "id"
    KM = "km"
    MI = "mi"
    PERCENT = "percent"
    USD = "usd"

    def __str__(self) -> str:
        return str(self.value)