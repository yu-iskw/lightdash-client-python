from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_metric import AdditionalMetric
    from ..models.custom_bin_dimension import CustomBinDimension
    from ..models.custom_sql_dimension import CustomSqlDimension
    from ..models.download_csv_from_explore_body_custom_labels import (
        DownloadCsvFromExploreBodyCustomLabels,
    )
    from ..models.filters import Filters
    from ..models.metric_query_metadata import MetricQueryMetadata
    from ..models.sort_field import SortField
    from ..models.table_calculation import TableCalculation


T = TypeVar("T", bound="DownloadCsvFromExploreBody")


@_attrs_define
class DownloadCsvFromExploreBody:
    """
    Attributes:
        table_calculations (List['TableCalculation']):
        limit (float):
        sorts (List['SortField']):
        filters (Filters):
        metrics (List[str]):
        dimensions (List[str]):
        explore_name (str):
        column_order (List[str]):
        show_table_names (bool):
        only_raw (bool):
        metadata (Union[Unset, MetricQueryMetadata]):
        timezone (Union[Unset, str]):
        custom_dimensions (Union[Unset, List[Union['CustomBinDimension', 'CustomSqlDimension']]]):
        additional_metrics (Union[Unset, List['AdditionalMetric']]):
        chart_name (Union[Unset, str]):
        hidden_fields (Union[Unset, List[str]]):
        custom_labels (Union[Unset, DownloadCsvFromExploreBodyCustomLabels]):
        csv_limit (Union[None, Unset, float]):
    """

    table_calculations: List["TableCalculation"]
    limit: float
    sorts: List["SortField"]
    filters: "Filters"
    metrics: List[str]
    dimensions: List[str]
    explore_name: str
    column_order: List[str]
    show_table_names: bool
    only_raw: bool
    metadata: Union[Unset, "MetricQueryMetadata"] = UNSET
    timezone: Union[Unset, str] = UNSET
    custom_dimensions: Union[Unset, List[Union["CustomBinDimension", "CustomSqlDimension"]]] = UNSET
    additional_metrics: Union[Unset, List["AdditionalMetric"]] = UNSET
    chart_name: Union[Unset, str] = UNSET
    hidden_fields: Union[Unset, List[str]] = UNSET
    custom_labels: Union[Unset, "DownloadCsvFromExploreBodyCustomLabels"] = UNSET
    csv_limit: Union[None, Unset, float] = UNSET
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

        column_order = self.column_order

        show_table_names = self.show_table_names

        only_raw = self.only_raw

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

        chart_name = self.chart_name

        hidden_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hidden_fields, Unset):
            hidden_fields = self.hidden_fields

        custom_labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_labels, Unset):
            custom_labels = self.custom_labels.to_dict()

        csv_limit: Union[None, Unset, float]
        if isinstance(self.csv_limit, Unset):
            csv_limit = UNSET
        else:
            csv_limit = self.csv_limit

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
                "columnOrder": column_order,
                "showTableNames": show_table_names,
                "onlyRaw": only_raw,
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
        if chart_name is not UNSET:
            field_dict["chartName"] = chart_name
        if hidden_fields is not UNSET:
            field_dict["hiddenFields"] = hidden_fields
        if custom_labels is not UNSET:
            field_dict["customLabels"] = custom_labels
        if csv_limit is not UNSET:
            field_dict["csvLimit"] = csv_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_metric import AdditionalMetric
        from ..models.custom_bin_dimension import CustomBinDimension
        from ..models.custom_sql_dimension import CustomSqlDimension
        from ..models.download_csv_from_explore_body_custom_labels import (
            DownloadCsvFromExploreBodyCustomLabels,
        )
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

        column_order = cast(List[str], d.pop("columnOrder"))

        show_table_names = d.pop("showTableNames")

        only_raw = d.pop("onlyRaw")

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

        chart_name = d.pop("chartName", UNSET)

        hidden_fields = cast(List[str], d.pop("hiddenFields", UNSET))

        _custom_labels = d.pop("customLabels", UNSET)
        custom_labels: Union[Unset, DownloadCsvFromExploreBodyCustomLabels]
        if isinstance(_custom_labels, Unset):
            custom_labels = UNSET
        else:
            custom_labels = DownloadCsvFromExploreBodyCustomLabels.from_dict(_custom_labels)

        def _parse_csv_limit(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        csv_limit = _parse_csv_limit(d.pop("csvLimit", UNSET))

        download_csv_from_explore_body = cls(
            table_calculations=table_calculations,
            limit=limit,
            sorts=sorts,
            filters=filters,
            metrics=metrics,
            dimensions=dimensions,
            explore_name=explore_name,
            column_order=column_order,
            show_table_names=show_table_names,
            only_raw=only_raw,
            metadata=metadata,
            timezone=timezone,
            custom_dimensions=custom_dimensions,
            additional_metrics=additional_metrics,
            chart_name=chart_name,
            hidden_fields=hidden_fields,
            custom_labels=custom_labels,
            csv_limit=csv_limit,
        )

        download_csv_from_explore_body.additional_properties = d
        return download_csv_from_explore_body

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
