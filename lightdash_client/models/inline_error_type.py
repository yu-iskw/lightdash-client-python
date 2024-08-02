from enum import Enum


class InlineErrorType(str, Enum):
    METADATA_PARSE_ERROR = "METADATA_PARSE_ERROR"
    NO_DIMENSIONS_FOUND = "NO_DIMENSIONS_FOUND"

    def __str__(self) -> str:
        return str(self.value)
