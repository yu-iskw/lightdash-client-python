from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickUserAttributeNameOrDescriptionOrAttributeDefault")


@attr.s(auto_attribs=True)
class PickUserAttributeNameOrDescriptionOrAttributeDefault:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        description (Union[Unset, str]):
        attribute_default (Optional[str]):
    """

    name: str
    attribute_default: Optional[str]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        attribute_default = self.attribute_default

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

        description = d.pop("description", UNSET)

        attribute_default = d.pop("attributeDefault")

        pick_user_attribute_name_or_description_or_attribute_default = cls(
            name=name,
            description=description,
            attribute_default=attribute_default,
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
