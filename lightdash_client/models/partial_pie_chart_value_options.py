from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partial_pie_chart_value_options_value_label import PartialPieChartValueOptionsValueLabel
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialPieChartValueOptions")


@_attrs_define
class PartialPieChartValueOptions:
    """Make all properties in T optional

    Attributes:
        value_label (Union[Unset, PartialPieChartValueOptionsValueLabel]):
        show_value (Union[Unset, bool]):
        show_percentage (Union[Unset, bool]):
    """

    value_label: Union[Unset, PartialPieChartValueOptionsValueLabel] = UNSET
    show_value: Union[Unset, bool] = UNSET
    show_percentage: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value_label: Union[Unset, str] = UNSET
        if not isinstance(self.value_label, Unset):
            value_label = self.value_label.value

        show_value = self.show_value

        show_percentage = self.show_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_label is not UNSET:
            field_dict["valueLabel"] = value_label
        if show_value is not UNSET:
            field_dict["showValue"] = show_value
        if show_percentage is not UNSET:
            field_dict["showPercentage"] = show_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _value_label = d.pop("valueLabel", UNSET)
        value_label: Union[Unset, PartialPieChartValueOptionsValueLabel]
        if isinstance(_value_label, Unset):
            value_label = UNSET
        else:
            value_label = PartialPieChartValueOptionsValueLabel(_value_label)

        show_value = d.pop("showValue", UNSET)

        show_percentage = d.pop("showPercentage", UNSET)

        partial_pie_chart_value_options = cls(
            value_label=value_label,
            show_value=show_value,
            show_percentage=show_percentage,
        )

        partial_pie_chart_value_options.additional_properties = d
        return partial_pie_chart_value_options

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
