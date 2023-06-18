from enum import Enum


class DbtProjectTypeGITHUB(str, Enum):
    GITHUB = "github"

    def __str__(self) -> str:
        return str(self.value)
