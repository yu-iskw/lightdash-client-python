from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.list_charts_in_project_response_200_results_item_chart_type import (
    ListChartsInProjectResponse200ResultsItemChartType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListChartsInProjectResponse200ResultsItem")


@attr.s(auto_attribs=True)
class ListChartsInProjectResponse200ResultsItem:
    """
    Attributes:
        name (str):
        organization_uuid (str):
        uuid (str):
        project_uuid (str):
        space_uuid (str):
        space_name (str):
        description (Union[Unset, str]):
        pinned_list_uuid (Optional[str]):
        chart_type (Union[Unset, ListChartsInProjectResponse200ResultsItemChartType]):
    """

    name: str
    organization_uuid: str
    uuid: str
    project_uuid: str
    space_uuid: str
    space_name: str
    pinned_list_uuid: Optional[str]
    description: Union[Unset, str] = UNSET
    chart_type: Union[Unset, ListChartsInProjectResponse200ResultsItemChartType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        organization_uuid = self.organization_uuid
        uuid = self.uuid
        project_uuid = self.project_uuid
        space_uuid = self.space_uuid
        space_name = self.space_name
        description = self.description
        pinned_list_uuid = self.pinned_list_uuid
        chart_type: Union[Unset, str] = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "organizationUuid": organization_uuid,
                "uuid": uuid,
                "projectUuid": project_uuid,
                "spaceUuid": space_uuid,
                "spaceName": space_name,
                "pinnedListUuid": pinned_list_uuid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if chart_type is not UNSET:
            field_dict["chartType"] = chart_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization_uuid = d.pop("organizationUuid")

        uuid = d.pop("uuid")

        project_uuid = d.pop("projectUuid")

        space_uuid = d.pop("spaceUuid")

        space_name = d.pop("spaceName")

        description = d.pop("description", UNSET)

        pinned_list_uuid = d.pop("pinnedListUuid")

        _chart_type = d.pop("chartType", UNSET)
        chart_type: Union[Unset, ListChartsInProjectResponse200ResultsItemChartType]
        if isinstance(_chart_type, Unset):
            chart_type = UNSET
        else:
            chart_type = ListChartsInProjectResponse200ResultsItemChartType(_chart_type)

        list_charts_in_project_response_200_results_item = cls(
            name=name,
            organization_uuid=organization_uuid,
            uuid=uuid,
            project_uuid=project_uuid,
            space_uuid=space_uuid,
            space_name=space_name,
            description=description,
            pinned_list_uuid=pinned_list_uuid,
            chart_type=chart_type,
        )

        list_charts_in_project_response_200_results_item.additional_properties = d
        return list_charts_in_project_response_200_results_item

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
