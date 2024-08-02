from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.space_member_role import SpaceMemberRole

T = TypeVar("T", bound="PickSpaceShareUserUuidOrRole")


@_attrs_define
class PickSpaceShareUserUuidOrRole:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        user_uuid (str):
        role (SpaceMemberRole):
    """

    user_uuid: str
    role: SpaceMemberRole
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_uuid = self.user_uuid

        role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_uuid = d.pop("userUuid")

        role = SpaceMemberRole(d.pop("role"))

        pick_space_share_user_uuid_or_role = cls(
            user_uuid=user_uuid,
            role=role,
        )

        pick_space_share_user_uuid_or_role.additional_properties = d
        return pick_space_share_user_uuid_or_role

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
