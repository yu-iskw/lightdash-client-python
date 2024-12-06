from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_frames import TimeFrames
from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultTimeDimension")


@_attrs_define
class DefaultTimeDimension:
    """
    Attributes:
        interval (TimeFrames):
        field (str):
    """

    interval: TimeFrames
    field: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interval = self.interval.value

        field = self.field

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval": interval,
                "field": field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interval = TimeFrames(d.pop("interval"))

        field = d.pop("field")

        default_time_dimension = cls(
            interval=interval,
            field=field,
        )

        default_time_dimension.additional_properties = d
        return default_time_dimension

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
