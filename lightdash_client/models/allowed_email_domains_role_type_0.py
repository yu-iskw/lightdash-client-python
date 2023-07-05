from enum import Enum


class AllowedEmailDomainsRoleType0(str, Enum):
    EDITOR = "editor"

    def __str__(self) -> str:
        return str(self.value)
