from enum import Enum


class RedshiftCredentialsType(str, Enum):
    REDSHIFT = "redshift"

    def __str__(self) -> str:
        return str(self.value)
