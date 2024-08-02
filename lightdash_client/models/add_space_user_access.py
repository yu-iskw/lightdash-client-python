from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.space_member_role import SpaceMemberRole

T = TypeVar("T", bound="AddSpaceUserAccess")


@_attrs_define
class AddSpaceUserAccess:
    """
    Attributes:
        space_role (SpaceMemberRole):
        user_uuid (str):
    """

    space_role: SpaceMemberRole
    user_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        space_role = self.space_role.value

        user_uuid = self.user_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spaceRole": space_role,
                "userUuid": user_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        space_role = SpaceMemberRole(d.pop("spaceRole"))

        user_uuid = d.pop("userUuid")

        add_space_user_access = cls(
            space_role=space_role,
            user_uuid=user_uuid,
        )

        add_space_user_access.additional_properties = d
        return add_space_user_access

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
