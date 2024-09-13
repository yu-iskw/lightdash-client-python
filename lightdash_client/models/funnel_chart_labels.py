from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.funnel_chart_label_position import FunnelChartLabelPosition
from ..types import UNSET, Unset

T = TypeVar("T", bound="FunnelChartLabels")


@_attrs_define
class FunnelChartLabels:
    """
    Attributes:
        show_percentage (Union[Unset, bool]):
        show_value (Union[Unset, bool]):
        position (Union[Unset, FunnelChartLabelPosition]):
    """

    show_percentage: Union[Unset, bool] = UNSET
    show_value: Union[Unset, bool] = UNSET
    position: Union[Unset, FunnelChartLabelPosition] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        show_percentage = self.show_percentage

        show_value = self.show_value

        position: Union[Unset, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if show_percentage is not UNSET:
            field_dict["showPercentage"] = show_percentage
        if show_value is not UNSET:
            field_dict["showValue"] = show_value
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        show_percentage = d.pop("showPercentage", UNSET)

        show_value = d.pop("showValue", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, FunnelChartLabelPosition]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = FunnelChartLabelPosition(_position)

        funnel_chart_labels = cls(
            show_percentage=show_percentage,
            show_value=show_value,
            position=position,
        )

        funnel_chart_labels.additional_properties = d
        return funnel_chart_labels

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
