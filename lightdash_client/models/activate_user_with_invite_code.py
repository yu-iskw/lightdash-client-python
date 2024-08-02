from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActivateUserWithInviteCode")


@_attrs_define
class ActivateUserWithInviteCode:
    """
    Attributes:
        password (str):
        last_name (str):
        first_name (str):
        invite_code (str):
    """

    password: str
    last_name: str
    first_name: str
    invite_code: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password

        last_name = self.last_name

        first_name = self.first_name

        invite_code = self.invite_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "lastName": last_name,
                "firstName": first_name,
                "inviteCode": invite_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        invite_code = d.pop("inviteCode")

        activate_user_with_invite_code = cls(
            password=password,
            last_name=last_name,
            first_name=first_name,
            invite_code=invite_code,
        )

        activate_user_with_invite_code.additional_properties = d
        return activate_user_with_invite_code

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
