from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_explorer_comparison_type_type_0 import MetricExplorerComparisonTypeType0
    from ..models.metric_explorer_comparison_type_type_1 import MetricExplorerComparisonTypeType1
    from ..models.metric_explorer_comparison_type_type_2 import MetricExplorerComparisonTypeType2
    from ..models.time_dimension_config import TimeDimensionConfig


T = TypeVar("T", bound="RunMetricExplorerQueryBody")


@_attrs_define
class RunMetricExplorerQueryBody:
    """
    Attributes:
        comparison (Union['MetricExplorerComparisonTypeType0', 'MetricExplorerComparisonTypeType1',
            'MetricExplorerComparisonTypeType2']):
        time_dimension_override (Union[Unset, TimeDimensionConfig]):
    """

    comparison: Union[
        "MetricExplorerComparisonTypeType0", "MetricExplorerComparisonTypeType1", "MetricExplorerComparisonTypeType2"
    ]
    time_dimension_override: Union[Unset, "TimeDimensionConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.metric_explorer_comparison_type_type_0 import MetricExplorerComparisonTypeType0
        from ..models.metric_explorer_comparison_type_type_1 import MetricExplorerComparisonTypeType1
        from ..models.metric_explorer_comparison_type_type_2 import MetricExplorerComparisonTypeType2
        from ..models.time_dimension_config import TimeDimensionConfig

        comparison: Dict[str, Any]
        if isinstance(self.comparison, MetricExplorerComparisonTypeType0):
            comparison = self.comparison.to_dict()
        elif isinstance(self.comparison, MetricExplorerComparisonTypeType1):
            comparison = self.comparison.to_dict()
        else:
            comparison = self.comparison.to_dict()

        time_dimension_override: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_dimension_override, Unset):
            time_dimension_override = self.time_dimension_override.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comparison": comparison,
            }
        )
        if time_dimension_override is not UNSET:
            field_dict["timeDimensionOverride"] = time_dimension_override

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metric_explorer_comparison_type_type_0 import MetricExplorerComparisonTypeType0
        from ..models.metric_explorer_comparison_type_type_1 import MetricExplorerComparisonTypeType1
        from ..models.metric_explorer_comparison_type_type_2 import MetricExplorerComparisonTypeType2
        from ..models.time_dimension_config import TimeDimensionConfig

        d = src_dict.copy()

        def _parse_comparison(
            data: object,
        ) -> Union[
            "MetricExplorerComparisonTypeType0",
            "MetricExplorerComparisonTypeType1",
            "MetricExplorerComparisonTypeType2",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_metric_explorer_comparison_type_type_0 = MetricExplorerComparisonTypeType0.from_dict(
                    data
                )

                return componentsschemas_metric_explorer_comparison_type_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_metric_explorer_comparison_type_type_1 = MetricExplorerComparisonTypeType1.from_dict(
                    data
                )

                return componentsschemas_metric_explorer_comparison_type_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_metric_explorer_comparison_type_type_2 = MetricExplorerComparisonTypeType2.from_dict(data)

            return componentsschemas_metric_explorer_comparison_type_type_2

        comparison = _parse_comparison(d.pop("comparison"))

        _time_dimension_override = d.pop("timeDimensionOverride", UNSET)
        time_dimension_override: Union[Unset, TimeDimensionConfig]
        if isinstance(_time_dimension_override, Unset):
            time_dimension_override = UNSET
        else:
            time_dimension_override = TimeDimensionConfig.from_dict(_time_dimension_override)

        run_metric_explorer_query_body = cls(
            comparison=comparison,
            time_dimension_override=time_dimension_override,
        )

        run_metric_explorer_query_body.additional_properties = d
        return run_metric_explorer_query_body

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
