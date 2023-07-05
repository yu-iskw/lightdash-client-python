from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.post_chart_results_response_200_results_metric_query_additional_metrics_item_filters_item_operator import (
    PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_chart_results_response_200_results_metric_query_additional_metrics_item_filters_item_target import (
        PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget,
    )


T = TypeVar("T", bound="PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem")


@attr.s(auto_attribs=True)
class PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem:
    """
    Attributes:
        operator (PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator):
        id (str):
        target (PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget):
        values (Union[Unset, List[Any]]):
        settings (Union[Unset, Any]):
    """

    operator: PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator
    id: str
    target: "PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget"
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
        from ..models.post_chart_results_response_200_results_metric_query_additional_metrics_item_filters_item_target import (
            PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget,
        )

        d = src_dict.copy()
        operator = PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator(
            d.pop("operator")
        )

        id = d.pop("id")

        target = PostChartResultsResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget.from_dict(
            d.pop("target")
        )

        values = cast(List[Any], d.pop("values", UNSET))

        settings = d.pop("settings", UNSET)

        post_chart_results_response_200_results_metric_query_additional_metrics_item_filters_item = cls(
            operator=operator,
            id=id,
            target=target,
            values=values,
            settings=settings,
        )

        return post_chart_results_response_200_results_metric_query_additional_metrics_item_filters_item
