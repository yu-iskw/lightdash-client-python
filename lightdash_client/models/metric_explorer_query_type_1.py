from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metric_explorer_comparison_previousperiod import MetricExplorerComparisonPREVIOUSPERIOD
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricExplorerQueryType1")


@_attrs_define
class MetricExplorerQueryType1:
    """
    Attributes:
        comparison (MetricExplorerComparisonPREVIOUSPERIOD):
    """

    comparison: MetricExplorerComparisonPREVIOUSPERIOD
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comparison = self.comparison.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comparison": comparison,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        comparison = MetricExplorerComparisonPREVIOUSPERIOD(d.pop("comparison"))

        metric_explorer_query_type_1 = cls(
            comparison=comparison,
        )

        metric_explorer_query_type_1.additional_properties = d
        return metric_explorer_query_type_1

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
