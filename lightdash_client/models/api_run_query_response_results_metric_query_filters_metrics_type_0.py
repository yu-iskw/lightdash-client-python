from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0")


@attr.s(auto_attribs=True)
class ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0:
    """
    Attributes:
        or_ (List[Any]):
        id (str):
    """

    or_: List[Any]
    id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        or_ = self.or_

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "or": or_,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        or_ = cast(List[Any], d.pop("or"))

        id = d.pop("id")

        api_run_query_response_results_metric_query_filters_metrics_type_0 = cls(
            or_=or_,
            id=id,
        )

        api_run_query_response_results_metric_query_filters_metrics_type_0.additional_properties = d
        return api_run_query_response_results_metric_query_filters_metrics_type_0

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
