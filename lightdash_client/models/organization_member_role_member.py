from enum import Enum


class OrganizationMemberRoleMEMBER(str, Enum):
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
