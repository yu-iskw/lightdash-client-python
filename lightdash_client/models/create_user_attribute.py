from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_attribute_value import GroupAttributeValue
    from ..models.pick_user_attribute_value_exclude_keyof_user_attribute_value_email import (
        PickUserAttributeValueExcludeKeyofUserAttributeValueEmail,
    )


T = TypeVar("T", bound="CreateUserAttribute")


@_attrs_define
class CreateUserAttribute:
    """
    Attributes:
        name (str):
        attribute_default (Union[None, str]):
        groups (List['GroupAttributeValue']):
        users (List['PickUserAttributeValueExcludeKeyofUserAttributeValueEmail']):
        description (Union[Unset, str]):
    """

    name: str
    attribute_default: Union[None, str]
    groups: List["GroupAttributeValue"]
    users: List["PickUserAttributeValueExcludeKeyofUserAttributeValueEmail"]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        attribute_default: Union[None, str]
        attribute_default = self.attribute_default

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "attributeDefault": attribute_default,
                "groups": groups,
                "users": users,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_attribute_value import GroupAttributeValue
        from ..models.pick_user_attribute_value_exclude_keyof_user_attribute_value_email import (
            PickUserAttributeValueExcludeKeyofUserAttributeValueEmail,
        )

        d = src_dict.copy()
        name = d.pop("name")

        def _parse_attribute_default(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        attribute_default = _parse_attribute_default(d.pop("attributeDefault"))

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = GroupAttributeValue.from_dict(groups_item_data)

            groups.append(groups_item)

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = PickUserAttributeValueExcludeKeyofUserAttributeValueEmail.from_dict(users_item_data)

            users.append(users_item)

        description = d.pop("description", UNSET)

        create_user_attribute = cls(
            name=name,
            attribute_default=attribute_default,
            groups=groups,
            users=users,
            description=description,
        )

        create_user_attribute.additional_properties = d
        return create_user_attribute

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
