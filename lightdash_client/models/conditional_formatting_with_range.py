from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConditionalFormattingWithRange")


@_attrs_define
class ConditionalFormattingWithRange:
    """
    Attributes:
        max_ (float):
        min_ (float):
    """

    max_: float
    min_: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_ = self.max_

        min_ = self.min_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max": max_,
                "min": min_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_ = d.pop("max")

        min_ = d.pop("min")

        conditional_formatting_with_range = cls(
            max_=max_,
            min_=min_,
        )

        conditional_formatting_with_range.additional_properties = d
        return conditional_formatting_with_range

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
