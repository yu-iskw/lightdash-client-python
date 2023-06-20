from enum import Enum


class UpdateProjectAccessForUserJsonBodyRole(str, Enum):
    ADMIN = "admin"
    DEVELOPER = "developer"
    EDITOR = "editor"
    INTERACTIVE_VIEWER = "interactive_viewer"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
