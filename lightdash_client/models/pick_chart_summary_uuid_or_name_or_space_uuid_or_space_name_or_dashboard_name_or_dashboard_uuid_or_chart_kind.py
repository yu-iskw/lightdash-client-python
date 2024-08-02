from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_kind import ChartKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="PickChartSummaryUuidOrNameOrSpaceUuidOrSpaceNameOrDashboardNameOrDashboardUuidOrChartKind")


@_attrs_define
class PickChartSummaryUuidOrNameOrSpaceUuidOrSpaceNameOrDashboardNameOrDashboardUuidOrChartKind:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        uuid (str):
        space_name (str):
        space_uuid (str):
        dashboard_uuid (Union[None, str]):
        dashboard_name (Union[None, str]):
        chart_kind (Union[Unset, ChartKind]):
    """

    name: str
    uuid: str
    space_name: str
    space_uuid: str
    dashboard_uuid: Union[None, str]
    dashboard_name: Union[None, str]
    chart_kind: Union[Unset, ChartKind] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        uuid = self.uuid

        space_name = self.space_name

        space_uuid = self.space_uuid

        dashboard_uuid: Union[None, str]
        dashboard_uuid = self.dashboard_uuid

        dashboard_name: Union[None, str]
        dashboard_name = self.dashboard_name

        chart_kind: Union[Unset, str] = UNSET
        if not isinstance(self.chart_kind, Unset):
            chart_kind = self.chart_kind.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "spaceName": space_name,
                "spaceUuid": space_uuid,
                "dashboardUuid": dashboard_uuid,
                "dashboardName": dashboard_name,
            }
        )
        if chart_kind is not UNSET:
            field_dict["chartKind"] = chart_kind

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        uuid = d.pop("uuid")

        space_name = d.pop("spaceName")

        space_uuid = d.pop("spaceUuid")

        def _parse_dashboard_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_uuid = _parse_dashboard_uuid(d.pop("dashboardUuid"))

        def _parse_dashboard_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_name = _parse_dashboard_name(d.pop("dashboardName"))

        _chart_kind = d.pop("chartKind", UNSET)
        chart_kind: Union[Unset, ChartKind]
        if isinstance(_chart_kind, Unset):
            chart_kind = UNSET
        else:
            chart_kind = ChartKind(_chart_kind)

        pick_chart_summary_uuid_or_name_or_space_uuid_or_space_name_or_dashboard_name_or_dashboard_uuid_or_chart_kind = cls(
            name=name,
            uuid=uuid,
            space_name=space_name,
            space_uuid=space_uuid,
            dashboard_uuid=dashboard_uuid,
            dashboard_name=dashboard_name,
            chart_kind=chart_kind,
        )

        pick_chart_summary_uuid_or_name_or_space_uuid_or_space_name_or_dashboard_name_or_dashboard_uuid_or_chart_kind.additional_properties = d
        return pick_chart_summary_uuid_or_name_or_space_uuid_or_space_name_or_dashboard_name_or_dashboard_uuid_or_chart_kind

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
