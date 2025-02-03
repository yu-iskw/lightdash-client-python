from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metric_explorer_comparison_none import MetricExplorerComparisonNONE
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricExplorerQueryType0")


@_attrs_define
class MetricExplorerQueryType0:
    """
    Attributes:
        segment_dimension (Union[None, str]):
        comparison (MetricExplorerComparisonNONE):
    """

    segment_dimension: Union[None, str]
    comparison: MetricExplorerComparisonNONE
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        segment_dimension: Union[None, str]
        segment_dimension = self.segment_dimension

        comparison = self.comparison.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segmentDimension": segment_dimension,
                "comparison": comparison,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_segment_dimension(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        segment_dimension = _parse_segment_dimension(d.pop("segmentDimension"))

        comparison = MetricExplorerComparisonNONE(d.pop("comparison"))

        metric_explorer_query_type_0 = cls(
            segment_dimension=segment_dimension,
            comparison=comparison,
        )

        metric_explorer_query_type_0.additional_properties = d
        return metric_explorer_query_type_0

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
