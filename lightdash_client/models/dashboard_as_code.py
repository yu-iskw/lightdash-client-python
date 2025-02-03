import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_filters import DashboardFilters
    from ..models.dashboard_tab import DashboardTab
    from ..models.dashboard_tile_as_code import DashboardTileAsCode


T = TypeVar("T", bound="DashboardAsCode")


@_attrs_define
class DashboardAsCode:
    """
    Attributes:
        name (str):
        slug (str):
        updated_at (datetime.datetime):
        filters (DashboardFilters):
        tabs (List['DashboardTab']):
        space_slug (str):
        version (float):
        tiles (List['DashboardTileAsCode']):
        description (Union[Unset, str]):
        downloaded_at (Union[Unset, datetime.datetime]):
    """

    name: str
    slug: str
    updated_at: datetime.datetime
    filters: "DashboardFilters"
    tabs: List["DashboardTab"]
    space_slug: str
    version: float
    tiles: List["DashboardTileAsCode"]
    description: Union[Unset, str] = UNSET
    downloaded_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_filters import DashboardFilters
        from ..models.dashboard_tab import DashboardTab
        from ..models.dashboard_tile_as_code import DashboardTileAsCode

        name = self.name

        slug = self.slug

        updated_at = self.updated_at.isoformat()

        filters = self.filters.to_dict()

        tabs = []
        for tabs_item_data in self.tabs:
            tabs_item = tabs_item_data.to_dict()
            tabs.append(tabs_item)

        space_slug = self.space_slug

        version = self.version

        tiles = []
        for tiles_item_data in self.tiles:
            tiles_item = tiles_item_data.to_dict()
            tiles.append(tiles_item)

        description = self.description

        downloaded_at: Union[Unset, str] = UNSET
        if not isinstance(self.downloaded_at, Unset):
            downloaded_at = self.downloaded_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "updatedAt": updated_at,
                "filters": filters,
                "tabs": tabs,
                "spaceSlug": space_slug,
                "version": version,
                "tiles": tiles,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if downloaded_at is not UNSET:
            field_dict["downloadedAt"] = downloaded_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_filters import DashboardFilters
        from ..models.dashboard_tab import DashboardTab
        from ..models.dashboard_tile_as_code import DashboardTileAsCode

        d = src_dict.copy()
        name = d.pop("name")

        slug = d.pop("slug")

        updated_at = isoparse(d.pop("updatedAt"))

        filters = DashboardFilters.from_dict(d.pop("filters"))

        tabs = []
        _tabs = d.pop("tabs")
        for tabs_item_data in _tabs:
            tabs_item = DashboardTab.from_dict(tabs_item_data)

            tabs.append(tabs_item)

        space_slug = d.pop("spaceSlug")

        version = d.pop("version")

        tiles = []
        _tiles = d.pop("tiles")
        for tiles_item_data in _tiles:
            tiles_item = DashboardTileAsCode.from_dict(tiles_item_data)

            tiles.append(tiles_item)

        description = d.pop("description", UNSET)

        _downloaded_at = d.pop("downloadedAt", UNSET)
        downloaded_at: Union[Unset, datetime.datetime]
        if isinstance(_downloaded_at, Unset):
            downloaded_at = UNSET
        else:
            downloaded_at = isoparse(_downloaded_at)

        dashboard_as_code = cls(
            name=name,
            slug=slug,
            updated_at=updated_at,
            filters=filters,
            tabs=tabs,
            space_slug=space_slug,
            version=version,
            tiles=tiles,
            description=description,
            downloaded_at=downloaded_at,
        )

        dashboard_as_code.additional_properties = d
        return dashboard_as_code

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
