from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PickLightdashUserUserUuidOrFirstNameOrLastName")


@_attrs_define
class PickLightdashUserUserUuidOrFirstNameOrLastName:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        user_uuid (str):
        first_name (str):
        last_name (str):
    """

    user_uuid: str
    first_name: str
    last_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_uuid = self.user_uuid

        first_name = self.first_name

        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
                "firstName": first_name,
                "lastName": last_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_uuid = d.pop("userUuid")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        pick_lightdash_user_user_uuid_or_first_name_or_last_name = cls(
            user_uuid=user_uuid,
            first_name=first_name,
            last_name=last_name,
        )

        pick_lightdash_user_user_uuid_or_first_name_or_last_name.additional_properties = d
        return pick_lightdash_user_user_uuid_or_first_name_or_last_name

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
