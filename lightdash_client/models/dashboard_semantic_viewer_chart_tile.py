from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_tile_types_semanticviewerchart import DashboardTileTypesSEMANTICVIEWERCHART
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_semantic_viewer_chart_tile_properties_properties import (
        DashboardSemanticViewerChartTilePropertiesProperties,
    )


T = TypeVar("T", bound="DashboardSemanticViewerChartTile")


@_attrs_define
class DashboardSemanticViewerChartTile:
    """
    Attributes:
        uuid (str):
        type (DashboardTileTypesSEMANTICVIEWERCHART):
        x (float):
        y (float):
        h (float):
        w (float):
        properties (DashboardSemanticViewerChartTilePropertiesProperties):
        tab_uuid (Union[Unset, str]):
    """

    uuid: str
    type: DashboardTileTypesSEMANTICVIEWERCHART
    x: float
    y: float
    h: float
    w: float
    properties: "DashboardSemanticViewerChartTilePropertiesProperties"
    tab_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_semantic_viewer_chart_tile_properties_properties import (
            DashboardSemanticViewerChartTilePropertiesProperties,
        )

        uuid = self.uuid

        type = self.type.value

        x = self.x

        y = self.y

        h = self.h

        w = self.w

        properties = self.properties.to_dict()

        tab_uuid = self.tab_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "type": type,
                "x": x,
                "y": y,
                "h": h,
                "w": w,
                "properties": properties,
            }
        )
        if tab_uuid is not UNSET:
            field_dict["tabUuid"] = tab_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_semantic_viewer_chart_tile_properties_properties import (
            DashboardSemanticViewerChartTilePropertiesProperties,
        )

        d = src_dict.copy()
        uuid = d.pop("uuid")

        type = DashboardTileTypesSEMANTICVIEWERCHART(d.pop("type"))

        x = d.pop("x")

        y = d.pop("y")

        h = d.pop("h")

        w = d.pop("w")

        properties = DashboardSemanticViewerChartTilePropertiesProperties.from_dict(d.pop("properties"))

        tab_uuid = d.pop("tabUuid", UNSET)

        dashboard_semantic_viewer_chart_tile = cls(
            uuid=uuid,
            type=type,
            x=x,
            y=y,
            h=h,
            w=w,
            properties=properties,
            tab_uuid=tab_uuid,
        )

        dashboard_semantic_viewer_chart_tile.additional_properties = d
        return dashboard_semantic_viewer_chart_tile

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
