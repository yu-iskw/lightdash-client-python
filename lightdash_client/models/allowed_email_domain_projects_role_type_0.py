from enum import Enum


class AllowedEmailDomainProjectsRoleType0(str, Enum):
    EDITOR = "editor"

    def __str__(self) -> str:
        return str(self.value)
