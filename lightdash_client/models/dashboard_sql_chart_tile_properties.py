from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_tile_types_sqlchart import DashboardTileTypesSQLCHART
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_sql_chart_tile_properties_properties import DashboardSqlChartTilePropertiesProperties


T = TypeVar("T", bound="DashboardSqlChartTileProperties")


@_attrs_define
class DashboardSqlChartTileProperties:
    """
    Attributes:
        properties (DashboardSqlChartTilePropertiesProperties):
        type (DashboardTileTypesSQLCHART):
    """

    properties: "DashboardSqlChartTilePropertiesProperties"
    type: DashboardTileTypesSQLCHART
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_sql_chart_tile_properties_properties import DashboardSqlChartTilePropertiesProperties

        properties = self.properties.to_dict()

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "properties": properties,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_sql_chart_tile_properties_properties import DashboardSqlChartTilePropertiesProperties

        d = src_dict.copy()
        properties = DashboardSqlChartTilePropertiesProperties.from_dict(d.pop("properties"))

        type = DashboardTileTypesSQLCHART(d.pop("type"))

        dashboard_sql_chart_tile_properties = cls(
            properties=properties,
            type=type,
        )

        dashboard_sql_chart_tile_properties.additional_properties = d
        return dashboard_sql_chart_tile_properties

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
