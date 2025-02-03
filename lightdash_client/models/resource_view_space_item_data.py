from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceViewSpaceItemData")


@_attrs_define
class ResourceViewSpaceItemData:
    """
    Attributes:
        name (str):
        project_uuid (str):
        uuid (str):
        organization_uuid (str):
        is_private (bool):
        pinned_list_uuid (Union[None, str]):
        pinned_list_order (Union[None, float]):
        chart_count (float):
        dashboard_count (float):
        access_list_length (float):
        access (List[str]):
    """

    name: str
    project_uuid: str
    uuid: str
    organization_uuid: str
    is_private: bool
    pinned_list_uuid: Union[None, str]
    pinned_list_order: Union[None, float]
    chart_count: float
    dashboard_count: float
    access_list_length: float
    access: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        project_uuid = self.project_uuid

        uuid = self.uuid

        organization_uuid = self.organization_uuid

        is_private = self.is_private

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        chart_count = self.chart_count

        dashboard_count = self.dashboard_count

        access_list_length = self.access_list_length

        access = self.access

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "projectUuid": project_uuid,
                "uuid": uuid,
                "organizationUuid": organization_uuid,
                "isPrivate": is_private,
                "pinnedListUuid": pinned_list_uuid,
                "pinnedListOrder": pinned_list_order,
                "chartCount": chart_count,
                "dashboardCount": dashboard_count,
                "accessListLength": access_list_length,
                "access": access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        uuid = d.pop("uuid")

        organization_uuid = d.pop("organizationUuid")

        is_private = d.pop("isPrivate")

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        chart_count = d.pop("chartCount")

        dashboard_count = d.pop("dashboardCount")

        access_list_length = d.pop("accessListLength")

        access = cast(List[str], d.pop("access"))

        resource_view_space_item_data = cls(
            name=name,
            project_uuid=project_uuid,
            uuid=uuid,
            organization_uuid=organization_uuid,
            is_private=is_private,
            pinned_list_uuid=pinned_list_uuid,
            pinned_list_order=pinned_list_order,
            chart_count=chart_count,
            dashboard_count=dashboard_count,
            access_list_length=access_list_length,
            access=access,
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
