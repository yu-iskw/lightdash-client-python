from enum import Enum


class SpaceMemberRole(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
