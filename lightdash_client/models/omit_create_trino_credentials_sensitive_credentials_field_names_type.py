from enum import Enum


class OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesType(str, Enum):
    TRINO = "trino"

    def __str__(self) -> str:
        return str(self.value)
