from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_member_role import ProjectMemberRole

T = TypeVar("T", bound="PickDBProjectGroupAccessRole")


@_attrs_define
class PickDBProjectGroupAccessRole:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        role (ProjectMemberRole):
    """

    role: ProjectMemberRole
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        role = ProjectMemberRole(d.pop("role"))

        pick_db_project_group_access_role = cls(
            role=role,
        )

        pick_db_project_group_access_role.additional_properties = d
        return pick_db_project_group_access_role

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
