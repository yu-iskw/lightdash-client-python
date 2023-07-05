from enum import Enum


class ApiOrganizationAllowedEmailDomainsResultsRoleType2(str, Enum):
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
