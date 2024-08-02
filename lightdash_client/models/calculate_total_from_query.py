from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metric_query_request import MetricQueryRequest


T = TypeVar("T", bound="CalculateTotalFromQuery")


@_attrs_define
class CalculateTotalFromQuery:
    """
    Attributes:
        explore (str):
        metric_query (MetricQueryRequest):
    """

    explore: str
    metric_query: "MetricQueryRequest"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        explore = self.explore

        metric_query = self.metric_query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "explore": explore,
                "metricQuery": metric_query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metric_query_request import MetricQueryRequest

        d = src_dict.copy()
        explore = d.pop("explore")

        metric_query = MetricQueryRequest.from_dict(d.pop("metricQuery"))

        calculate_total_from_query = cls(
            explore=explore,
            metric_query=metric_query,
        )

        calculate_total_from_query.additional_properties = d
        return calculate_total_from_query

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
