from enum import Enum


class ApiProjectResponseResultsDbtConnectionType4Type(str, Enum):
    GITLAB = "gitlab"

    def __str__(self) -> str:
        return str(self.value)
