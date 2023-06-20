from enum import Enum


class OmitCreateBigqueryCredentialsSensitiveCredentialsFieldNamesType(str, Enum):
    BIGQUERY = "bigquery"

    def __str__(self) -> str:
        return str(self.value)
