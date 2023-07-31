from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateUserAttributeValue")


@attr.s(auto_attribs=True)
class CreateUserAttributeValue:
    """Construct a type with the properties of T except for those in type K.

    Attributes:
        user_uuid (str):
        value (str):
    """

    user_uuid: str
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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

        create_user_attribute_value = cls(
            user_uuid=user_uuid,
            value=value,
        )

        create_user_attribute_value.additional_properties = d
        return create_user_attribute_value

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
