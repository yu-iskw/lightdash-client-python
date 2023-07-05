from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.grant_project_access_to_user_json_body_role import (
    GrantProjectAccessToUserJsonBodyRole,
)

T = TypeVar("T", bound="GrantProjectAccessToUserJsonBody")


@attr.s(auto_attribs=True)
class GrantProjectAccessToUserJsonBody:
    """
    Attributes:
        send_email (bool):
        role (GrantProjectAccessToUserJsonBodyRole):
        email (str):
    """

    send_email: bool
    role: GrantProjectAccessToUserJsonBodyRole
    email: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        send_email = self.send_email
        role = self.role.value

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sendEmail": send_email,
                "role": role,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        send_email = d.pop("sendEmail")

        role = GrantProjectAccessToUserJsonBodyRole(d.pop("role"))

        email = d.pop("email")

        grant_project_access_to_user_json_body = cls(
            send_email=send_email,
            role=role,
            email=email,
        )

        grant_project_access_to_user_json_body.additional_properties = d
        return grant_project_access_to_user_json_body

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
