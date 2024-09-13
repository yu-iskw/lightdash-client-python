from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.funnel_chart_data_input import FunnelChartDataInput
from ..models.funnel_chart_legend_position import FunnelChartLegendPosition
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.funnel_chart_labels import FunnelChartLabels
    from ..models.record_string_series_metadata import RecordStringSeriesMetadata
    from ..models.record_string_string import RecordStringString


T = TypeVar("T", bound="FunnelChart")


@_attrs_define
class FunnelChart:
    """
    Attributes:
        legend_position (Union[Unset, FunnelChartLegendPosition]):
        show_legend (Union[Unset, bool]):
        labels (Union[Unset, FunnelChartLabels]):
        color_overrides (Union[Unset, RecordStringString]): Construct a type with a set of properties K of type T
        label_overrides (Union[Unset, RecordStringString]): Construct a type with a set of properties K of type T
        metadata (Union[Unset, RecordStringSeriesMetadata]): Construct a type with a set of properties K of type T
        field_id (Union[Unset, str]):
        data_input (Union[Unset, FunnelChartDataInput]):
    """

    legend_position: Union[Unset, FunnelChartLegendPosition] = UNSET
    show_legend: Union[Unset, bool] = UNSET
    labels: Union[Unset, "FunnelChartLabels"] = UNSET
    color_overrides: Union[Unset, "RecordStringString"] = UNSET
    label_overrides: Union[Unset, "RecordStringString"] = UNSET
    metadata: Union[Unset, "RecordStringSeriesMetadata"] = UNSET
    field_id: Union[Unset, str] = UNSET
    data_input: Union[Unset, FunnelChartDataInput] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        legend_position: Union[Unset, str] = UNSET
        if not isinstance(self.legend_position, Unset):
            legend_position = self.legend_position.value

        show_legend = self.show_legend

        labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        color_overrides: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color_overrides, Unset):
            color_overrides = self.color_overrides.to_dict()

        label_overrides: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label_overrides, Unset):
            label_overrides = self.label_overrides.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_id = self.field_id

        data_input: Union[Unset, str] = UNSET
        if not isinstance(self.data_input, Unset):
            data_input = self.data_input.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legend_position is not UNSET:
            field_dict["legendPosition"] = legend_position
        if show_legend is not UNSET:
            field_dict["showLegend"] = show_legend
        if labels is not UNSET:
            field_dict["labels"] = labels
        if color_overrides is not UNSET:
            field_dict["colorOverrides"] = color_overrides
        if label_overrides is not UNSET:
            field_dict["labelOverrides"] = label_overrides
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if data_input is not UNSET:
            field_dict["dataInput"] = data_input

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.funnel_chart_labels import FunnelChartLabels
        from ..models.record_string_series_metadata import RecordStringSeriesMetadata
        from ..models.record_string_string import RecordStringString

        d = src_dict.copy()
        _legend_position = d.pop("legendPosition", UNSET)
        legend_position: Union[Unset, FunnelChartLegendPosition]
        if isinstance(_legend_position, Unset):
            legend_position = UNSET
        else:
            legend_position = FunnelChartLegendPosition(_legend_position)

        show_legend = d.pop("showLegend", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, FunnelChartLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = FunnelChartLabels.from_dict(_labels)

        _color_overrides = d.pop("colorOverrides", UNSET)
        color_overrides: Union[Unset, RecordStringString]
        if isinstance(_color_overrides, Unset):
            color_overrides = UNSET
        else:
            color_overrides = RecordStringString.from_dict(_color_overrides)

        _label_overrides = d.pop("labelOverrides", UNSET)
        label_overrides: Union[Unset, RecordStringString]
        if isinstance(_label_overrides, Unset):
            label_overrides = UNSET
        else:
            label_overrides = RecordStringString.from_dict(_label_overrides)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, RecordStringSeriesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RecordStringSeriesMetadata.from_dict(_metadata)

        field_id = d.pop("fieldId", UNSET)

        _data_input = d.pop("dataInput", UNSET)
        data_input: Union[Unset, FunnelChartDataInput]
        if isinstance(_data_input, Unset):
            data_input = UNSET
        else:
            data_input = FunnelChartDataInput(_data_input)

        funnel_chart = cls(
            legend_position=legend_position,
            show_legend=show_legend,
            labels=labels,
            color_overrides=color_overrides,
            label_overrides=label_overrides,
            metadata=metadata,
            field_id=field_id,
            data_input=data_input,
        )

        funnel_chart.additional_properties = d
        return funnel_chart

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
