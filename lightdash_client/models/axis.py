from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Axis")


@_attrs_define
class Axis:
    """
    Attributes:
        rotate (Union[Unset, float]):
        inverse (Union[Unset, bool]):
        max_offset (Union[Unset, str]):
        min_offset (Union[Unset, str]):
        max_ (Union[Unset, str]):
        min_ (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    rotate: Union[Unset, float] = UNSET
    inverse: Union[Unset, bool] = UNSET
    max_offset: Union[Unset, str] = UNSET
    min_offset: Union[Unset, str] = UNSET
    max_: Union[Unset, str] = UNSET
    min_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rotate = self.rotate

        inverse = self.inverse

        max_offset = self.max_offset

        min_offset = self.min_offset

        max_ = self.max_

        min_ = self.min_

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rotate is not UNSET:
            field_dict["rotate"] = rotate
        if inverse is not UNSET:
            field_dict["inverse"] = inverse
        if max_offset is not UNSET:
            field_dict["maxOffset"] = max_offset
        if min_offset is not UNSET:
            field_dict["minOffset"] = min_offset
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rotate = d.pop("rotate", UNSET)

        inverse = d.pop("inverse", UNSET)

        max_offset = d.pop("maxOffset", UNSET)

        min_offset = d.pop("minOffset", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        name = d.pop("name", UNSET)

        axis = cls(
            rotate=rotate,
            inverse=inverse,
            max_offset=max_offset,
            min_offset=min_offset,
            max_=max_,
            min_=min_,
            name=name,
        )

        axis.additional_properties = d
        return axis

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
