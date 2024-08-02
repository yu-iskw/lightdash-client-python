from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.series_label_position import SeriesLabelPosition
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeriesLabel")


@_attrs_define
class SeriesLabel:
    """
    Attributes:
        position (Union[Unset, SeriesLabelPosition]):
        show (Union[Unset, bool]):
    """

    position: Union[Unset, SeriesLabelPosition] = UNSET
    show: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position: Union[Unset, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value

        show = self.show

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if show is not UNSET:
            field_dict["show"] = show

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _position = d.pop("position", UNSET)
        position: Union[Unset, SeriesLabelPosition]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = SeriesLabelPosition(_position)

        show = d.pop("show", UNSET)

        series_label = cls(
            position=position,
            show=show,
        )

        series_label.additional_properties = d
        return series_label

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
