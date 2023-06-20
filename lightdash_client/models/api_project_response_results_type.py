from enum import Enum


class ApiProjectResponseResultsType(str, Enum):
    DEFAULT = "DEFAULT"
    PREVIEW = "PREVIEW"

    def __str__(self) -> str:
        return str(self.value)
