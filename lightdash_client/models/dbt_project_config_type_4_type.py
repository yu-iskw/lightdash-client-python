from enum import Enum


class DbtProjectConfigType4Type(str, Enum):
    GITLAB = "gitlab"

    def __str__(self) -> str:
        return str(self.value)
