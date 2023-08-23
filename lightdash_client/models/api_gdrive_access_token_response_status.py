from enum import Enum


class ApiGdriveAccessTokenResponseStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
