from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_tile_types import DashboardTileTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_tile_as_code_properties_type_1 import DashboardTileAsCodePropertiesType1
    from ..models.dashboard_tile_as_code_properties_type_2 import DashboardTileAsCodePropertiesType2
    from ..models.pick_dashboard_chart_tile_properties_at_properties_title_or_hide_title_or_chart_slug import (
        PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug,
    )


T = TypeVar("T", bound="DashboardTileAsCode")


@_attrs_define
class DashboardTileAsCode:
    """
    Attributes:
        type (DashboardTileTypes):
        x (float):
        y (float):
        h (float):
        w (float):
        properties (Union['DashboardTileAsCodePropertiesType1', 'DashboardTileAsCodePropertiesType2',
            'PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug']):
        tab_uuid (Union[Unset, str]):
        uuid (Union[Unset, str]):
    """

    type: DashboardTileTypes
    x: float
    y: float
    h: float
    w: float
    properties: Union[
        "DashboardTileAsCodePropertiesType1",
        "DashboardTileAsCodePropertiesType2",
        "PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug",
    ]
    tab_uuid: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_tile_as_code_properties_type_1 import DashboardTileAsCodePropertiesType1
        from ..models.dashboard_tile_as_code_properties_type_2 import DashboardTileAsCodePropertiesType2
        from ..models.pick_dashboard_chart_tile_properties_at_properties_title_or_hide_title_or_chart_slug import (
            PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug,
        )

        type = self.type.value

        x = self.x

        y = self.y

        h = self.h

        w = self.w

        properties: Dict[str, Any]
        if isinstance(self.properties, PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug):
            properties = self.properties.to_dict()
        elif isinstance(self.properties, DashboardTileAsCodePropertiesType1):
            properties = self.properties.to_dict()
        else:
            properties = self.properties.to_dict()

        tab_uuid = self.tab_uuid

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_tile_as_code_properties_type_1 import DashboardTileAsCodePropertiesType1
        from ..models.dashboard_tile_as_code_properties_type_2 import DashboardTileAsCodePropertiesType2
        from ..models.pick_dashboard_chart_tile_properties_at_properties_title_or_hide_title_or_chart_slug import (
            PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug,
        )

        d = src_dict.copy()
        type = DashboardTileTypes(d.pop("type"))

        x = d.pop("x")

        y = d.pop("y")

        h = d.pop("h")

        w = d.pop("w")

        def _parse_properties(
            data: object,
        ) -> Union[
            "DashboardTileAsCodePropertiesType1",
            "DashboardTileAsCodePropertiesType2",
            "PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = PickDashboardChartTilePropertiesAtPropertiesTitleOrHideTitleOrChartSlug.from_dict(
                    data
                )

                return properties_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = DashboardTileAsCodePropertiesType1.from_dict(data)

                return properties_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_2 = DashboardTileAsCodePropertiesType2.from_dict(data)

            return properties_type_2

        properties = _parse_properties(d.pop("properties"))

        tab_uuid = d.pop("tabUuid", UNSET)

        uuid = d.pop("uuid", UNSET)

        dashboard_tile_as_code = cls(
            type=type,
            x=x,
            y=y,
            h=h,
            w=w,
            properties=properties,
            tab_uuid=tab_uuid,
            uuid=uuid,
        )

        dashboard_tile_as_code.additional_properties = d
        return dashboard_tile_as_code

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
