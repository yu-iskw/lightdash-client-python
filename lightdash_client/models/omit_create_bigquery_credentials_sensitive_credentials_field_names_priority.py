from enum import Enum


class OmitCreateBigqueryCredentialsSensitiveCredentialsFieldNamesPriority(str, Enum):
    BATCH = "batch"
    INTERACTIVE = "interactive"

    def __str__(self) -> str:
        return str(self.value)
