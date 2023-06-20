from enum import Enum


class GetProjectResponse200ResultsDbtConnectionType4Type(str, Enum):
    GITLAB = "gitlab"

    def __str__(self) -> str:
        return str(self.value)
