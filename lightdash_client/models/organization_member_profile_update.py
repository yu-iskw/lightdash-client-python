from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.organization_member_profile_update_role import (
    OrganizationMemberProfileUpdateRole,
)

T = TypeVar("T", bound="OrganizationMemberProfileUpdate")


@attr.s(auto_attribs=True)
class OrganizationMemberProfileUpdate:
    """
    Attributes:
        role (OrganizationMemberProfileUpdateRole):
    """

    role: OrganizationMemberProfileUpdateRole
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = OrganizationMemberProfileUpdateRole(d.pop("role"))

        organization_member_profile_update = cls(
            role=role,
        )

        organization_member_profile_update.additional_properties = d
        return organization_member_profile_update

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
