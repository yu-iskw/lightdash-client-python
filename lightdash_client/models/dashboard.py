import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_chart_tile import DashboardChartTile
    from ..models.dashboard_filters import DashboardFilters
    from ..models.dashboard_loom_tile import DashboardLoomTile
    from ..models.dashboard_markdown_tile import DashboardMarkdownTile
    from ..models.dashboard_semantic_viewer_chart_tile import DashboardSemanticViewerChartTile
    from ..models.dashboard_sql_chart_tile import DashboardSqlChartTile
    from ..models.dashboard_tab import DashboardTab
    from ..models.space_share import SpaceShare
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar("T", bound="Dashboard")


@_attrs_define
class Dashboard:
    """
    Attributes:
        slug (str):
        access (Union[List['SpaceShare'], None]):
        is_private (Union[None, bool]):
        tabs (List['DashboardTab']):
        pinned_list_order (Union[None, float]):
        pinned_list_uuid (Union[None, str]):
        first_viewed_at (Union[None, datetime.datetime, str]):
        views (float):
        space_name (str):
        space_uuid (str):
        filters (DashboardFilters):
        tiles (List[Union['DashboardChartTile', 'DashboardLoomTile', 'DashboardMarkdownTile',
            'DashboardSemanticViewerChartTile', 'DashboardSqlChartTile']]):
        updated_at (datetime.datetime):
        name (str):
        uuid (str):
        dashboard_version_id (float):
        project_uuid (str):
        organization_uuid (str):
        updated_by_user (Union[Unset, UpdatedByUser]):
        description (Union[Unset, str]):
    """

    slug: str
    access: Union[List["SpaceShare"], None]
    is_private: Union[None, bool]
    tabs: List["DashboardTab"]
    pinned_list_order: Union[None, float]
    pinned_list_uuid: Union[None, str]
    first_viewed_at: Union[None, datetime.datetime, str]
    views: float
    space_name: str
    space_uuid: str
    filters: "DashboardFilters"
    tiles: List[
        Union[
            "DashboardChartTile",
            "DashboardLoomTile",
            "DashboardMarkdownTile",
            "DashboardSemanticViewerChartTile",
            "DashboardSqlChartTile",
        ]
    ]
    updated_at: datetime.datetime
    name: str
    uuid: str
    dashboard_version_id: float
    project_uuid: str
    organization_uuid: str
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_chart_tile import DashboardChartTile
        from ..models.dashboard_filters import DashboardFilters
        from ..models.dashboard_loom_tile import DashboardLoomTile
        from ..models.dashboard_markdown_tile import DashboardMarkdownTile
        from ..models.dashboard_semantic_viewer_chart_tile import DashboardSemanticViewerChartTile
        from ..models.dashboard_sql_chart_tile import DashboardSqlChartTile
        from ..models.dashboard_tab import DashboardTab
        from ..models.space_share import SpaceShare
        from ..models.updated_by_user import UpdatedByUser

        slug = self.slug

        access: Union[List[Dict[str, Any]], None]
        if isinstance(self.access, list):
            access = []
            for access_type_0_item_data in self.access:
                access_type_0_item = access_type_0_item_data.to_dict()
                access.append(access_type_0_item)

        else:
            access = self.access

        is_private: Union[None, bool]
        is_private = self.is_private

        tabs = []
        for tabs_item_data in self.tabs:
            tabs_item = tabs_item_data.to_dict()
            tabs.append(tabs_item)

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        first_viewed_at: Union[None, str]
        if isinstance(self.first_viewed_at, datetime.datetime):
            first_viewed_at = self.first_viewed_at.isoformat()
        else:
            first_viewed_at = self.first_viewed_at

        views = self.views

        space_name = self.space_name

        space_uuid = self.space_uuid

        filters = self.filters.to_dict()

        tiles = []
        for tiles_item_data in self.tiles:
            tiles_item: Dict[str, Any]
            if isinstance(tiles_item_data, DashboardChartTile):
                tiles_item = tiles_item_data.to_dict()
            elif isinstance(tiles_item_data, DashboardMarkdownTile):
                tiles_item = tiles_item_data.to_dict()
            elif isinstance(tiles_item_data, DashboardLoomTile):
                tiles_item = tiles_item_data.to_dict()
            elif isinstance(tiles_item_data, DashboardSqlChartTile):
                tiles_item = tiles_item_data.to_dict()
            else:
                tiles_item = tiles_item_data.to_dict()

            tiles.append(tiles_item)

        updated_at = self.updated_at.isoformat()

        name = self.name

        uuid = self.uuid

        dashboard_version_id = self.dashboard_version_id

        project_uuid = self.project_uuid

        organization_uuid = self.organization_uuid

        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "access": access,
                "isPrivate": is_private,
                "tabs": tabs,
                "pinnedListOrder": pinned_list_order,
                "pinnedListUuid": pinned_list_uuid,
                "firstViewedAt": first_viewed_at,
                "views": views,
                "spaceName": space_name,
                "spaceUuid": space_uuid,
                "filters": filters,
                "tiles": tiles,
                "updatedAt": updated_at,
                "name": name,
                "uuid": uuid,
                "dashboardVersionId": dashboard_version_id,
                "projectUuid": project_uuid,
                "organizationUuid": organization_uuid,
            }
        )
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_chart_tile import DashboardChartTile
        from ..models.dashboard_filters import DashboardFilters
        from ..models.dashboard_loom_tile import DashboardLoomTile
        from ..models.dashboard_markdown_tile import DashboardMarkdownTile
        from ..models.dashboard_semantic_viewer_chart_tile import DashboardSemanticViewerChartTile
        from ..models.dashboard_sql_chart_tile import DashboardSqlChartTile
        from ..models.dashboard_tab import DashboardTab
        from ..models.space_share import SpaceShare
        from ..models.updated_by_user import UpdatedByUser

        d = src_dict.copy()
        slug = d.pop("slug")

        def _parse_access(data: object) -> Union[List["SpaceShare"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_type_0 = []
                _access_type_0 = data
                for access_type_0_item_data in _access_type_0:
                    access_type_0_item = SpaceShare.from_dict(access_type_0_item_data)

                    access_type_0.append(access_type_0_item)

                return access_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SpaceShare"], None], data)

        access = _parse_access(d.pop("access"))

        def _parse_is_private(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        is_private = _parse_is_private(d.pop("isPrivate"))

        tabs = []
        _tabs = d.pop("tabs")
        for tabs_item_data in _tabs:
            tabs_item = DashboardTab.from_dict(tabs_item_data)

            tabs.append(tabs_item)

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        def _parse_first_viewed_at(data: object) -> Union[None, datetime.datetime, str]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_viewed_at_type_0 = isoparse(data)

                return first_viewed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime, str], data)

        first_viewed_at = _parse_first_viewed_at(d.pop("firstViewedAt"))

        views = d.pop("views")

        space_name = d.pop("spaceName")

        space_uuid = d.pop("spaceUuid")

        filters = DashboardFilters.from_dict(d.pop("filters"))

        tiles = []
        _tiles = d.pop("tiles")
        for tiles_item_data in _tiles:

            def _parse_tiles_item(
                data: object,
            ) -> Union[
                "DashboardChartTile",
                "DashboardLoomTile",
                "DashboardMarkdownTile",
                "DashboardSemanticViewerChartTile",
                "DashboardSqlChartTile",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_dashboard_tile_type_0 = DashboardChartTile.from_dict(data)

                    return componentsschemas_dashboard_tile_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_dashboard_tile_type_1 = DashboardMarkdownTile.from_dict(data)

                    return componentsschemas_dashboard_tile_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_dashboard_tile_type_2 = DashboardLoomTile.from_dict(data)

                    return componentsschemas_dashboard_tile_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_dashboard_tile_type_3 = DashboardSqlChartTile.from_dict(data)

                    return componentsschemas_dashboard_tile_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_dashboard_tile_type_4 = DashboardSemanticViewerChartTile.from_dict(data)

                return componentsschemas_dashboard_tile_type_4

            tiles_item = _parse_tiles_item(tiles_item_data)

            tiles.append(tiles_item)

        updated_at = isoparse(d.pop("updatedAt"))

        name = d.pop("name")

        uuid = d.pop("uuid")

        dashboard_version_id = d.pop("dashboardVersionId")

        project_uuid = d.pop("projectUuid")

        organization_uuid = d.pop("organizationUuid")

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, UpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UpdatedByUser.from_dict(_updated_by_user)

        description = d.pop("description", UNSET)

        dashboard = cls(
            slug=slug,
            access=access,
            is_private=is_private,
            tabs=tabs,
            pinned_list_order=pinned_list_order,
            pinned_list_uuid=pinned_list_uuid,
            first_viewed_at=first_viewed_at,
            views=views,
            space_name=space_name,
            space_uuid=space_uuid,
            filters=filters,
            tiles=tiles,
            updated_at=updated_at,
            name=name,
            uuid=uuid,
            dashboard_version_id=dashboard_version_id,
            project_uuid=project_uuid,
            organization_uuid=organization_uuid,
            updated_by_user=updated_by_user,
            description=description,
        )

        dashboard.additional_properties = d
        return dashboard

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
