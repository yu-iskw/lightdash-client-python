from enum import Enum


class BigqueryCredentialsType(str, Enum):
    BIGQUERY = "bigquery"

    def __str__(self) -> str:
        return str(self.value)
