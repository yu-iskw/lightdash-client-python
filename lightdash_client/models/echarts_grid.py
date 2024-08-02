from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EchartsGrid")


@_attrs_define
class EchartsGrid:
    """
    Attributes:
        height (Union[Unset, str]):
        width (Union[Unset, str]):
        left (Union[Unset, str]):
        bottom (Union[Unset, str]):
        right (Union[Unset, str]):
        top (Union[Unset, str]):
        contain_label (Union[Unset, bool]):
    """

    height: Union[Unset, str] = UNSET
    width: Union[Unset, str] = UNSET
    left: Union[Unset, str] = UNSET
    bottom: Union[Unset, str] = UNSET
    right: Union[Unset, str] = UNSET
    top: Union[Unset, str] = UNSET
    contain_label: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        height = self.height

        width = self.width

        left = self.left

        bottom = self.bottom

        right = self.right

        top = self.top

        contain_label = self.contain_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if left is not UNSET:
            field_dict["left"] = left
        if bottom is not UNSET:
            field_dict["bottom"] = bottom
        if right is not UNSET:
            field_dict["right"] = right
        if top is not UNSET:
            field_dict["top"] = top
        if contain_label is not UNSET:
            field_dict["containLabel"] = contain_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        left = d.pop("left", UNSET)

        bottom = d.pop("bottom", UNSET)

        right = d.pop("right", UNSET)

        top = d.pop("top", UNSET)

        contain_label = d.pop("containLabel", UNSET)

        echarts_grid = cls(
            height=height,
            width=width,
            left=left,
            bottom=bottom,
            right=right,
            top=top,
            contain_label=contain_label,
        )

        echarts_grid.additional_properties = d
        return echarts_grid

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
