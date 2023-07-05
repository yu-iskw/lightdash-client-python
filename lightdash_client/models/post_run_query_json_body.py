from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_run_query_json_body_additional_metrics_item import (
        PostRunQueryJsonBodyAdditionalMetricsItem,
    )
    from ..models.post_run_query_json_body_filters import PostRunQueryJsonBodyFilters
    from ..models.post_run_query_json_body_sorts_item import (
        PostRunQueryJsonBodySortsItem,
    )
    from ..models.post_run_query_json_body_table_calculations_item import (
        PostRunQueryJsonBodyTableCalculationsItem,
    )


T = TypeVar("T", bound="PostRunQueryJsonBody")


@attr.s(auto_attribs=True)
class PostRunQueryJsonBody:
    """metricQuery for the chart to run

    Attributes:
        table_calculations (List['PostRunQueryJsonBodyTableCalculationsItem']):
        limit (float):
        sorts (List['PostRunQueryJsonBodySortsItem']):
        filters (PostRunQueryJsonBodyFilters):
        metrics (List[str]):
        dimensions (List[str]):
        csv_limit (Union[Unset, float]):
        additional_metrics (Union[Unset, List['PostRunQueryJsonBodyAdditionalMetricsItem']]):
    """

    table_calculations: List["PostRunQueryJsonBodyTableCalculationsItem"]
    limit: float
    sorts: List["PostRunQueryJsonBodySortsItem"]
    filters: "PostRunQueryJsonBodyFilters"
    metrics: List[str]
    dimensions: List[str]
    csv_limit: Union[Unset, float] = UNSET
    additional_metrics: Union[Unset, List["PostRunQueryJsonBodyAdditionalMetricsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_calculations = []
        for table_calculations_item_data in self.table_calculations:
            table_calculations_item = table_calculations_item_data.to_dict()

            table_calculations.append(table_calculations_item)

        limit = self.limit
        sorts = []
        for sorts_item_data in self.sorts:
            sorts_item = sorts_item_data.to_dict()

            sorts.append(sorts_item)

        filters = self.filters.to_dict()

        metrics = self.metrics

        dimensions = self.dimensions

        csv_limit = self.csv_limit
        additional_metrics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_metrics, Unset):
            additional_metrics = []
            for additional_metrics_item_data in self.additional_metrics:
                additional_metrics_item = additional_metrics_item_data.to_dict()

                additional_metrics.append(additional_metrics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableCalculations": table_calculations,
                "limit": limit,
                "sorts": sorts,
                "filters": filters,
                "metrics": metrics,
                "dimensions": dimensions,
            }
        )
        if csv_limit is not UNSET:
            field_dict["csvLimit"] = csv_limit
        if additional_metrics is not UNSET:
            field_dict["additionalMetrics"] = additional_metrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_run_query_json_body_additional_metrics_item import (
            PostRunQueryJsonBodyAdditionalMetricsItem,
        )
        from ..models.post_run_query_json_body_filters import (
            PostRunQueryJsonBodyFilters,
        )
        from ..models.post_run_query_json_body_sorts_item import (
            PostRunQueryJsonBodySortsItem,
        )
        from ..models.post_run_query_json_body_table_calculations_item import (
            PostRunQueryJsonBodyTableCalculationsItem,
        )

        d = src_dict.copy()
        table_calculations = []
        _table_calculations = d.pop("tableCalculations")
        for table_calculations_item_data in _table_calculations:
            table_calculations_item = PostRunQueryJsonBodyTableCalculationsItem.from_dict(table_calculations_item_data)

            table_calculations.append(table_calculations_item)

        limit = d.pop("limit")

        sorts = []
        _sorts = d.pop("sorts")
        for sorts_item_data in _sorts:
            sorts_item = PostRunQueryJsonBodySortsItem.from_dict(sorts_item_data)

            sorts.append(sorts_item)

        filters = PostRunQueryJsonBodyFilters.from_dict(d.pop("filters"))

        metrics = cast(List[str], d.pop("metrics"))

        dimensions = cast(List[str], d.pop("dimensions"))

        csv_limit = d.pop("csvLimit", UNSET)

        additional_metrics = []
        _additional_metrics = d.pop("additionalMetrics", UNSET)
        for additional_metrics_item_data in _additional_metrics or []:
            additional_metrics_item = PostRunQueryJsonBodyAdditionalMetricsItem.from_dict(additional_metrics_item_data)

            additional_metrics.append(additional_metrics_item)

        post_run_query_json_body = cls(
            table_calculations=table_calculations,
            limit=limit,
            sorts=sorts,
            filters=filters,
            metrics=metrics,
            dimensions=dimensions,
            csv_limit=csv_limit,
            additional_metrics=additional_metrics,
        )

        post_run_query_json_body.additional_properties = d
        return post_run_query_json_body

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
