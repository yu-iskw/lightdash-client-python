from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricQueryRequestFilters")


@_attrs_define
class MetricQueryRequestFilters:
    """
    Attributes:
        table_calculations (Union[Unset, Any]):
        metrics (Union[Unset, Any]):
        dimensions (Union[Unset, Any]):
    """

    table_calculations: Union[Unset, Any] = UNSET
    metrics: Union[Unset, Any] = UNSET
    dimensions: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_calculations = self.table_calculations

        metrics = self.metrics

        dimensions = self.dimensions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if table_calculations is not UNSET:
            field_dict["tableCalculations"] = table_calculations
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_calculations = d.pop("tableCalculations", UNSET)

        metrics = d.pop("metrics", UNSET)

        dimensions = d.pop("dimensions", UNSET)

        metric_query_request_filters = cls(
            table_calculations=table_calculations,
            metrics=metrics,
            dimensions=dimensions,
        )

        metric_query_request_filters.additional_properties = d
        return metric_query_request_filters

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
