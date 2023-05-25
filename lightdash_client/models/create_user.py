from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="CreateUser")


@attr.s(auto_attribs=True)
class CreateUser:
    """
    Attributes:
        invite_code (str):
        first_name (str):
        last_name (str):
        email (str):
        password (str):
    """

    invite_code: str
    first_name: str
    last_name: str
    email: str
    password: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invite_code = self.invite_code
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inviteCode": invite_code,
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invite_code = d.pop("inviteCode")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        email = d.pop("email")

        password = d.pop("password")

        create_user = cls(
            invite_code=invite_code,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        create_user.additional_properties = d
        return create_user

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
