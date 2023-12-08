from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mark_line_data_label import MarkLineDataLabel
    from ..models.mark_line_data_line_style import MarkLineDataLineStyle


T = TypeVar("T", bound="MarkLineData")


@attr.s(auto_attribs=True)
class MarkLineData:
    """
    Attributes:
        value (str):
        name (str):
        label (Union[Unset, MarkLineDataLabel]):
        line_style (Union[Unset, MarkLineDataLineStyle]):
        x_axis (Union[Unset, str]):
        y_axis (Union[Unset, str]):
    """

    value: str
    name: str
    label: Union[Unset, "MarkLineDataLabel"] = UNSET
    line_style: Union[Unset, "MarkLineDataLineStyle"] = UNSET
    x_axis: Union[Unset, str] = UNSET
    y_axis: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        name = self.name
        label: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        line_style: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_style, Unset):
            line_style = self.line_style.to_dict()

        x_axis = self.x_axis
        y_axis = self.y_axis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "name": name,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if line_style is not UNSET:
            field_dict["lineStyle"] = line_style
        if x_axis is not UNSET:
            field_dict["xAxis"] = x_axis
        if y_axis is not UNSET:
            field_dict["yAxis"] = y_axis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mark_line_data_label import MarkLineDataLabel
        from ..models.mark_line_data_line_style import MarkLineDataLineStyle

        d = src_dict.copy()
        value = d.pop("value")

        name = d.pop("name")

        _label = d.pop("label", UNSET)
        label: Union[Unset, MarkLineDataLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = MarkLineDataLabel.from_dict(_label)

        _line_style = d.pop("lineStyle", UNSET)
        line_style: Union[Unset, MarkLineDataLineStyle]
        if isinstance(_line_style, Unset):
            line_style = UNSET
        else:
            line_style = MarkLineDataLineStyle.from_dict(_line_style)

        x_axis = d.pop("xAxis", UNSET)

        y_axis = d.pop("yAxis", UNSET)

        mark_line_data = cls(
            value=value,
            name=name,
            label=label,
            line_style=line_style,
            x_axis=x_axis,
            y_axis=y_axis,
        )

        mark_line_data.additional_properties = d
        return mark_line_data

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
