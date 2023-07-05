from enum import Enum


class ListOrganizationEmailDomainsResponse200ResultsRoleType3(str, Enum):
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
