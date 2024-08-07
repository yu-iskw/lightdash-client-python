from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.date_granularity import DateGranularity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sort_field import SortField


T = TypeVar("T", bound="PostDashboardTileBody")


@_attrs_define
class PostDashboardTileBody:
    """
    Attributes:
        dashboard_uuid (str):
        dashboard_sorts (List['SortField']):
        dashboard_filters (Any):
        auto_refresh (Union[Unset, bool]):
        granularity (Union[Unset, DateGranularity]):
        invalidate_cache (Union[Unset, bool]):
    """

    dashboard_uuid: str
    dashboard_sorts: List["SortField"]
    dashboard_filters: Any
    auto_refresh: Union[Unset, bool] = UNSET
    granularity: Union[Unset, DateGranularity] = UNSET
    invalidate_cache: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dashboard_uuid = self.dashboard_uuid

        dashboard_sorts = []
        for dashboard_sorts_item_data in self.dashboard_sorts:
            dashboard_sorts_item = dashboard_sorts_item_data.to_dict()
            dashboard_sorts.append(dashboard_sorts_item)

        dashboard_filters = self.dashboard_filters

        auto_refresh = self.auto_refresh

        granularity: Union[Unset, str] = UNSET
        if not isinstance(self.granularity, Unset):
            granularity = self.granularity.value

        invalidate_cache = self.invalidate_cache

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dashboardUuid": dashboard_uuid,
                "dashboardSorts": dashboard_sorts,
                "dashboardFilters": dashboard_filters,
            }
        )
        if auto_refresh is not UNSET:
            field_dict["autoRefresh"] = auto_refresh
        if granularity is not UNSET:
            field_dict["granularity"] = granularity
        if invalidate_cache is not UNSET:
            field_dict["invalidateCache"] = invalidate_cache

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sort_field import SortField

        d = src_dict.copy()
        dashboard_uuid = d.pop("dashboardUuid")

        dashboard_sorts = []
        _dashboard_sorts = d.pop("dashboardSorts")
        for dashboard_sorts_item_data in _dashboard_sorts:
            dashboard_sorts_item = SortField.from_dict(dashboard_sorts_item_data)

            dashboard_sorts.append(dashboard_sorts_item)

        dashboard_filters = d.pop("dashboardFilters")

        auto_refresh = d.pop("autoRefresh", UNSET)

        _granularity = d.pop("granularity", UNSET)
        granularity: Union[Unset, DateGranularity]
        if isinstance(_granularity, Unset):
            granularity = UNSET
        else:
            granularity = DateGranularity(_granularity)

        invalidate_cache = d.pop("invalidateCache", UNSET)

        post_dashboard_tile_body = cls(
            dashboard_uuid=dashboard_uuid,
            dashboard_sorts=dashboard_sorts,
            dashboard_filters=dashboard_filters,
            auto_refresh=auto_refresh,
            granularity=granularity,
            invalidate_cache=invalidate_cache,
        )

        post_dashboard_tile_body.additional_properties = d
        return post_dashboard_tile_body

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
