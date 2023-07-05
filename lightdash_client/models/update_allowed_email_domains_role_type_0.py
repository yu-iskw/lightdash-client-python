from enum import Enum


class UpdateAllowedEmailDomainsRoleType0(str, Enum):
    EDITOR = "editor"

    def __str__(self) -> str:
        return str(self.value)
