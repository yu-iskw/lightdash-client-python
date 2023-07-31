import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_user_attributes_response_200_results_item_users_item import (
        GetUserAttributesResponse200ResultsItemUsersItem,
    )


T = TypeVar("T", bound="GetUserAttributesResponse200ResultsItem")


@attr.s(auto_attribs=True)
class GetUserAttributesResponse200ResultsItem:
    """
    Attributes:
        users (List['GetUserAttributesResponse200ResultsItemUsersItem']):
        organization_uuid (str):
        name (str):
        created_at (datetime.datetime):
        uuid (str):
        description (Union[Unset, str]):
    """

    users: List["GetUserAttributesResponse200ResultsItemUsersItem"]
    organization_uuid: str
    name: str
    created_at: datetime.datetime
    uuid: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()

            users.append(users_item)

        organization_uuid = self.organization_uuid
        name = self.name
        created_at = self.created_at.isoformat()

        uuid = self.uuid
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
                "organizationUuid": organization_uuid,
                "name": name,
                "createdAt": created_at,
                "uuid": uuid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_user_attributes_response_200_results_item_users_item import (
            GetUserAttributesResponse200ResultsItemUsersItem,
        )

        d = src_dict.copy()
        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = GetUserAttributesResponse200ResultsItemUsersItem.from_dict(users_item_data)

            users.append(users_item)

        organization_uuid = d.pop("organizationUuid")

        name = d.pop("name")

        created_at = isoparse(d.pop("createdAt"))

        uuid = d.pop("uuid")

        description = d.pop("description", UNSET)

        get_user_attributes_response_200_results_item = cls(
            users=users,
            organization_uuid=organization_uuid,
            name=name,
            created_at=created_at,
            uuid=uuid,
            description=description,
        )

        get_user_attributes_response_200_results_item.additional_properties = d
        return get_user_attributes_response_200_results_item

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
