from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.update_project_member_role import UpdateProjectMemberRole

T = TypeVar("T", bound="UpdateProjectMember")


@attr.s(auto_attribs=True)
class UpdateProjectMember:
    """
    Attributes:
        role (UpdateProjectMemberRole):
    """

    role: UpdateProjectMemberRole
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = UpdateProjectMemberRole(d.pop("role"))

        update_project_member = cls(
            role=role,
        )

        update_project_member.additional_properties = d
        return update_project_member

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
