from enum import Enum


class DbtGithubProjectConfigType(str, Enum):
    GITHUB = "github"

    def __str__(self) -> str:
        return str(self.value)
