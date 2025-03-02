from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardTileAsCodePropertiesType2")


@_attrs_define
class DashboardTileAsCodePropertiesType2:
    """
    Attributes:
        url (str):
        title (str):
        hide_title (Union[Unset, bool]):
    """

    url: str
    title: str
    hide_title: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        title = self.title

        hide_title = self.hide_title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "title": title,
            }
        )
        if hide_title is not UNSET:
            field_dict["hideTitle"] = hide_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        title = d.pop("title")

        hide_title = d.pop("hideTitle", UNSET)

        dashboard_tile_as_code_properties_type_2 = cls(
            url=url,
            title=title,
            hide_title=hide_title,
        )

        dashboard_tile_as_code_properties_type_2.additional_properties = d
        return dashboard_tile_as_code_properties_type_2

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
