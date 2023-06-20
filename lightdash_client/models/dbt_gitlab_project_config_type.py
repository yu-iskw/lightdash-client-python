from enum import Enum


class DbtGitlabProjectConfigType(str, Enum):
    GITLAB = "gitlab"

    def __str__(self) -> str:
        return str(self.value)
