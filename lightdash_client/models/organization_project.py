from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

from ..models.project_type import ProjectType

T = TypeVar("T", bound="OrganizationProject")


@attr.s(auto_attribs=True)
class OrganizationProject:
    """Summary of a project under an organization

    Attributes:
        type (ProjectType):
        name (str):
        project_uuid (str): The unique identifier of the project
    """

    type: ProjectType
    name: str
    project_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        name = self.name
        project_uuid = self.project_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
                "projectUuid": project_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ProjectType(d.pop("type"))

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        organization_project = cls(
            type=type,
            name=name,
            project_uuid=project_uuid,
        )

        organization_project.additional_properties = d
        return organization_project

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
