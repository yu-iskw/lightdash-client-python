from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PickUserAttributeValueExcludeKeyofUserAttributeValueEmail")


@_attrs_define
class PickUserAttributeValueExcludeKeyofUserAttributeValueEmail:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        user_uuid (str):
        value (str):
    """

    user_uuid: str
    value: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_uuid = self.user_uuid

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_uuid = d.pop("userUuid")

        value = d.pop("value")

        pick_user_attribute_value_exclude_keyof_user_attribute_value_email = cls(
            user_uuid=user_uuid,
            value=value,
        )

        pick_user_attribute_value_exclude_keyof_user_attribute_value_email.additional_properties = d
        return pick_user_attribute_value_exclude_keyof_user_attribute_value_email

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
