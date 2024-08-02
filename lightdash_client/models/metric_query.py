from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_metric import AdditionalMetric
    from ..models.custom_bin_dimension import CustomBinDimension
    from ..models.custom_sql_dimension import CustomSqlDimension
    from ..models.filters import Filters
    from ..models.metric_query_metadata import MetricQueryMetadata
    from ..models.sort_field import SortField
    from ..models.table_calculation import TableCalculation


T = TypeVar("T", bound="MetricQuery")


@_attrs_define
class MetricQuery:
    """
    Attributes:
        table_calculations (List['TableCalculation']):
        limit (float):
        sorts (List['SortField']):
        filters (Filters):
        metrics (List[str]):
        dimensions (List[str]):
        explore_name (str):
        metadata (Union[Unset, MetricQueryMetadata]):
        timezone (Union[Unset, str]):
        custom_dimensions (Union[Unset, List[Union['CustomBinDimension', 'CustomSqlDimension']]]):
        additional_metrics (Union[Unset, List['AdditionalMetric']]):
    """

    table_calculations: List["TableCalculation"]
    limit: float
    sorts: List["SortField"]
    filters: "Filters"
    metrics: List[str]
    dimensions: List[str]
    explore_name: str
    metadata: Union[Unset, "MetricQueryMetadata"] = UNSET
    timezone: Union[Unset, str] = UNSET
    custom_dimensions: Union[Unset, List[Union["CustomBinDimension", "CustomSqlDimension"]]] = UNSET
    additional_metrics: Union[Unset, List["AdditionalMetric"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.custom_bin_dimension import CustomBinDimension

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

        explore_name = self.explore_name

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        timezone = self.timezone

        custom_dimensions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_dimensions, Unset):
            custom_dimensions = []
            for custom_dimensions_item_data in self.custom_dimensions:
                custom_dimensions_item: Dict[str, Any]
                if isinstance(custom_dimensions_item_data, CustomBinDimension):
                    custom_dimensions_item = custom_dimensions_item_data.to_dict()
                else:
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
                "exploreName": explore_name,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if custom_dimensions is not UNSET:
            field_dict["customDimensions"] = custom_dimensions
        if additional_metrics is not UNSET:
            field_dict["additionalMetrics"] = additional_metrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_metric import AdditionalMetric
        from ..models.custom_bin_dimension import CustomBinDimension
        from ..models.custom_sql_dimension import CustomSqlDimension
        from ..models.filters import Filters
        from ..models.metric_query_metadata import MetricQueryMetadata
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

        filters = Filters.from_dict(d.pop("filters"))

        metrics = cast(List[str], d.pop("metrics"))

        dimensions = cast(List[str], d.pop("dimensions"))

        explore_name = d.pop("exploreName")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, MetricQueryMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = MetricQueryMetadata.from_dict(_metadata)

        timezone = d.pop("timezone", UNSET)

        custom_dimensions = []
        _custom_dimensions = d.pop("customDimensions", UNSET)
        for custom_dimensions_item_data in _custom_dimensions or []:

            def _parse_custom_dimensions_item(data: object) -> Union["CustomBinDimension", "CustomSqlDimension"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_custom_dimension_type_0 = CustomBinDimension.from_dict(data)

                    return componentsschemas_custom_dimension_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_custom_dimension_type_1 = CustomSqlDimension.from_dict(data)

                return componentsschemas_custom_dimension_type_1

            custom_dimensions_item = _parse_custom_dimensions_item(custom_dimensions_item_data)

            custom_dimensions.append(custom_dimensions_item)

        additional_metrics = []
        _additional_metrics = d.pop("additionalMetrics", UNSET)
        for additional_metrics_item_data in _additional_metrics or []:
            additional_metrics_item = AdditionalMetric.from_dict(additional_metrics_item_data)

            additional_metrics.append(additional_metrics_item)

        metric_query = cls(
            table_calculations=table_calculations,
            limit=limit,
            sorts=sorts,
            filters=filters,
            metrics=metrics,
            dimensions=dimensions,
            explore_name=explore_name,
            metadata=metadata,
            timezone=timezone,
            custom_dimensions=custom_dimensions,
            additional_metrics=additional_metrics,
        )

        metric_query.additional_properties = d
        return metric_query

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
