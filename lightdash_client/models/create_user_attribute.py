from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_user_attribute_users_item import CreateUserAttributeUsersItem


T = TypeVar("T", bound="CreateUserAttribute")


@attr.s(auto_attribs=True)
class CreateUserAttribute:
    """
    Attributes:
        name (str):
        users (List['CreateUserAttributeUsersItem']):
        description (Union[Unset, str]):
    """

    name: str
    users: List["CreateUserAttributeUsersItem"]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
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
                "users": users,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_user_attribute_users_item import (
            CreateUserAttributeUsersItem,
        )

        d = src_dict.copy()
        name = d.pop("name")

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = CreateUserAttributeUsersItem.from_dict(users_item_data)

            users.append(users_item)

        description = d.pop("description", UNSET)

        create_user_attribute = cls(
            name=name,
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
