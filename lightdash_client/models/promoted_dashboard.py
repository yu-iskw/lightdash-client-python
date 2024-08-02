import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_chart_tile import DashboardChartTile
    from ..models.dashboard_filters import DashboardFilters
    from ..models.dashboard_loom_tile import DashboardLoomTile
    from ..models.dashboard_markdown_tile import DashboardMarkdownTile
    from ..models.dashboard_tab import DashboardTab
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar("T", bound="PromotedDashboard")


@_attrs_define
class PromotedDashboard:
    """
    Attributes:
        name (str):
        uuid (str):
        space_name (str):
        space_uuid (str):
        project_uuid (str):
        organization_uuid (str):
        pinned_list_uuid (Union[None, str]):
        dashboard_version_id (float):
        updated_at (datetime.datetime):
        tiles (List[Union['DashboardChartTile', 'DashboardLoomTile', 'DashboardMarkdownTile']]):
        filters (DashboardFilters):
        views (float):
        first_viewed_at (Union[None, datetime.datetime, str]):
        pinned_list_order (Union[None, float]):
        tabs (List['DashboardTab']):
        slug (str):
        space_slug (str):
        description (Union[Unset, str]):
        updated_by_user (Union[Unset, UpdatedByUser]):
    """

    name: str
    uuid: str
    space_name: str
    space_uuid: str
    project_uuid: str
    organization_uuid: str
    pinned_list_uuid: Union[None, str]
    dashboard_version_id: float
    updated_at: datetime.datetime
    tiles: List[Union["DashboardChartTile", "DashboardLoomTile", "DashboardMarkdownTile"]]
    filters: "DashboardFilters"
    views: float
    first_viewed_at: Union[None, datetime.datetime, str]
    pinned_list_order: Union[None, float]
    tabs: List["DashboardTab"]
    slug: str
    space_slug: str
    description: Union[Unset, str] = UNSET
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_chart_tile import DashboardChartTile
        from ..models.dashboard_markdown_tile import DashboardMarkdownTile

        name = self.name

        uuid = self.uuid

        space_name = self.space_name

        space_uuid = self.space_uuid

        project_uuid = self.project_uuid

        organization_uuid = self.organization_uuid

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        dashboard_version_id = self.dashboard_version_id

        updated_at = self.updated_at.isoformat()

        tiles = []
        for tiles_item_data in self.tiles:
            tiles_item: Dict[str, Any]
            if isinstance(tiles_item_data, DashboardChartTile):
                tiles_item = tiles_item_data.to_dict()
            elif isinstance(tiles_item_data, DashboardMarkdownTile):
                tiles_item = tiles_item_data.to_dict()
            else:
                tiles_item = tiles_item_data.to_dict()

            tiles.append(tiles_item)

        filters = self.filters.to_dict()

        views = self.views

        first_viewed_at: Union[None, str]
        if isinstance(self.first_viewed_at, datetime.datetime):
            first_viewed_at = self.first_viewed_at.isoformat()
        else:
            first_viewed_at = self.first_viewed_at

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        tabs = []
        for tabs_item_data in self.tabs:
            tabs_item = tabs_item_data.to_dict()
            tabs.append(tabs_item)

        slug = self.slug

        space_slug = self.space_slug

        description = self.description

        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "spaceName": space_name,
                "spaceUuid": space_uuid,
                "projectUuid": project_uuid,
                "organizationUuid": organization_uuid,
                "pinnedListUuid": pinned_list_uuid,
                "dashboardVersionId": dashboard_version_id,
                "updatedAt": updated_at,
                "tiles": tiles,
                "filters": filters,
                "views": views,
                "firstViewedAt": first_viewed_at,
                "pinnedListOrder": pinned_list_order,
                "tabs": tabs,
                "slug": slug,
                "spaceSlug": space_slug,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_chart_tile import DashboardChartTile
        from ..models.dashboard_filters import DashboardFilters
        from ..models.dashboard_loom_tile import DashboardLoomTile
        from ..models.dashboard_markdown_tile import DashboardMarkdownTile
        from ..models.dashboard_tab import DashboardTab
        from ..models.updated_by_user import UpdatedByUser

        d = src_dict.copy()
        name = d.pop("name")

        uuid = d.pop("uuid")

        space_name = d.pop("spaceName")

        space_uuid = d.pop("spaceUuid")

        project_uuid = d.pop("projectUuid")

        organization_uuid = d.pop("organizationUuid")

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        dashboard_version_id = d.pop("dashboardVersionId")

        updated_at = isoparse(d.pop("updatedAt"))

        tiles = []
        _tiles = d.pop("tiles")
        for tiles_item_data in _tiles:

            def _parse_tiles_item(
                data: object,
            ) -> Union["DashboardChartTile", "DashboardLoomTile", "DashboardMarkdownTile"]:
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
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_dashboard_tile_type_2 = DashboardLoomTile.from_dict(data)

                return componentsschemas_dashboard_tile_type_2

            tiles_item = _parse_tiles_item(tiles_item_data)

            tiles.append(tiles_item)

        filters = DashboardFilters.from_dict(d.pop("filters"))

        views = d.pop("views")

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

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        tabs = []
        _tabs = d.pop("tabs")
        for tabs_item_data in _tabs:
            tabs_item = DashboardTab.from_dict(tabs_item_data)

            tabs.append(tabs_item)

        slug = d.pop("slug")

        space_slug = d.pop("spaceSlug")

        description = d.pop("description", UNSET)

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, UpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UpdatedByUser.from_dict(_updated_by_user)

        promoted_dashboard = cls(
            name=name,
            uuid=uuid,
            space_name=space_name,
            space_uuid=space_uuid,
            project_uuid=project_uuid,
            organization_uuid=organization_uuid,
            pinned_list_uuid=pinned_list_uuid,
            dashboard_version_id=dashboard_version_id,
            updated_at=updated_at,
            tiles=tiles,
            filters=filters,
            views=views,
            first_viewed_at=first_viewed_at,
            pinned_list_order=pinned_list_order,
            tabs=tabs,
            slug=slug,
            space_slug=space_slug,
            description=description,
            updated_by_user=updated_by_user,
        )

        promoted_dashboard.additional_properties = d
        return promoted_dashboard

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
