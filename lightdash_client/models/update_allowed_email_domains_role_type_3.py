from enum import Enum


class UpdateAllowedEmailDomainsRoleType3(str, Enum):
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
