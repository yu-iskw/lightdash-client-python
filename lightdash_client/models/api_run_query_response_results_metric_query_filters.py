from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_run_query_response_results_metric_query_filters_dimensions_type_0 import (
        ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType0,
    )
    from ..models.api_run_query_response_results_metric_query_filters_dimensions_type_1 import (
        ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType1,
    )
    from ..models.api_run_query_response_results_metric_query_filters_metrics_type_0 import (
        ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0,
    )
    from ..models.api_run_query_response_results_metric_query_filters_metrics_type_1 import (
        ApiRunQueryResponseResultsMetricQueryFiltersMetricsType1,
    )


T = TypeVar("T", bound="ApiRunQueryResponseResultsMetricQueryFilters")


@attr.s(auto_attribs=True)
class ApiRunQueryResponseResultsMetricQueryFilters:
    """
    Attributes:
        metrics (Union['ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0',
            'ApiRunQueryResponseResultsMetricQueryFiltersMetricsType1', Unset]):
        dimensions (Union['ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType0',
            'ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType1', Unset]):
    """

    metrics: Union[
        "ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0",
        "ApiRunQueryResponseResultsMetricQueryFiltersMetricsType1",
        Unset,
    ] = UNSET
    dimensions: Union[
        "ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType0",
        "ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType1",
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.api_run_query_response_results_metric_query_filters_dimensions_type_0 import (
            ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType0,
        )
        from ..models.api_run_query_response_results_metric_query_filters_metrics_type_0 import (
            ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0,
        )

        metrics: Union[Dict[str, Any], Unset]
        if isinstance(self.metrics, Unset):
            metrics = UNSET

        elif isinstance(self.metrics, ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0):
            metrics = UNSET
            if not isinstance(self.metrics, Unset):
                metrics = self.metrics.to_dict()

        else:
            metrics = UNSET
            if not isinstance(self.metrics, Unset):
                metrics = self.metrics.to_dict()

        dimensions: Union[Dict[str, Any], Unset]
        if isinstance(self.dimensions, Unset):
            dimensions = UNSET

        elif isinstance(self.dimensions, ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType0):
            dimensions = UNSET
            if not isinstance(self.dimensions, Unset):
                dimensions = self.dimensions.to_dict()

        else:
            dimensions = UNSET
            if not isinstance(self.dimensions, Unset):
                dimensions = self.dimensions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_run_query_response_results_metric_query_filters_dimensions_type_0 import (
            ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType0,
        )
        from ..models.api_run_query_response_results_metric_query_filters_dimensions_type_1 import (
            ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType1,
        )
        from ..models.api_run_query_response_results_metric_query_filters_metrics_type_0 import (
            ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0,
        )
        from ..models.api_run_query_response_results_metric_query_filters_metrics_type_1 import (
            ApiRunQueryResponseResultsMetricQueryFiltersMetricsType1,
        )

        d = src_dict.copy()

        def _parse_metrics(
            data: object,
        ) -> Union[
            "ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0",
            "ApiRunQueryResponseResultsMetricQueryFiltersMetricsType1",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _metrics_type_0 = data
                metrics_type_0: Union[Unset, ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0]
                if isinstance(_metrics_type_0, Unset):
                    metrics_type_0 = UNSET
                else:
                    metrics_type_0 = ApiRunQueryResponseResultsMetricQueryFiltersMetricsType0.from_dict(_metrics_type_0)

                return metrics_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _metrics_type_1 = data
            metrics_type_1: Union[Unset, ApiRunQueryResponseResultsMetricQueryFiltersMetricsType1]
            if isinstance(_metrics_type_1, Unset):
                metrics_type_1 = UNSET
            else:
                metrics_type_1 = ApiRunQueryResponseResultsMetricQueryFiltersMetricsType1.from_dict(_metrics_type_1)

            return metrics_type_1

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_dimensions(
            data: object,
        ) -> Union[
            "ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType0",
            "ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType1",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _dimensions_type_0 = data
                dimensions_type_0: Union[Unset, ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType0]
                if isinstance(_dimensions_type_0, Unset):
                    dimensions_type_0 = UNSET
                else:
                    dimensions_type_0 = ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType0.from_dict(
                        _dimensions_type_0
                    )

                return dimensions_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _dimensions_type_1 = data
            dimensions_type_1: Union[Unset, ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType1]
            if isinstance(_dimensions_type_1, Unset):
                dimensions_type_1 = UNSET
            else:
                dimensions_type_1 = ApiRunQueryResponseResultsMetricQueryFiltersDimensionsType1.from_dict(
                    _dimensions_type_1
                )

            return dimensions_type_1

        dimensions = _parse_dimensions(d.pop("dimensions", UNSET))

        api_run_query_response_results_metric_query_filters = cls(
            metrics=metrics,
            dimensions=dimensions,
        )

        api_run_query_response_results_metric_query_filters.additional_properties = d
        return api_run_query_response_results_metric_query_filters

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
