from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_chart_results_json_body_filters_dimensions_type_0 import (
        PostChartResultsJsonBodyFiltersDimensionsType0,
    )
    from ..models.post_chart_results_json_body_filters_dimensions_type_1 import (
        PostChartResultsJsonBodyFiltersDimensionsType1,
    )
    from ..models.post_chart_results_json_body_filters_metrics_type_0 import (
        PostChartResultsJsonBodyFiltersMetricsType0,
    )
    from ..models.post_chart_results_json_body_filters_metrics_type_1 import (
        PostChartResultsJsonBodyFiltersMetricsType1,
    )


T = TypeVar("T", bound="PostChartResultsJsonBodyFilters")


@attr.s(auto_attribs=True)
class PostChartResultsJsonBodyFilters:
    """
    Attributes:
        metrics (Union['PostChartResultsJsonBodyFiltersMetricsType0', 'PostChartResultsJsonBodyFiltersMetricsType1',
            Unset]):
        dimensions (Union['PostChartResultsJsonBodyFiltersDimensionsType0',
            'PostChartResultsJsonBodyFiltersDimensionsType1', Unset]):
    """

    metrics: Union[
        "PostChartResultsJsonBodyFiltersMetricsType0", "PostChartResultsJsonBodyFiltersMetricsType1", Unset
    ] = UNSET
    dimensions: Union[
        "PostChartResultsJsonBodyFiltersDimensionsType0", "PostChartResultsJsonBodyFiltersDimensionsType1", Unset
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.post_chart_results_json_body_filters_dimensions_type_0 import (
            PostChartResultsJsonBodyFiltersDimensionsType0,
        )
        from ..models.post_chart_results_json_body_filters_metrics_type_0 import (
            PostChartResultsJsonBodyFiltersMetricsType0,
        )

        metrics: Union[Dict[str, Any], Unset]
        if isinstance(self.metrics, Unset):
            metrics = UNSET

        elif isinstance(self.metrics, PostChartResultsJsonBodyFiltersMetricsType0):
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

        elif isinstance(self.dimensions, PostChartResultsJsonBodyFiltersDimensionsType0):
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
        from ..models.post_chart_results_json_body_filters_dimensions_type_0 import (
            PostChartResultsJsonBodyFiltersDimensionsType0,
        )
        from ..models.post_chart_results_json_body_filters_dimensions_type_1 import (
            PostChartResultsJsonBodyFiltersDimensionsType1,
        )
        from ..models.post_chart_results_json_body_filters_metrics_type_0 import (
            PostChartResultsJsonBodyFiltersMetricsType0,
        )
        from ..models.post_chart_results_json_body_filters_metrics_type_1 import (
            PostChartResultsJsonBodyFiltersMetricsType1,
        )

        d = src_dict.copy()

        def _parse_metrics(
            data: object,
        ) -> Union["PostChartResultsJsonBodyFiltersMetricsType0", "PostChartResultsJsonBodyFiltersMetricsType1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _metrics_type_0 = data
                metrics_type_0: Union[Unset, PostChartResultsJsonBodyFiltersMetricsType0]
                if isinstance(_metrics_type_0, Unset):
                    metrics_type_0 = UNSET
                else:
                    metrics_type_0 = PostChartResultsJsonBodyFiltersMetricsType0.from_dict(_metrics_type_0)

                return metrics_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _metrics_type_1 = data
            metrics_type_1: Union[Unset, PostChartResultsJsonBodyFiltersMetricsType1]
            if isinstance(_metrics_type_1, Unset):
                metrics_type_1 = UNSET
            else:
                metrics_type_1 = PostChartResultsJsonBodyFiltersMetricsType1.from_dict(_metrics_type_1)

            return metrics_type_1

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_dimensions(
            data: object,
        ) -> Union[
            "PostChartResultsJsonBodyFiltersDimensionsType0", "PostChartResultsJsonBodyFiltersDimensionsType1", Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _dimensions_type_0 = data
                dimensions_type_0: Union[Unset, PostChartResultsJsonBodyFiltersDimensionsType0]
                if isinstance(_dimensions_type_0, Unset):
                    dimensions_type_0 = UNSET
                else:
                    dimensions_type_0 = PostChartResultsJsonBodyFiltersDimensionsType0.from_dict(_dimensions_type_0)

                return dimensions_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _dimensions_type_1 = data
            dimensions_type_1: Union[Unset, PostChartResultsJsonBodyFiltersDimensionsType1]
            if isinstance(_dimensions_type_1, Unset):
                dimensions_type_1 = UNSET
            else:
                dimensions_type_1 = PostChartResultsJsonBodyFiltersDimensionsType1.from_dict(_dimensions_type_1)

            return dimensions_type_1

        dimensions = _parse_dimensions(d.pop("dimensions", UNSET))

        post_chart_results_json_body_filters = cls(
            metrics=metrics,
            dimensions=dimensions,
        )

        post_chart_results_json_body_filters.additional_properties = d
        return post_chart_results_json_body_filters

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
