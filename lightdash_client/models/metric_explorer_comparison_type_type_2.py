from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metric_explorer_comparison_differentmetric import MetricExplorerComparisonDIFFERENTMETRIC
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricExplorerComparisonTypeType2")


@_attrs_define
class MetricExplorerComparisonTypeType2:
    """
    Attributes:
        metric_name (str):
        metric_table (str):
        type (MetricExplorerComparisonDIFFERENTMETRIC):
    """

    metric_name: str
    metric_table: str
    type: MetricExplorerComparisonDIFFERENTMETRIC
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metric_name = self.metric_name

        metric_table = self.metric_table

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metricName": metric_name,
                "metricTable": metric_table,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metric_name = d.pop("metricName")

        metric_table = d.pop("metricTable")

        type = MetricExplorerComparisonDIFFERENTMETRIC(d.pop("type"))

        metric_explorer_comparison_type_type_2 = cls(
            metric_name=metric_name,
            metric_table=metric_table,
            type=type,
        )

        metric_explorer_comparison_type_type_2.additional_properties = d
        return metric_explorer_comparison_type_type_2

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
