from enum import Enum


class ProjectDbtConnectionType2Type(str, Enum):
    GITHUB = "github"

    def __str__(self) -> str:
        return str(self.value)
