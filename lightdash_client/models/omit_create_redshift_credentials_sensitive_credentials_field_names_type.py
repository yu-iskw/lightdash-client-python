from enum import Enum


class OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesType(str, Enum):
    REDSHIFT = "redshift"

    def __str__(self) -> str:
        return str(self.value)
