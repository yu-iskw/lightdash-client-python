from enum import Enum


class ApiUpdateProjectGroupAccessStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
