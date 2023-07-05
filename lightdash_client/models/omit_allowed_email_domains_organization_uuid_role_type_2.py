from enum import Enum


class OmitAllowedEmailDomainsOrganizationUuidRoleType2(str, Enum):
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
