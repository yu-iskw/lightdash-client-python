from typing import Any, Dict, List, Optional, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ListSpacesInProjectResponse200ResultsItem")


@attr.s(auto_attribs=True)
class ListSpacesInProjectResponse200ResultsItem:
    """
    Attributes:
        name (str):
        organization_uuid (str):
        uuid (str):
        project_uuid (str):
        is_private (bool):
        dashboard_count (float):
        chart_count (float):
        access (List[str]):
        pinned_list_uuid (Optional[str]):
        pinned_list_order (Optional[float]):
    """

    name: str
    organization_uuid: str
    uuid: str
    project_uuid: str
    is_private: bool
    dashboard_count: float
    chart_count: float
    access: List[str]
    pinned_list_uuid: Optional[str]
    pinned_list_order: Optional[float]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        organization_uuid = self.organization_uuid
        uuid = self.uuid
        project_uuid = self.project_uuid
        is_private = self.is_private
        dashboard_count = self.dashboard_count
        chart_count = self.chart_count
        access = self.access

        pinned_list_uuid = self.pinned_list_uuid
        pinned_list_order = self.pinned_list_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "organizationUuid": organization_uuid,
                "uuid": uuid,
                "projectUuid": project_uuid,
                "isPrivate": is_private,
                "dashboardCount": dashboard_count,
                "chartCount": chart_count,
                "access": access,
                "pinnedListUuid": pinned_list_uuid,
                "pinnedListOrder": pinned_list_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization_uuid = d.pop("organizationUuid")

        uuid = d.pop("uuid")

        project_uuid = d.pop("projectUuid")

        is_private = d.pop("isPrivate")

        dashboard_count = d.pop("dashboardCount")

        chart_count = d.pop("chartCount")

        access = cast(List[str], d.pop("access"))

        pinned_list_uuid = d.pop("pinnedListUuid")

        pinned_list_order = d.pop("pinnedListOrder")

        list_spaces_in_project_response_200_results_item = cls(
            name=name,
            organization_uuid=organization_uuid,
            uuid=uuid,
            project_uuid=project_uuid,
            is_private=is_private,
            dashboard_count=dashboard_count,
            chart_count=chart_count,
            access=access,
            pinned_list_uuid=pinned_list_uuid,
            pinned_list_order=pinned_list_order,
        )

        list_spaces_in_project_response_200_results_item.additional_properties = d
        return list_spaces_in_project_response_200_results_item

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
