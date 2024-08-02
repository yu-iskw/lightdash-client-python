from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_complete_cartesian_chart_layout import (
        PartialCompleteCartesianChartLayout,
    )
    from ..models.partial_complete_e_charts_config import PartialCompleteEChartsConfig
    from ..models.record_string_series_metadata import RecordStringSeriesMetadata


T = TypeVar("T", bound="CartesianChart")


@_attrs_define
class CartesianChart:
    """
    Attributes:
        e_charts_config (PartialCompleteEChartsConfig): Make all properties in T optional
        layout (PartialCompleteCartesianChartLayout): Make all properties in T optional
        metadata (Union[Unset, RecordStringSeriesMetadata]): Construct a type with a set of properties K of type T
    """

    e_charts_config: "PartialCompleteEChartsConfig"
    layout: "PartialCompleteCartesianChartLayout"
    metadata: Union[Unset, "RecordStringSeriesMetadata"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        e_charts_config = self.e_charts_config.to_dict()

        layout = self.layout.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eChartsConfig": e_charts_config,
                "layout": layout,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.partial_complete_cartesian_chart_layout import (
            PartialCompleteCartesianChartLayout,
        )
        from ..models.partial_complete_e_charts_config import (
            PartialCompleteEChartsConfig,
        )
        from ..models.record_string_series_metadata import RecordStringSeriesMetadata

        d = src_dict.copy()
        e_charts_config = PartialCompleteEChartsConfig.from_dict(d.pop("eChartsConfig"))

        layout = PartialCompleteCartesianChartLayout.from_dict(d.pop("layout"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, RecordStringSeriesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RecordStringSeriesMetadata.from_dict(_metadata)

        cartesian_chart = cls(
            e_charts_config=e_charts_config,
            layout=layout,
            metadata=metadata,
        )

        cartesian_chart.additional_properties = d
        return cartesian_chart

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
