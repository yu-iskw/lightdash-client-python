from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filters_dimensions_type_0 import FiltersDimensionsType0
    from ..models.filters_dimensions_type_1 import FiltersDimensionsType1
    from ..models.filters_metrics_type_0 import FiltersMetricsType0
    from ..models.filters_metrics_type_1 import FiltersMetricsType1


T = TypeVar("T", bound="Filters")


@attr.s(auto_attribs=True)
class Filters:
    """
    Attributes:
        metrics (Union['FiltersMetricsType0', 'FiltersMetricsType1', Unset]):
        dimensions (Union['FiltersDimensionsType0', 'FiltersDimensionsType1', Unset]):
    """

    metrics: Union["FiltersMetricsType0", "FiltersMetricsType1", Unset] = UNSET
    dimensions: Union["FiltersDimensionsType0", "FiltersDimensionsType1", Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.filters_dimensions_type_0 import FiltersDimensionsType0
        from ..models.filters_metrics_type_0 import FiltersMetricsType0

        metrics: Union[Dict[str, Any], Unset]
        if isinstance(self.metrics, Unset):
            metrics = UNSET

        elif isinstance(self.metrics, FiltersMetricsType0):
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

        elif isinstance(self.dimensions, FiltersDimensionsType0):
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
        from ..models.filters_dimensions_type_0 import FiltersDimensionsType0
        from ..models.filters_dimensions_type_1 import FiltersDimensionsType1
        from ..models.filters_metrics_type_0 import FiltersMetricsType0
        from ..models.filters_metrics_type_1 import FiltersMetricsType1

        d = src_dict.copy()

        def _parse_metrics(data: object) -> Union["FiltersMetricsType0", "FiltersMetricsType1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _metrics_type_0 = data
                metrics_type_0: Union[Unset, FiltersMetricsType0]
                if isinstance(_metrics_type_0, Unset):
                    metrics_type_0 = UNSET
                else:
                    metrics_type_0 = FiltersMetricsType0.from_dict(_metrics_type_0)

                return metrics_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _metrics_type_1 = data
            metrics_type_1: Union[Unset, FiltersMetricsType1]
            if isinstance(_metrics_type_1, Unset):
                metrics_type_1 = UNSET
            else:
                metrics_type_1 = FiltersMetricsType1.from_dict(_metrics_type_1)

            return metrics_type_1

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_dimensions(data: object) -> Union["FiltersDimensionsType0", "FiltersDimensionsType1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _dimensions_type_0 = data
                dimensions_type_0: Union[Unset, FiltersDimensionsType0]
                if isinstance(_dimensions_type_0, Unset):
                    dimensions_type_0 = UNSET
                else:
                    dimensions_type_0 = FiltersDimensionsType0.from_dict(_dimensions_type_0)

                return dimensions_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _dimensions_type_1 = data
            dimensions_type_1: Union[Unset, FiltersDimensionsType1]
            if isinstance(_dimensions_type_1, Unset):
                dimensions_type_1 = UNSET
            else:
                dimensions_type_1 = FiltersDimensionsType1.from_dict(_dimensions_type_1)

            return dimensions_type_1

        dimensions = _parse_dimensions(d.pop("dimensions", UNSET))

        filters = cls(
            metrics=metrics,
            dimensions=dimensions,
        )

        filters.additional_properties = d
        return filters

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
