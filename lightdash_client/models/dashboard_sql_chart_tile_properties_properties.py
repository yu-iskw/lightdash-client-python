from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardSqlChartTilePropertiesProperties")


@_attrs_define
class DashboardSqlChartTilePropertiesProperties:
    """
    Attributes:
        chart_name (str):
        saved_sql_uuid (Union[None, str]):
        hide_title (Union[Unset, bool]):
        title (Union[Unset, str]):
    """

    chart_name: str
    saved_sql_uuid: Union[None, str]
    hide_title: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chart_name = self.chart_name

        saved_sql_uuid: Union[None, str]
        saved_sql_uuid = self.saved_sql_uuid

        hide_title = self.hide_title

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chartName": chart_name,
                "savedSqlUuid": saved_sql_uuid,
            }
        )
        if hide_title is not UNSET:
            field_dict["hideTitle"] = hide_title
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chart_name = d.pop("chartName")

        def _parse_saved_sql_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        saved_sql_uuid = _parse_saved_sql_uuid(d.pop("savedSqlUuid"))

        hide_title = d.pop("hideTitle", UNSET)

        title = d.pop("title", UNSET)

        dashboard_sql_chart_tile_properties_properties = cls(
            chart_name=chart_name,
            saved_sql_uuid=saved_sql_uuid,
            hide_title=hide_title,
            title=title,
        )

        dashboard_sql_chart_tile_properties_properties.additional_properties = d
        return dashboard_sql_chart_tile_properties_properties

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
