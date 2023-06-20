from enum import Enum


class TrinoCredentialsType(str, Enum):
    TRINO = "trino"

    def __str__(self) -> str:
        return str(self.value)
