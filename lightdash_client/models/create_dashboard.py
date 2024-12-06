from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_dashboard_chart_tile import CreateDashboardChartTile
    from ..models.create_dashboard_loom_tile import CreateDashboardLoomTile
    from ..models.create_dashboard_markdown_tile import CreateDashboardMarkdownTile
    from ..models.create_dashboard_semantic_viewer_chart_tile import CreateDashboardSemanticViewerChartTile
    from ..models.create_dashboard_sql_chart_tile import CreateDashboardSqlChartTile
    from ..models.dashboard_filters import DashboardFilters
    from ..models.dashboard_tab import DashboardTab
    from ..models.pick_updated_by_user_user_uuid import PickUpdatedByUserUserUuid


T = TypeVar("T", bound="CreateDashboard")


@_attrs_define
class CreateDashboard:
    """
    Attributes:
        tabs (List['DashboardTab']):
        tiles (List[Union['CreateDashboardChartTile', 'CreateDashboardLoomTile', 'CreateDashboardMarkdownTile',
            'CreateDashboardSemanticViewerChartTile', 'CreateDashboardSqlChartTile']]):
        name (str):
        space_uuid (Union[Unset, str]):
        updated_by_user (Union[Unset, PickUpdatedByUserUserUuid]): From T, pick a set of properties whose keys are in
            the union K
        filters (Union[Unset, DashboardFilters]):
        description (Union[Unset, str]):
    """

    tabs: List["DashboardTab"]
    tiles: List[
        Union[
            "CreateDashboardChartTile",
            "CreateDashboardLoomTile",
            "CreateDashboardMarkdownTile",
            "CreateDashboardSemanticViewerChartTile",
            "CreateDashboardSqlChartTile",
        ]
    ]
    name: str
    space_uuid: Union[Unset, str] = UNSET
    updated_by_user: Union[Unset, "PickUpdatedByUserUserUuid"] = UNSET
    filters: Union[Unset, "DashboardFilters"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.create_dashboard_chart_tile import CreateDashboardChartTile
        from ..models.create_dashboard_loom_tile import CreateDashboardLoomTile
        from ..models.create_dashboard_markdown_tile import CreateDashboardMarkdownTile
        from ..models.create_dashboard_semantic_viewer_chart_tile import CreateDashboardSemanticViewerChartTile
        from ..models.create_dashboard_sql_chart_tile import CreateDashboardSqlChartTile
        from ..models.dashboard_filters import DashboardFilters
        from ..models.dashboard_tab import DashboardTab
        from ..models.pick_updated_by_user_user_uuid import PickUpdatedByUserUserUuid

        tabs = []
        for tabs_item_data in self.tabs:
            tabs_item = tabs_item_data.to_dict()
            tabs.append(tabs_item)

        tiles = []
        for tiles_item_data in self.tiles:
            tiles_item: Dict[str, Any]
            if isinstance(tiles_item_data, CreateDashboardChartTile):
                tiles_item = tiles_item_data.to_dict()
            elif isinstance(tiles_item_data, CreateDashboardMarkdownTile):
                tiles_item = tiles_item_data.to_dict()
            elif isinstance(tiles_item_data, CreateDashboardLoomTile):
                tiles_item = tiles_item_data.to_dict()
            elif isinstance(tiles_item_data, CreateDashboardSqlChartTile):
                tiles_item = tiles_item_data.to_dict()
            else:
                tiles_item = tiles_item_data.to_dict()

            tiles.append(tiles_item)

        name = self.name

        space_uuid = self.space_uuid

        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tabs": tabs,
                "tiles": tiles,
                "name": name,
            }
        )
        if space_uuid is not UNSET:
            field_dict["spaceUuid"] = space_uuid
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user
        if filters is not UNSET:
            field_dict["filters"] = filters
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_dashboard_chart_tile import CreateDashboardChartTile
        from ..models.create_dashboard_loom_tile import CreateDashboardLoomTile
        from ..models.create_dashboard_markdown_tile import CreateDashboardMarkdownTile
        from ..models.create_dashboard_semantic_viewer_chart_tile import CreateDashboardSemanticViewerChartTile
        from ..models.create_dashboard_sql_chart_tile import CreateDashboardSqlChartTile
        from ..models.dashboard_filters import DashboardFilters
        from ..models.dashboard_tab import DashboardTab
        from ..models.pick_updated_by_user_user_uuid import PickUpdatedByUserUserUuid

        d = src_dict.copy()
        tabs = []
        _tabs = d.pop("tabs")
        for tabs_item_data in _tabs:
            tabs_item = DashboardTab.from_dict(tabs_item_data)

            tabs.append(tabs_item)

        tiles = []
        _tiles = d.pop("tiles")
        for tiles_item_data in _tiles:

            def _parse_tiles_item(
                data: object,
            ) -> Union[
                "CreateDashboardChartTile",
                "CreateDashboardLoomTile",
                "CreateDashboardMarkdownTile",
                "CreateDashboardSemanticViewerChartTile",
                "CreateDashboardSqlChartTile",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tiles_item_type_0 = CreateDashboardChartTile.from_dict(data)

                    return tiles_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tiles_item_type_1 = CreateDashboardMarkdownTile.from_dict(data)

                    return tiles_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tiles_item_type_2 = CreateDashboardLoomTile.from_dict(data)

                    return tiles_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tiles_item_type_3 = CreateDashboardSqlChartTile.from_dict(data)

                    return tiles_item_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                tiles_item_type_4 = CreateDashboardSemanticViewerChartTile.from_dict(data)

                return tiles_item_type_4

            tiles_item = _parse_tiles_item(tiles_item_data)

            tiles.append(tiles_item)

        name = d.pop("name")

        space_uuid = d.pop("spaceUuid", UNSET)

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, PickUpdatedByUserUserUuid]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = PickUpdatedByUserUserUuid.from_dict(_updated_by_user)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, DashboardFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = DashboardFilters.from_dict(_filters)

        description = d.pop("description", UNSET)

        create_dashboard = cls(
            tabs=tabs,
            tiles=tiles,
            name=name,
            space_uuid=space_uuid,
            updated_by_user=updated_by_user,
            filters=filters,
            description=description,
        )

        create_dashboard.additional_properties = d
        return create_dashboard

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
