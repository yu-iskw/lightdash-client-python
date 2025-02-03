from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format import CustomFormat


T = TypeVar("T", bound="PickMetricFormatOptions")


@_attrs_define
class PickMetricFormatOptions:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        format_options (Union[Unset, CustomFormat]):
    """

    format_options: Union[Unset, "CustomFormat"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.custom_format import CustomFormat

        format_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_options, Unset):
            format_options = self.format_options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_options is not UNSET:
            field_dict["formatOptions"] = format_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_format import CustomFormat

        d = src_dict.copy()
        _format_options = d.pop("formatOptions", UNSET)
        format_options: Union[Unset, CustomFormat]
        if isinstance(_format_options, Unset):
            format_options = UNSET
        else:
            format_options = CustomFormat.from_dict(_format_options)

        pick_metric_format_options = cls(
            format_options=format_options,
        )

        pick_metric_format_options.additional_properties = d
        return pick_metric_format_options

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
