from enum import Enum


class GetProjectResponse200ResultsDbtConnectionType2Type(str, Enum):
    GITHUB = "github"

    def __str__(self) -> str:
        return str(self.value)
