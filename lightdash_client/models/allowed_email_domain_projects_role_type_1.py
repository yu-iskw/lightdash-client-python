from enum import Enum


class AllowedEmailDomainProjectsRoleType1(str, Enum):
    INTERACTIVE_VIEWER = "interactive_viewer"

    def __str__(self) -> str:
        return str(self.value)
