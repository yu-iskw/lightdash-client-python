from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mark_line_data_label_position import MarkLineDataLabelPosition
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkLineDataLabel")


@_attrs_define
class MarkLineDataLabel:
    """
    Attributes:
        position (Union[Unset, MarkLineDataLabelPosition]):
        formatter (Union[Unset, str]):
    """

    position: Union[Unset, MarkLineDataLabelPosition] = UNSET
    formatter: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position: Union[Unset, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value

        formatter = self.formatter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if formatter is not UNSET:
            field_dict["formatter"] = formatter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _position = d.pop("position", UNSET)
        position: Union[Unset, MarkLineDataLabelPosition]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = MarkLineDataLabelPosition(_position)

        formatter = d.pop("formatter", UNSET)

        mark_line_data_label = cls(
            position=position,
            formatter=formatter,
        )

        mark_line_data_label.additional_properties = d
        return mark_line_data_label

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
