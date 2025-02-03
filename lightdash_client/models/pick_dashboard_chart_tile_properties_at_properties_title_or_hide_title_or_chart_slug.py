from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug")


@_attrs_define
class PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        title (Union[Unset, str]):
        hide_title (Union[Unset, bool]):
        chart_slug (Union[Unset, str]):
    """

    title: Union[Unset, str] = UNSET
    hide_title: Union[Unset, bool] = UNSET
    chart_slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        hide_title = self.hide_title

        chart_slug = self.chart_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if hide_title is not UNSET:
            field_dict["hideTitle"] = hide_title
        if chart_slug is not UNSET:
            field_dict["chartSlug"] = chart_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        hide_title = d.pop("hideTitle", UNSET)

        chart_slug = d.pop("chartSlug", UNSET)

        pick_dashboard_chart_tile_properties_at_properties_title_or_hide_title_or_chart_slug = cls(
            title=title,
            hide_title=hide_title,
            chart_slug=chart_slug,
        )

        pick_dashboard_chart_tile_properties_at_properties_title_or_hide_title_or_chart_slug.additional_properties = d
        return pick_dashboard_chart_tile_properties_at_properties_title_or_hide_title_or_chart_slug

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
