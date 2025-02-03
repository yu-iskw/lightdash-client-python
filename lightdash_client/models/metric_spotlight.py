from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metric_spotlight_visibility import MetricSpotlightVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricSpotlight")


@_attrs_define
class MetricSpotlight:
    """
    Attributes:
        visibility (MetricSpotlightVisibility):
        categories (Union[Unset, List[str]]):
    """

    visibility: MetricSpotlightVisibility
    categories: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        visibility = self.visibility.value

        categories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
            }
        )
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        visibility = MetricSpotlightVisibility(d.pop("visibility"))

        categories = cast(List[str], d.pop("categories", UNSET))

        metric_spotlight = cls(
            visibility=visibility,
            categories=categories,
        )

        metric_spotlight.additional_properties = d
        return metric_spotlight

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
