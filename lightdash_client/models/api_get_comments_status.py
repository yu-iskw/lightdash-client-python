from enum import Enum


class ApiGetCommentsStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
