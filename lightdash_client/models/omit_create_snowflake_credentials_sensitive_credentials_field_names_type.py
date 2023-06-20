from enum import Enum


class OmitCreateSnowflakeCredentialsSensitiveCredentialsFieldNamesType(str, Enum):
    SNOWFLAKE = "snowflake"

    def __str__(self) -> str:
        return str(self.value)
