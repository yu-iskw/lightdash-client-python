from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.space_member_role import SpaceMemberRole

T = TypeVar("T", bound="AddSpaceGroupAccess")


@_attrs_define
class AddSpaceGroupAccess:
    """
    Attributes:
        space_role (SpaceMemberRole):
        group_uuid (str):
    """

    space_role: SpaceMemberRole
    group_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        space_role = self.space_role.value

        group_uuid = self.group_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spaceRole": space_role,
                "groupUuid": group_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        space_role = SpaceMemberRole(d.pop("spaceRole"))

        group_uuid = d.pop("groupUuid")

        add_space_group_access = cls(
            space_role=space_role,
            group_uuid=group_uuid,
        )

        add_space_group_access.additional_properties = d
        return add_space_group_access

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
