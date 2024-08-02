from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.axis import Axis
    from ..models.echarts_grid import EchartsGrid
    from ..models.echarts_legend import EchartsLegend
    from ..models.series import Series


T = TypeVar("T", bound="PartialCompleteEChartsConfig")


@_attrs_define
class PartialCompleteEChartsConfig:
    """Make all properties in T optional

    Attributes:
        legend (Union[Unset, EchartsLegend]):
        grid (Union[Unset, EchartsGrid]):
        series (Union[Unset, List['Series']]):
        x_axis (Union[Unset, List['Axis']]):
        y_axis (Union[Unset, List['Axis']]):
    """

    legend: Union[Unset, "EchartsLegend"] = UNSET
    grid: Union[Unset, "EchartsGrid"] = UNSET
    series: Union[Unset, List["Series"]] = UNSET
    x_axis: Union[Unset, List["Axis"]] = UNSET
    y_axis: Union[Unset, List["Axis"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        legend: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.legend, Unset):
            legend = self.legend.to_dict()

        grid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.grid, Unset):
            grid = self.grid.to_dict()

        series: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        x_axis: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.x_axis, Unset):
            x_axis = []
            for x_axis_item_data in self.x_axis:
                x_axis_item = x_axis_item_data.to_dict()
                x_axis.append(x_axis_item)

        y_axis: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.y_axis, Unset):
            y_axis = []
            for y_axis_item_data in self.y_axis:
                y_axis_item = y_axis_item_data.to_dict()
                y_axis.append(y_axis_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legend is not UNSET:
            field_dict["legend"] = legend
        if grid is not UNSET:
            field_dict["grid"] = grid
        if series is not UNSET:
            field_dict["series"] = series
        if x_axis is not UNSET:
            field_dict["xAxis"] = x_axis
        if y_axis is not UNSET:
            field_dict["yAxis"] = y_axis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.axis import Axis
        from ..models.echarts_grid import EchartsGrid
        from ..models.echarts_legend import EchartsLegend
        from ..models.series import Series

        d = src_dict.copy()
        _legend = d.pop("legend", UNSET)
        legend: Union[Unset, EchartsLegend]
        if isinstance(_legend, Unset):
            legend = UNSET
        else:
            legend = EchartsLegend.from_dict(_legend)

        _grid = d.pop("grid", UNSET)
        grid: Union[Unset, EchartsGrid]
        if isinstance(_grid, Unset):
            grid = UNSET
        else:
            grid = EchartsGrid.from_dict(_grid)

        series = []
        _series = d.pop("series", UNSET)
        for series_item_data in _series or []:
            series_item = Series.from_dict(series_item_data)

            series.append(series_item)

        x_axis = []
        _x_axis = d.pop("xAxis", UNSET)
        for x_axis_item_data in _x_axis or []:
            x_axis_item = Axis.from_dict(x_axis_item_data)

            x_axis.append(x_axis_item)

        y_axis = []
        _y_axis = d.pop("yAxis", UNSET)
        for y_axis_item_data in _y_axis or []:
            y_axis_item = Axis.from_dict(y_axis_item_data)

            y_axis.append(y_axis_item)

        partial_complete_e_charts_config = cls(
            legend=legend,
            grid=grid,
            series=series,
            x_axis=x_axis,
            y_axis=y_axis,
        )

        partial_complete_e_charts_config.additional_properties = d
        return partial_complete_e_charts_config

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
