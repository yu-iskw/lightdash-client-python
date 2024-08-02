from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pie_chart_legend_position import PieChartLegendPosition
from ..models.pie_chart_value_label import PieChartValueLabel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_string_partial_pie_chart_value_options import (
        RecordStringPartialPieChartValueOptions,
    )
    from ..models.record_string_series_metadata import RecordStringSeriesMetadata
    from ..models.record_string_string import RecordStringString


T = TypeVar("T", bound="PieChart")


@_attrs_define
class PieChart:
    """
    Attributes:
        metadata (Union[Unset, RecordStringSeriesMetadata]): Construct a type with a set of properties K of type T
        legend_position (Union[Unset, PieChartLegendPosition]):
        show_legend (Union[Unset, bool]):
        group_sort_overrides (Union[Unset, List[str]]):
        group_value_option_overrides (Union[Unset, RecordStringPartialPieChartValueOptions]): Construct a type with a
            set of properties K of type T
        group_color_overrides (Union[Unset, RecordStringString]): Construct a type with a set of properties K of type T
        group_label_overrides (Union[Unset, RecordStringString]): Construct a type with a set of properties K of type T
        show_percentage (Union[Unset, bool]):
        show_value (Union[Unset, bool]):
        value_label (Union[Unset, PieChartValueLabel]):
        is_donut (Union[Unset, bool]):
        metric_id (Union[Unset, str]):
        group_field_ids (Union[Unset, List[str]]):
    """

    metadata: Union[Unset, "RecordStringSeriesMetadata"] = UNSET
    legend_position: Union[Unset, PieChartLegendPosition] = UNSET
    show_legend: Union[Unset, bool] = UNSET
    group_sort_overrides: Union[Unset, List[str]] = UNSET
    group_value_option_overrides: Union[Unset, "RecordStringPartialPieChartValueOptions"] = UNSET
    group_color_overrides: Union[Unset, "RecordStringString"] = UNSET
    group_label_overrides: Union[Unset, "RecordStringString"] = UNSET
    show_percentage: Union[Unset, bool] = UNSET
    show_value: Union[Unset, bool] = UNSET
    value_label: Union[Unset, PieChartValueLabel] = UNSET
    is_donut: Union[Unset, bool] = UNSET
    metric_id: Union[Unset, str] = UNSET
    group_field_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        legend_position: Union[Unset, str] = UNSET
        if not isinstance(self.legend_position, Unset):
            legend_position = self.legend_position.value

        show_legend = self.show_legend

        group_sort_overrides: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_sort_overrides, Unset):
            group_sort_overrides = self.group_sort_overrides

        group_value_option_overrides: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_value_option_overrides, Unset):
            group_value_option_overrides = self.group_value_option_overrides.to_dict()

        group_color_overrides: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_color_overrides, Unset):
            group_color_overrides = self.group_color_overrides.to_dict()

        group_label_overrides: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_label_overrides, Unset):
            group_label_overrides = self.group_label_overrides.to_dict()

        show_percentage = self.show_percentage

        show_value = self.show_value

        value_label: Union[Unset, str] = UNSET
        if not isinstance(self.value_label, Unset):
            value_label = self.value_label.value

        is_donut = self.is_donut

        metric_id = self.metric_id

        group_field_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_field_ids, Unset):
            group_field_ids = self.group_field_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if legend_position is not UNSET:
            field_dict["legendPosition"] = legend_position
        if show_legend is not UNSET:
            field_dict["showLegend"] = show_legend
        if group_sort_overrides is not UNSET:
            field_dict["groupSortOverrides"] = group_sort_overrides
        if group_value_option_overrides is not UNSET:
            field_dict["groupValueOptionOverrides"] = group_value_option_overrides
        if group_color_overrides is not UNSET:
            field_dict["groupColorOverrides"] = group_color_overrides
        if group_label_overrides is not UNSET:
            field_dict["groupLabelOverrides"] = group_label_overrides
        if show_percentage is not UNSET:
            field_dict["showPercentage"] = show_percentage
        if show_value is not UNSET:
            field_dict["showValue"] = show_value
        if value_label is not UNSET:
            field_dict["valueLabel"] = value_label
        if is_donut is not UNSET:
            field_dict["isDonut"] = is_donut
        if metric_id is not UNSET:
            field_dict["metricId"] = metric_id
        if group_field_ids is not UNSET:
            field_dict["groupFieldIds"] = group_field_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_string_partial_pie_chart_value_options import (
            RecordStringPartialPieChartValueOptions,
        )
        from ..models.record_string_series_metadata import RecordStringSeriesMetadata
        from ..models.record_string_string import RecordStringString

        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, RecordStringSeriesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RecordStringSeriesMetadata.from_dict(_metadata)

        _legend_position = d.pop("legendPosition", UNSET)
        legend_position: Union[Unset, PieChartLegendPosition]
        if isinstance(_legend_position, Unset):
            legend_position = UNSET
        else:
            legend_position = PieChartLegendPosition(_legend_position)

        show_legend = d.pop("showLegend", UNSET)

        group_sort_overrides = cast(List[str], d.pop("groupSortOverrides", UNSET))

        _group_value_option_overrides = d.pop("groupValueOptionOverrides", UNSET)
        group_value_option_overrides: Union[Unset, RecordStringPartialPieChartValueOptions]
        if isinstance(_group_value_option_overrides, Unset):
            group_value_option_overrides = UNSET
        else:
            group_value_option_overrides = RecordStringPartialPieChartValueOptions.from_dict(
                _group_value_option_overrides
            )

        _group_color_overrides = d.pop("groupColorOverrides", UNSET)
        group_color_overrides: Union[Unset, RecordStringString]
        if isinstance(_group_color_overrides, Unset):
            group_color_overrides = UNSET
        else:
            group_color_overrides = RecordStringString.from_dict(_group_color_overrides)

        _group_label_overrides = d.pop("groupLabelOverrides", UNSET)
        group_label_overrides: Union[Unset, RecordStringString]
        if isinstance(_group_label_overrides, Unset):
            group_label_overrides = UNSET
        else:
            group_label_overrides = RecordStringString.from_dict(_group_label_overrides)

        show_percentage = d.pop("showPercentage", UNSET)

        show_value = d.pop("showValue", UNSET)

        _value_label = d.pop("valueLabel", UNSET)
        value_label: Union[Unset, PieChartValueLabel]
        if isinstance(_value_label, Unset):
            value_label = UNSET
        else:
            value_label = PieChartValueLabel(_value_label)

        is_donut = d.pop("isDonut", UNSET)

        metric_id = d.pop("metricId", UNSET)

        group_field_ids = cast(List[str], d.pop("groupFieldIds", UNSET))

        pie_chart = cls(
            metadata=metadata,
            legend_position=legend_position,
            show_legend=show_legend,
            group_sort_overrides=group_sort_overrides,
            group_value_option_overrides=group_value_option_overrides,
            group_color_overrides=group_color_overrides,
            group_label_overrides=group_label_overrides,
            show_percentage=show_percentage,
            show_value=show_value,
            value_label=value_label,
            is_donut=is_donut,
            metric_id=metric_id,
            group_field_ids=group_field_ids,
        )

        pie_chart.additional_properties = d
        return pie_chart

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
