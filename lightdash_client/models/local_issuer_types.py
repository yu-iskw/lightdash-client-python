from enum import Enum


class LocalIssuerTypes(str, Enum):
    APITOKEN = "apiToken"
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
