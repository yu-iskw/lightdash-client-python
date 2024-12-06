from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.space_member_role import SpaceMemberRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpaceGroup")


@_attrs_define
class SpaceGroup:
    """
    Attributes:
        space_role (SpaceMemberRole):
        group_name (str):
        group_uuid (str):
    """

    space_role: SpaceMemberRole
    group_name: str
    group_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        space_role = self.space_role.value

        group_name = self.group_name

        group_uuid = self.group_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spaceRole": space_role,
                "groupName": group_name,
                "groupUuid": group_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        space_role = SpaceMemberRole(d.pop("spaceRole"))

        group_name = d.pop("groupName")

        group_uuid = d.pop("groupUuid")

        space_group = cls(
            space_role=space_role,
            group_name=group_name,
            group_uuid=group_uuid,
        )

        space_group.additional_properties = d
        return space_group

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
