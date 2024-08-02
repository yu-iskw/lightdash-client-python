from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialCompleteCartesianChartLayout")


@_attrs_define
class PartialCompleteCartesianChartLayout:
    """Make all properties in T optional

    Attributes:
        x_field (Union[Unset, str]):
        y_field (Union[Unset, List[str]]):
        flip_axes (Union[Unset, bool]):
        show_grid_x (Union[Unset, bool]):
        show_grid_y (Union[Unset, bool]):
    """

    x_field: Union[Unset, str] = UNSET
    y_field: Union[Unset, List[str]] = UNSET
    flip_axes: Union[Unset, bool] = UNSET
    show_grid_x: Union[Unset, bool] = UNSET
    show_grid_y: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x_field = self.x_field

        y_field: Union[Unset, List[str]] = UNSET
        if not isinstance(self.y_field, Unset):
            y_field = self.y_field

        flip_axes = self.flip_axes

        show_grid_x = self.show_grid_x

        show_grid_y = self.show_grid_y

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x_field is not UNSET:
            field_dict["xField"] = x_field
        if y_field is not UNSET:
            field_dict["yField"] = y_field
        if flip_axes is not UNSET:
            field_dict["flipAxes"] = flip_axes
        if show_grid_x is not UNSET:
            field_dict["showGridX"] = show_grid_x
        if show_grid_y is not UNSET:
            field_dict["showGridY"] = show_grid_y

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x_field = d.pop("xField", UNSET)

        y_field = cast(List[str], d.pop("yField", UNSET))

        flip_axes = d.pop("flipAxes", UNSET)

        show_grid_x = d.pop("showGridX", UNSET)

        show_grid_y = d.pop("showGridY", UNSET)

        partial_complete_cartesian_chart_layout = cls(
            x_field=x_field,
            y_field=y_field,
            flip_axes=flip_axes,
            show_grid_x=show_grid_x,
            show_grid_y=show_grid_y,
        )

        partial_complete_cartesian_chart_layout.additional_properties = d
        return partial_complete_cartesian_chart_layout

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
