from enum import Enum


class ApiCreateUserAttributeResponseStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
