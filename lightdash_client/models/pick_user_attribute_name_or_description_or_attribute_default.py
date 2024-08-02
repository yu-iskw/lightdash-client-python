from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickUserAttributeNameOrDescriptionOrAttributeDefault")


@_attrs_define
class PickUserAttributeNameOrDescriptionOrAttributeDefault:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        attribute_default (Union[None, str]):
        description (Union[Unset, str]):
    """

    name: str
    attribute_default: Union[None, str]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        attribute_default: Union[None, str]
        attribute_default = self.attribute_default

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "attributeDefault": attribute_default,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        def _parse_attribute_default(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        attribute_default = _parse_attribute_default(d.pop("attributeDefault"))

        description = d.pop("description", UNSET)

        pick_user_attribute_name_or_description_or_attribute_default = cls(
            name=name,
            attribute_default=attribute_default,
            description=description,
        )

        pick_user_attribute_name_or_description_or_attribute_default.additional_properties = d
        return pick_user_attribute_name_or_description_or_attribute_default

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
