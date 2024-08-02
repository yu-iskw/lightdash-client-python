from enum import Enum


class ApiPromotionChangesResponseStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
