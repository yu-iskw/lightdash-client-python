from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_organization_projects_results_item_type import (
    ApiOrganizationProjectsResultsItemType,
)

T = TypeVar("T", bound="ApiOrganizationProjectsResultsItem")


@attr.s(auto_attribs=True)
class ApiOrganizationProjectsResultsItem:
    """Summary of a project under an organization

    Attributes:
        type (ApiOrganizationProjectsResultsItemType):
        name (str):
        project_uuid (str): The unique identifier of the project
    """

    type: ApiOrganizationProjectsResultsItemType
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
        type = ApiOrganizationProjectsResultsItemType(d.pop("type"))

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        api_organization_projects_results_item = cls(
            type=type,
            name=name,
            project_uuid=project_uuid,
        )

        api_organization_projects_results_item.additional_properties = d
        return api_organization_projects_results_item

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
