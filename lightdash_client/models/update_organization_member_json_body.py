from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.update_organization_member_json_body_role import (
    UpdateOrganizationMemberJsonBodyRole,
)

T = TypeVar("T", bound="UpdateOrganizationMemberJsonBody")


@attr.s(auto_attribs=True)
class UpdateOrganizationMemberJsonBody:
    """the new membership profile

    Attributes:
        role (UpdateOrganizationMemberJsonBodyRole):
    """

    role: UpdateOrganizationMemberJsonBodyRole
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
        role = UpdateOrganizationMemberJsonBodyRole(d.pop("role"))

        update_organization_member_json_body = cls(
            role=role,
        )

        update_organization_member_json_body.additional_properties = d
        return update_organization_member_json_body

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
