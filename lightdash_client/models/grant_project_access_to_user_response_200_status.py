from enum import Enum


class GrantProjectAccessToUserResponse200Status(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
