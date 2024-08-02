from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_tile_types_markdown import DashboardTileTypesMARKDOWN

if TYPE_CHECKING:
    from ..models.dashboard_markdown_tile_properties_properties import (
        DashboardMarkdownTilePropertiesProperties,
    )


T = TypeVar("T", bound="DashboardMarkdownTileProperties")


@_attrs_define
class DashboardMarkdownTileProperties:
    """
    Attributes:
        properties (DashboardMarkdownTilePropertiesProperties):
        type (DashboardTileTypesMARKDOWN):
    """

    properties: "DashboardMarkdownTilePropertiesProperties"
    type: DashboardTileTypesMARKDOWN
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        from ..models.dashboard_markdown_tile_properties_properties import (
            DashboardMarkdownTilePropertiesProperties,
        )

        d = src_dict.copy()
        properties = DashboardMarkdownTilePropertiesProperties.from_dict(d.pop("properties"))

        type = DashboardTileTypesMARKDOWN(d.pop("type"))

        dashboard_markdown_tile_properties = cls(
            properties=properties,
            type=type,
        )

        dashboard_markdown_tile_properties.additional_properties = d
        return dashboard_markdown_tile_properties

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
