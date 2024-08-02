from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateUserArgs")


@_attrs_define
class CreateUserArgs:
    """
    Attributes:
        password (str):
        email (str): Email
        last_name (str):
        first_name (str):
    """

    password: str
    email: str
    last_name: str
    first_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password

        email = self.email

        last_name = self.last_name

        first_name = self.first_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "email": email,
                "lastName": last_name,
                "firstName": first_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password")

        email = d.pop("email")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        create_user_args = cls(
            password=password,
            email=email,
            last_name=last_name,
            first_name=first_name,
        )

        create_user_args.additional_properties = d
        return create_user_args

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
