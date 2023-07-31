from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickUserAttributeExcludeKeyofUserAttributeUuidOrCreatedAtOrOrganizationUuidOrUsers")


@attr.s(auto_attribs=True)
class PickUserAttributeExcludeKeyofUserAttributeUuidOrCreatedAtOrOrganizationUuidOrUsers:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        description (Union[Unset, str]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
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

        pick_user_attribute_exclude_keyof_user_attribute_uuid_or_created_at_or_organization_uuid_or_users = cls(
            name=name,
            description=description,
        )

        pick_user_attribute_exclude_keyof_user_attribute_uuid_or_created_at_or_organization_uuid_or_users.additional_properties = (
            d
        )
        return pick_user_attribute_exclude_keyof_user_attribute_uuid_or_created_at_or_organization_uuid_or_users

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
