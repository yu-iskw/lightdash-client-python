from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

import attr

if TYPE_CHECKING:
    from ..models.post_run_underlying_data_query_response_200_results_metric_query import (
        PostRunUnderlyingDataQueryResponse200ResultsMetricQuery,
    )


T = TypeVar("T", bound="PostRunUnderlyingDataQueryResponse200Results")


@attr.s(auto_attribs=True)
class PostRunUnderlyingDataQueryResponse200Results:
    """
    Attributes:
        rows (List[Any]):
        metric_query (PostRunUnderlyingDataQueryResponse200ResultsMetricQuery):
    """

    rows: List[Any]
    metric_query: "PostRunUnderlyingDataQueryResponse200ResultsMetricQuery"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rows = self.rows

        metric_query = self.metric_query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
                "metricQuery": metric_query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_run_underlying_data_query_response_200_results_metric_query import (
            PostRunUnderlyingDataQueryResponse200ResultsMetricQuery,
        )

        d = src_dict.copy()
        rows = cast(List[Any], d.pop("rows"))

        metric_query = PostRunUnderlyingDataQueryResponse200ResultsMetricQuery.from_dict(d.pop("metricQuery"))

        post_run_underlying_data_query_response_200_results = cls(
            rows=rows,
            metric_query=metric_query,
        )

        post_run_underlying_data_query_response_200_results.additional_properties = d
        return post_run_underlying_data_query_response_200_results

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
