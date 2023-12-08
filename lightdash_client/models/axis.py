from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Axis")


@attr.s(auto_attribs=True)
class Axis:
    """
    Attributes:
        inverse (Union[Unset, bool]):
        max_ (Union[Unset, str]):
        min_ (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    inverse: Union[Unset, bool] = UNSET
    max_: Union[Unset, str] = UNSET
    min_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inverse = self.inverse
        max_ = self.max_
        min_ = self.min_
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inverse is not UNSET:
            field_dict["inverse"] = inverse
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
        inverse = d.pop("inverse", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        name = d.pop("name", UNSET)

        axis = cls(
            inverse=inverse,
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
