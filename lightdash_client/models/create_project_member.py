from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

from ..models.project_member_role import ProjectMemberRole

T = TypeVar("T", bound="CreateProjectMember")


@attr.s(auto_attribs=True)
class CreateProjectMember:
    """
    Attributes:
        send_email (bool):
        role (ProjectMemberRole):
        email (str):
    """

    send_email: bool
    role: ProjectMemberRole
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

        role = ProjectMemberRole(d.pop("role"))

        email = d.pop("email")

        create_project_member = cls(
            send_email=send_email,
            role=role,
            email=email,
        )

        create_project_member.additional_properties = d
        return create_project_member

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
