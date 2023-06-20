from enum import Enum


class DeleteSpaceResponse204Status(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
