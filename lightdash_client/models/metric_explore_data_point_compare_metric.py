from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricExploreDataPointCompareMetric")


@_attrs_define
class MetricExploreDataPointCompareMetric:
    """
    Attributes:
        label (Union[None, str]):
        value (Union[None, float]):
    """

    label: Union[None, str]
    value: Union[None, float]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label: Union[None, str]
        label = self.label

        value: Union[None, float]
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_label(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        label = _parse_label(d.pop("label"))

        def _parse_value(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        value = _parse_value(d.pop("value"))

        metric_explore_data_point_compare_metric = cls(
            label=label,
            value=value,
        )

        metric_explore_data_point_compare_metric.additional_properties = d
        return metric_explore_data_point_compare_metric

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
