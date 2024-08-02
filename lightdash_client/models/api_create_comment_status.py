from enum import Enum


class ApiCreateCommentStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
