from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

import attr

if TYPE_CHECKING:
    from ..models.metric_query_response import MetricQueryResponse


T = TypeVar("T", bound="ApiRunQueryResponseResults")


@attr.s(auto_attribs=True)
class ApiRunQueryResponseResults:
    """
    Attributes:
        rows (List[Any]):
        metric_query (MetricQueryResponse):
    """

    rows: List[Any]
    metric_query: "MetricQueryResponse"
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
        from ..models.metric_query_response import MetricQueryResponse

        d = src_dict.copy()
        rows = cast(List[Any], d.pop("rows"))

        metric_query = MetricQueryResponse.from_dict(d.pop("metricQuery"))

        api_run_query_response_results = cls(
            rows=rows,
            metric_query=metric_query,
        )

        api_run_query_response_results.additional_properties = d
        return api_run_query_response_results

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
