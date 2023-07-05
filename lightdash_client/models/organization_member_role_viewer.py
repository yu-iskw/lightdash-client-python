from enum import Enum


class OrganizationMemberRoleVIEWER(str, Enum):
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
