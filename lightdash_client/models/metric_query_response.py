from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_metric import AdditionalMetric
    from ..models.custom_dimension import CustomDimension
    from ..models.filters_response import FiltersResponse
    from ..models.metric_query_response_metadata import MetricQueryResponseMetadata
    from ..models.sort_field import SortField
    from ..models.table_calculation import TableCalculation


T = TypeVar("T", bound="MetricQueryResponse")


@attr.s(auto_attribs=True)
class MetricQueryResponse:
    """
    Attributes:
        table_calculations (List['TableCalculation']):
        limit (float):
        sorts (List['SortField']):
        filters (FiltersResponse):
        metrics (List[str]):
        dimensions (List[str]):
        metadata (Union[Unset, MetricQueryResponseMetadata]):
        custom_dimensions (Union[Unset, List['CustomDimension']]):
        additional_metrics (Union[Unset, List['AdditionalMetric']]):
    """

    table_calculations: List["TableCalculation"]
    limit: float
    sorts: List["SortField"]
    filters: "FiltersResponse"
    metrics: List[str]
    dimensions: List[str]
    metadata: Union[Unset, "MetricQueryResponseMetadata"] = UNSET
    custom_dimensions: Union[Unset, List["CustomDimension"]] = UNSET
    additional_metrics: Union[Unset, List["AdditionalMetric"]] = UNSET
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

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        custom_dimensions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_dimensions, Unset):
            custom_dimensions = []
            for custom_dimensions_item_data in self.custom_dimensions:
                custom_dimensions_item = custom_dimensions_item_data.to_dict()

                custom_dimensions.append(custom_dimensions_item)

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
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if custom_dimensions is not UNSET:
            field_dict["customDimensions"] = custom_dimensions
        if additional_metrics is not UNSET:
            field_dict["additionalMetrics"] = additional_metrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_metric import AdditionalMetric
        from ..models.custom_dimension import CustomDimension
        from ..models.filters_response import FiltersResponse
        from ..models.metric_query_response_metadata import MetricQueryResponseMetadata
        from ..models.sort_field import SortField
        from ..models.table_calculation import TableCalculation

        d = src_dict.copy()
        table_calculations = []
        _table_calculations = d.pop("tableCalculations")
        for table_calculations_item_data in _table_calculations:
            table_calculations_item = TableCalculation.from_dict(table_calculations_item_data)

            table_calculations.append(table_calculations_item)

        limit = d.pop("limit")

        sorts = []
        _sorts = d.pop("sorts")
        for sorts_item_data in _sorts:
            sorts_item = SortField.from_dict(sorts_item_data)

            sorts.append(sorts_item)

        filters = FiltersResponse.from_dict(d.pop("filters"))

        metrics = cast(List[str], d.pop("metrics"))

        dimensions = cast(List[str], d.pop("dimensions"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, MetricQueryResponseMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = MetricQueryResponseMetadata.from_dict(_metadata)

        custom_dimensions = []
        _custom_dimensions = d.pop("customDimensions", UNSET)
        for custom_dimensions_item_data in _custom_dimensions or []:
            custom_dimensions_item = CustomDimension.from_dict(custom_dimensions_item_data)

            custom_dimensions.append(custom_dimensions_item)

        additional_metrics = []
        _additional_metrics = d.pop("additionalMetrics", UNSET)
        for additional_metrics_item_data in _additional_metrics or []:
            additional_metrics_item = AdditionalMetric.from_dict(additional_metrics_item_data)

            additional_metrics.append(additional_metrics_item)

        metric_query_response = cls(
            table_calculations=table_calculations,
            limit=limit,
            sorts=sorts,
            filters=filters,
            metrics=metrics,
            dimensions=dimensions,
            metadata=metadata,
            custom_dimensions=custom_dimensions,
            additional_metrics=additional_metrics,
        )

        metric_query_response.additional_properties = d
        return metric_query_response

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
