from enum import Enum


class Format(str, Enum):
    DKK = "dkk"
    EUR = "eur"
    GBP = "gbp"
    ID = "id"
    JPY = "jpy"
    KM = "km"
    MI = "mi"
    PERCENT = "percent"
    USD = "usd"

    def __str__(self) -> str:
        return str(self.value)
