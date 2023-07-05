from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.list_organization_projects_response_200_results_item_type import (
    ListOrganizationProjectsResponse200ResultsItemType,
)

T = TypeVar("T", bound="ListOrganizationProjectsResponse200ResultsItem")


@attr.s(auto_attribs=True)
class ListOrganizationProjectsResponse200ResultsItem:
    """Summary of a project under an organization

    Attributes:
        type (ListOrganizationProjectsResponse200ResultsItemType):
        name (str):
        project_uuid (str): The unique identifier of the project
    """

    type: ListOrganizationProjectsResponse200ResultsItemType
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
        type = ListOrganizationProjectsResponse200ResultsItemType(d.pop("type"))

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        list_organization_projects_response_200_results_item = cls(
            type=type,
            name=name,
            project_uuid=project_uuid,
        )

        list_organization_projects_response_200_results_item.additional_properties = d
        return list_organization_projects_response_200_results_item

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
