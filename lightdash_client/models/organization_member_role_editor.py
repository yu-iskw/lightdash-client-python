from enum import Enum


class OrganizationMemberRoleEDITOR(str, Enum):
    EDITOR = "editor"

    def __str__(self) -> str:
        return str(self.value)
