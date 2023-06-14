from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="ResourceViewSpaceItemData")


@attr.s(auto_attribs=True)
class ResourceViewSpaceItemData:
    """
    Attributes:
        name (str):
        organization_uuid (str):
        uuid (str):
        project_uuid (str):
        is_private (bool):
        chart_count (float):
        dashboard_count (float):
        access_list_length (float):
        access (List[str]):
        pinned_list_uuid (Optional[str]):
        pinned_list_order (Optional[float]):
    """

    name: str
    organization_uuid: str
    uuid: str
    project_uuid: str
    is_private: bool
    chart_count: float
    dashboard_count: float
    access_list_length: float
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
        chart_count = self.chart_count
        dashboard_count = self.dashboard_count
        access_list_length = self.access_list_length
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
                "chartCount": chart_count,
                "dashboardCount": dashboard_count,
                "accessListLength": access_list_length,
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

        chart_count = d.pop("chartCount")

        dashboard_count = d.pop("dashboardCount")

        access_list_length = d.pop("accessListLength")

        access = cast(List[str], d.pop("access"))

        pinned_list_uuid = d.pop("pinnedListUuid")

        pinned_list_order = d.pop("pinnedListOrder")

        resource_view_space_item_data = cls(
            name=name,
            organization_uuid=organization_uuid,
            uuid=uuid,
            project_uuid=project_uuid,
            is_private=is_private,
            chart_count=chart_count,
            dashboard_count=dashboard_count,
            access_list_length=access_list_length,
            access=access,
            pinned_list_uuid=pinned_list_uuid,
            pinned_list_order=pinned_list_order,
        )

        resource_view_space_item_data.additional_properties = d
        return resource_view_space_item_data

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
