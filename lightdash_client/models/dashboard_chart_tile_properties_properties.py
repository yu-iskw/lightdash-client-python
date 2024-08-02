from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_kind import ChartKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardChartTilePropertiesProperties")


@_attrs_define
class DashboardChartTilePropertiesProperties:
    """
    Attributes:
        saved_chart_uuid (Union[None, str]):
        last_version_chart_kind (Union[ChartKind, None, Unset]):
        chart_name (Union[None, Unset, str]):
        belongs_to_dashboard (Union[Unset, bool]):
        hide_title (Union[Unset, bool]):
        title (Union[Unset, str]):
    """

    saved_chart_uuid: Union[None, str]
    last_version_chart_kind: Union[ChartKind, None, Unset] = UNSET
    chart_name: Union[None, Unset, str] = UNSET
    belongs_to_dashboard: Union[Unset, bool] = UNSET
    hide_title: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        saved_chart_uuid: Union[None, str]
        saved_chart_uuid = self.saved_chart_uuid

        last_version_chart_kind: Union[None, Unset, str]
        if isinstance(self.last_version_chart_kind, Unset):
            last_version_chart_kind = UNSET
        elif isinstance(self.last_version_chart_kind, ChartKind):
            last_version_chart_kind = self.last_version_chart_kind.value
        else:
            last_version_chart_kind = self.last_version_chart_kind

        chart_name: Union[None, Unset, str]
        if isinstance(self.chart_name, Unset):
            chart_name = UNSET
        else:
            chart_name = self.chart_name

        belongs_to_dashboard = self.belongs_to_dashboard

        hide_title = self.hide_title

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "savedChartUuid": saved_chart_uuid,
            }
        )
        if last_version_chart_kind is not UNSET:
            field_dict["lastVersionChartKind"] = last_version_chart_kind
        if chart_name is not UNSET:
            field_dict["chartName"] = chart_name
        if belongs_to_dashboard is not UNSET:
            field_dict["belongsToDashboard"] = belongs_to_dashboard
        if hide_title is not UNSET:
            field_dict["hideTitle"] = hide_title
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_saved_chart_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        saved_chart_uuid = _parse_saved_chart_uuid(d.pop("savedChartUuid"))

        def _parse_last_version_chart_kind(data: object) -> Union[ChartKind, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_version_chart_kind_type_1 = ChartKind(data)

                return last_version_chart_kind_type_1
            except:  # noqa: E722
                pass
            return cast(Union[ChartKind, None, Unset], data)

        last_version_chart_kind = _parse_last_version_chart_kind(d.pop("lastVersionChartKind", UNSET))

        def _parse_chart_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chart_name = _parse_chart_name(d.pop("chartName", UNSET))

        belongs_to_dashboard = d.pop("belongsToDashboard", UNSET)

        hide_title = d.pop("hideTitle", UNSET)

        title = d.pop("title", UNSET)

        dashboard_chart_tile_properties_properties = cls(
            saved_chart_uuid=saved_chart_uuid,
            last_version_chart_kind=last_version_chart_kind,
            chart_name=chart_name,
            belongs_to_dashboard=belongs_to_dashboard,
            hide_title=hide_title,
            title=title,
        )

        dashboard_chart_tile_properties_properties.additional_properties = d
        return dashboard_chart_tile_properties_properties

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
