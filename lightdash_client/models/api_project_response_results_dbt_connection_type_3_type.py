from enum import Enum


class ApiProjectResponseResultsDbtConnectionType3Type(str, Enum):
    BITBUCKET = "bitbucket"

    def __str__(self) -> str:
        return str(self.value)
