from enum import Enum


class AllowedEmailDomainProjectsRoleType2(str, Enum):
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
