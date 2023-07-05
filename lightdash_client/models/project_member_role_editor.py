from enum import Enum


class ProjectMemberRoleEDITOR(str, Enum):
    EDITOR = "editor"

    def __str__(self) -> str:
        return str(self.value)
