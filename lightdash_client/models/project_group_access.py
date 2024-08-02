from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_member_role import ProjectMemberRole

T = TypeVar("T", bound="ProjectGroupAccess")


@_attrs_define
class ProjectGroupAccess:
    """
    Attributes:
        role (ProjectMemberRole):
        group_uuid (str):
        project_uuid (str):
    """

    role: ProjectMemberRole
    group_uuid: str
    project_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        group_uuid = self.group_uuid

        project_uuid = self.project_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "groupUuid": group_uuid,
                "projectUuid": project_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = ProjectMemberRole(d.pop("role"))

        group_uuid = d.pop("groupUuid")

        project_uuid = d.pop("projectUuid")

        project_group_access = cls(
            role=role,
            group_uuid=group_uuid,
            project_uuid=project_uuid,
        )

        project_group_access.additional_properties = d
        return project_group_access

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
