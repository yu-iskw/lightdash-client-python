from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PickGroupMemberUserUuid")


@_attrs_define
class PickGroupMemberUserUuid:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        user_uuid (str): Unique id for the user
    """

    user_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_uuid = self.user_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_uuid = d.pop("userUuid")

        pick_group_member_user_uuid = cls(
            user_uuid=user_uuid,
        )

        pick_group_member_user_uuid.additional_properties = d
        return pick_group_member_user_uuid

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
