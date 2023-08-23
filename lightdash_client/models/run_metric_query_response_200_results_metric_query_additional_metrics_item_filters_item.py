from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.run_metric_query_response_200_results_metric_query_additional_metrics_item_filters_item_operator import (
    RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_metric_query_response_200_results_metric_query_additional_metrics_item_filters_item_target import (
        RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget,
    )


T = TypeVar("T", bound="RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem")


@attr.s(auto_attribs=True)
class RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem:
    """
    Attributes:
        operator (RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator):
        id (str):
        target (RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget):
        values (Union[Unset, List[Any]]):
        settings (Union[Unset, Any]):
        disabled (Union[Unset, bool]):
    """

    operator: RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator
    id: str
    target: "RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget"
    values: Union[Unset, List[Any]] = UNSET
    settings: Union[Unset, Any] = UNSET
    disabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        operator = self.operator.value

        id = self.id
        target = self.target.to_dict()

        values: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        settings = self.settings
        disabled = self.disabled

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
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.run_metric_query_response_200_results_metric_query_additional_metrics_item_filters_item_target import (
            RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget,
        )

        d = src_dict.copy()
        operator = RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemOperator(
            d.pop("operator")
        )

        id = d.pop("id")

        target = RunMetricQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItemTarget.from_dict(
            d.pop("target")
        )

        values = cast(List[Any], d.pop("values", UNSET))

        settings = d.pop("settings", UNSET)

        disabled = d.pop("disabled", UNSET)

        run_metric_query_response_200_results_metric_query_additional_metrics_item_filters_item = cls(
            operator=operator,
            id=id,
            target=target,
            values=values,
            settings=settings,
            disabled=disabled,
        )

        return run_metric_query_response_200_results_metric_query_additional_metrics_item_filters_item
