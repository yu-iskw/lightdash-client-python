from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GroupMember")


@_attrs_define
class GroupMember:
    """A summary for a Lightdash user within a group

    Attributes:
        last_name (str): The user's last name
        first_name (str): The user's first name
        email (str): Primary email address for the user
        user_uuid (str): Unique id for the user
    """

    last_name: str
    first_name: str
    email: str
    user_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_name = self.last_name

        first_name = self.first_name

        email = self.email

        user_uuid = self.user_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastName": last_name,
                "firstName": first_name,
                "email": email,
                "userUuid": user_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        email = d.pop("email")

        user_uuid = d.pop("userUuid")

        group_member = cls(
            last_name=last_name,
            first_name=first_name,
            email=email,
            user_uuid=user_uuid,
        )

        group_member.additional_properties = d
        return group_member

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
