from enum import Enum


class ListGroupsInOrganizationResponse200Status(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
