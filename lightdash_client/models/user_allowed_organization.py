from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="UserAllowedOrganization")


@attr.s(auto_attribs=True)
class UserAllowedOrganization:
    """
    Attributes:
        members_count (float):
        name (str):
        organization_uuid (str):
    """

    members_count: float
    name: str
    organization_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        members_count = self.members_count
        name = self.name
        organization_uuid = self.organization_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "membersCount": members_count,
                "name": name,
                "organizationUuid": organization_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        members_count = d.pop("membersCount")

        name = d.pop("name")

        organization_uuid = d.pop("organizationUuid")

        user_allowed_organization = cls(
            members_count=members_count,
            name=name,
            organization_uuid=organization_uuid,
        )

        user_allowed_organization.additional_properties = d
        return user_allowed_organization

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
