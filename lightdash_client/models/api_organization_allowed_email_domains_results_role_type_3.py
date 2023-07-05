from enum import Enum


class ApiOrganizationAllowedEmailDomainsResultsRoleType3(str, Enum):
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
