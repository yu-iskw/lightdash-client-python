from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..models.organization_member_profile_update_role import OrganizationMemberProfileUpdateRole
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="OrganizationMemberProfileUpdate")


@attr.s(auto_attribs=True)
class OrganizationMemberProfileUpdate:
    """Make all properties in T optional

    Attributes:
        role (Union[Unset, OrganizationMemberProfileUpdateRole]): The role of the user in the organization
    """

    role: Union[Unset, OrganizationMemberProfileUpdateRole] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _role = d.pop("role", UNSET)
        role: Union[Unset, OrganizationMemberProfileUpdateRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = OrganizationMemberProfileUpdateRole(_role)

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
