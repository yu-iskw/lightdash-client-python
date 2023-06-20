from enum import Enum


class OmitCreatePostgresCredentialsSensitiveCredentialsFieldNamesType(str, Enum):
    POSTGRES = "postgres"

    def __str__(self) -> str:
        return str(self.value)
