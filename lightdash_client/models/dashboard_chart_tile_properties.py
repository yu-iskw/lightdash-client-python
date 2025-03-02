from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_tile_types_savedchart import DashboardTileTypesSAVEDCHART
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_chart_tile_properties_properties import DashboardChartTilePropertiesProperties


T = TypeVar("T", bound="DashboardChartTileProperties")


@_attrs_define
class DashboardChartTileProperties:
    """
    Attributes:
        properties (DashboardChartTilePropertiesProperties):
        type (DashboardTileTypesSAVEDCHART):
    """

    properties: "DashboardChartTilePropertiesProperties"
    type: DashboardTileTypesSAVEDCHART
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_chart_tile_properties_properties import DashboardChartTilePropertiesProperties

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
        from ..models.dashboard_chart_tile_properties_properties import DashboardChartTilePropertiesProperties

        d = src_dict.copy()
        properties = DashboardChartTilePropertiesProperties.from_dict(d.pop("properties"))

        type = DashboardTileTypesSAVEDCHART(d.pop("type"))

        dashboard_chart_tile_properties = cls(
            properties=properties,
            type=type,
        )

        dashboard_chart_tile_properties.additional_properties = d
        return dashboard_chart_tile_properties

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
