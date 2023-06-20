from enum import Enum


class SnowflakeCredentialsType(str, Enum):
    SNOWFLAKE = "snowflake"

    def __str__(self) -> str:
        return str(self.value)
