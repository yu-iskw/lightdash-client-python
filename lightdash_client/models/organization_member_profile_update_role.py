from enum import Enum


class OrganizationMemberProfileUpdateRole(str, Enum):
    ADMIN = "admin"
    DEVELOPER = "developer"
    EDITOR = "editor"
    INTERACTIVE_VIEWER = "interactive_viewer"
    MEMBER = "member"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
