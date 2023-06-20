from enum import Enum


class PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesType(
    str, Enum
):
    DATABRICKS = "databricks"

    def __str__(self) -> str:
        return str(self.value)
