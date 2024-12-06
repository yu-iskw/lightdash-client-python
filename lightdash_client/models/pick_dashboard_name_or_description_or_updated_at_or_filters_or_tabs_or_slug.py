import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_filters import DashboardFilters
    from ..models.dashboard_tab import DashboardTab


T = TypeVar("T", bound="PickDashboardNameOrDescriptionOrUpdatedAtOrFiltersOrTabsOrSlug")


@_attrs_define
class PickDashboardNameOrDescriptionOrUpdatedAtOrFiltersOrTabsOrSlug:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        slug (str):
        updated_at (datetime.datetime):
        filters (DashboardFilters):
        tabs (List['DashboardTab']):
        description (Union[Unset, str]):
    """

    name: str
    slug: str
    updated_at: datetime.datetime
    filters: "DashboardFilters"
    tabs: List["DashboardTab"]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_filters import DashboardFilters
        from ..models.dashboard_tab import DashboardTab

        name = self.name

        slug = self.slug

        updated_at = self.updated_at.isoformat()

        filters = self.filters.to_dict()

        tabs = []
        for tabs_item_data in self.tabs:
            tabs_item = tabs_item_data.to_dict()
            tabs.append(tabs_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "updatedAt": updated_at,
                "filters": filters,
                "tabs": tabs,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_filters import DashboardFilters
        from ..models.dashboard_tab import DashboardTab

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

        description = d.pop("description", UNSET)

        pick_dashboard_name_or_description_or_updated_at_or_filters_or_tabs_or_slug = cls(
            name=name,
            slug=slug,
            updated_at=updated_at,
            filters=filters,
            tabs=tabs,
            description=description,
        )

        pick_dashboard_name_or_description_or_updated_at_or_filters_or_tabs_or_slug.additional_properties = d
        return pick_dashboard_name_or_description_or_updated_at_or_filters_or_tabs_or_slug

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
