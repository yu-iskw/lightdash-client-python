import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_tab import DashboardTab


T = TypeVar("T", bound="PickDashboardAsCodeExcludeKeyofDashboardAsCodeFiltersOrTilesOrDescription")


@_attrs_define
class PickDashboardAsCodeExcludeKeyofDashboardAsCodeFiltersOrTilesOrDescription:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        slug (str):
        updated_at (datetime.datetime):
        tabs (List['DashboardTab']):
        version (float):
        space_slug (str):
        downloaded_at (Union[Unset, datetime.datetime]):
    """

    name: str
    slug: str
    updated_at: datetime.datetime
    tabs: List["DashboardTab"]
    version: float
    space_slug: str
    downloaded_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_tab import DashboardTab

        name = self.name

        slug = self.slug

        updated_at = self.updated_at.isoformat()

        tabs = []
        for tabs_item_data in self.tabs:
            tabs_item = tabs_item_data.to_dict()
            tabs.append(tabs_item)

        version = self.version

        space_slug = self.space_slug

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
                "tabs": tabs,
                "version": version,
                "spaceSlug": space_slug,
            }
        )
        if downloaded_at is not UNSET:
            field_dict["downloadedAt"] = downloaded_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_tab import DashboardTab

        d = src_dict.copy()
        name = d.pop("name")

        slug = d.pop("slug")

        updated_at = isoparse(d.pop("updatedAt"))

        tabs = []
        _tabs = d.pop("tabs")
        for tabs_item_data in _tabs:
            tabs_item = DashboardTab.from_dict(tabs_item_data)

            tabs.append(tabs_item)

        version = d.pop("version")

        space_slug = d.pop("spaceSlug")

        _downloaded_at = d.pop("downloadedAt", UNSET)
        downloaded_at: Union[Unset, datetime.datetime]
        if isinstance(_downloaded_at, Unset):
            downloaded_at = UNSET
        else:
            downloaded_at = isoparse(_downloaded_at)

        pick_dashboard_as_code_exclude_keyof_dashboard_as_code_filters_or_tiles_or_description = cls(
            name=name,
            slug=slug,
            updated_at=updated_at,
            tabs=tabs,
            version=version,
            space_slug=space_slug,
            downloaded_at=downloaded_at,
        )

        pick_dashboard_as_code_exclude_keyof_dashboard_as_code_filters_or_tiles_or_description.additional_properties = d
        return pick_dashboard_as_code_exclude_keyof_dashboard_as_code_filters_or_tiles_or_description

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
