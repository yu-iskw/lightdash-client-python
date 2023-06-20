from enum import Enum


class OmitCreateDatabricksCredentialsSensitiveCredentialsFieldNamesType(str, Enum):
    DATABRICKS = "databricks"

    def __str__(self) -> str:
        return str(self.value)
