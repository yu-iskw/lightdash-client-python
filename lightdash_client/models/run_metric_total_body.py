from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metric_total_comparison_type import MetricTotalComparisonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunMetricTotalBody")


@_attrs_define
class RunMetricTotalBody:
    """
    Attributes:
        comparison_type (Union[Unset, MetricTotalComparisonType]):
    """

    comparison_type: Union[Unset, MetricTotalComparisonType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comparison_type: Union[Unset, str] = UNSET
        if not isinstance(self.comparison_type, Unset):
            comparison_type = self.comparison_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comparison_type is not UNSET:
            field_dict["comparisonType"] = comparison_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _comparison_type = d.pop("comparisonType", UNSET)
        comparison_type: Union[Unset, MetricTotalComparisonType]
        if isinstance(_comparison_type, Unset):
            comparison_type = UNSET
        else:
            comparison_type = MetricTotalComparisonType(_comparison_type)

        run_metric_total_body = cls(
            comparison_type=comparison_type,
        )

        run_metric_total_body.additional_properties = d
        return run_metric_total_body

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
