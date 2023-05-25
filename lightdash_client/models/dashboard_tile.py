from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..models.create_dashboard_tile_type import CreateDashboardTileType

if TYPE_CHECKING:
    from ..models.loom_tile_properties import LoomTileProperties
    from ..models.markdown_tile_properties import MarkdownTileProperties
    from ..models.tile_properties_chart import TilePropertiesChart


T = TypeVar("T", bound="DashboardTile")


@attr.s(auto_attribs=True)
class DashboardTile:
    """
    Attributes:
        type (CreateDashboardTileType):
        properties (Union['LoomTileProperties', 'MarkdownTileProperties', 'TilePropertiesChart']):
        x (float):
        y (float):
        h (float):
        w (float):
        uuid (str):
    """

    type: CreateDashboardTileType
    properties: Union["LoomTileProperties", "MarkdownTileProperties", "TilePropertiesChart"]
    x: float
    y: float
    h: float
    w: float
    uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.loom_tile_properties import LoomTileProperties
        from ..models.tile_properties_chart import TilePropertiesChart

        type = self.type.value

        properties: Dict[str, Any]

        if isinstance(self.properties, TilePropertiesChart):
            properties = self.properties.to_dict()

        elif isinstance(self.properties, LoomTileProperties):
            properties = self.properties.to_dict()

        else:
            properties = self.properties.to_dict()

        x = self.x
        y = self.y
        h = self.h
        w = self.w
        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "properties": properties,
                "x": x,
                "y": y,
                "h": h,
                "w": w,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.loom_tile_properties import LoomTileProperties
        from ..models.markdown_tile_properties import MarkdownTileProperties
        from ..models.tile_properties_chart import TilePropertiesChart

        d = src_dict.copy()
        type = CreateDashboardTileType(d.pop("type"))

        def _parse_properties(
            data: object,
        ) -> Union["LoomTileProperties", "MarkdownTileProperties", "TilePropertiesChart"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = TilePropertiesChart.from_dict(data)

                return properties_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = LoomTileProperties.from_dict(data)

                return properties_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_2 = MarkdownTileProperties.from_dict(data)

            return properties_type_2

        properties = _parse_properties(d.pop("properties"))

        x = d.pop("x")

        y = d.pop("y")

        h = d.pop("h")

        w = d.pop("w")

        uuid = d.pop("uuid")

        dashboard_tile = cls(
            type=type,
            properties=properties,
            x=x,
            y=y,
            h=h,
            w=w,
            uuid=uuid,
        )

        dashboard_tile.additional_properties = d
        return dashboard_tile

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
