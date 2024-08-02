from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pick_chart_summary_uuid_or_name_or_space_uuid_or_space_name_or_dashboard_name_or_dashboard_uuid_or_chart_kind import (
        PickChartSummaryUuidOrNameOrSpaceUuidOrSpaceNameOrDashboardNameOrDashboardUuidOrChartKind,
    )


T = TypeVar("T", bound="CatalogAnalytics")


@_attrs_define
class CatalogAnalytics:
    """
    Attributes:
        charts (List['PickChartSummaryUuidOrNameOrSpaceUuidOrSpaceNameOrDashboardNameOrDashboardUuidOrChartKind']):
    """

    charts: List["PickChartSummaryUuidOrNameOrSpaceUuidOrSpaceNameOrDashboardNameOrDashboardUuidOrChartKind"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charts = []
        for charts_item_data in self.charts:
            charts_item = charts_item_data.to_dict()
            charts.append(charts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "charts": charts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_chart_summary_uuid_or_name_or_space_uuid_or_space_name_or_dashboard_name_or_dashboard_uuid_or_chart_kind import (
            PickChartSummaryUuidOrNameOrSpaceUuidOrSpaceNameOrDashboardNameOrDashboardUuidOrChartKind,
        )

        d = src_dict.copy()
        charts = []
        _charts = d.pop("charts")
        for charts_item_data in _charts:
            charts_item = (
                PickChartSummaryUuidOrNameOrSpaceUuidOrSpaceNameOrDashboardNameOrDashboardUuidOrChartKind.from_dict(
                    charts_item_data
                )
            )

            charts.append(charts_item)

        catalog_analytics = cls(
            charts=charts,
        )

        catalog_analytics.additional_properties = d
        return catalog_analytics

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
