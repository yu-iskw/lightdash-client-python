from enum import Enum


class PostgresCredentialsType(str, Enum):
    POSTGRES = "postgres"

    def __str__(self) -> str:
        return str(self.value)
