from enum import Enum


class UpdateOrganizationEmailDomainsJsonBodyRoleType3(str, Enum):
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
