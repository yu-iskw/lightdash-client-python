from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..models.post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_filters_item_operator import (
    PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator,
)
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_filters_item_target import (
        PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget,
    )


T = TypeVar("T", bound="PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem")


@attr.s(auto_attribs=True)
class PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem:
    """
    Attributes:
        operator (PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator):
        id (str):
        target (PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget):
        values (Union[Unset, List[Any]]):
        settings (Union[Unset, Any]):
    """

    operator: PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator
    id: str
    target: "PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget"
    values: Union[Unset, List[Any]] = UNSET
    settings: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        operator = self.operator.value

        id = self.id
        target = self.target.to_dict()

        values: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        settings = self.settings

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "operator": operator,
                "id": id,
                "target": target,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_filters_item_target import (
            PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget,
        )

        d = src_dict.copy()
        operator = PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator(
            d.pop("operator")
        )

        id = d.pop("id")

        target = (
            PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget.from_dict(
                d.pop("target")
            )
        )

        values = cast(List[Any], d.pop("values", UNSET))

        settings = d.pop("settings", UNSET)

        post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_filters_item = cls(
            operator=operator,
            id=id,
            target=target,
            values=values,
            settings=settings,
        )

        return post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_filters_item
