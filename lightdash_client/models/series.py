from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cartesian_series_type import CartesianSeriesType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mark_line import MarkLine
    from ..models.series_area_style import SeriesAreaStyle
    from ..models.series_encode import SeriesEncode
    from ..models.series_label import SeriesLabel
    from ..models.series_stack_label import SeriesStackLabel


T = TypeVar("T", bound="Series")


@_attrs_define
class Series:
    """
    Attributes:
        type (CartesianSeriesType):
        encode (SeriesEncode):
        mark_line (Union[Unset, MarkLine]):
        smooth (Union[Unset, bool]):
        show_symbol (Union[Unset, bool]):
        area_style (Union[Unset, SeriesAreaStyle]):
        hidden (Union[Unset, bool]):
        label (Union[Unset, SeriesLabel]):
        y_axis_index (Union[Unset, float]):
        color (Union[Unset, str]):
        name (Union[Unset, str]):
        stack_label (Union[Unset, SeriesStackLabel]):
        stack (Union[Unset, str]):
    """

    type: CartesianSeriesType
    encode: "SeriesEncode"
    mark_line: Union[Unset, "MarkLine"] = UNSET
    smooth: Union[Unset, bool] = UNSET
    show_symbol: Union[Unset, bool] = UNSET
    area_style: Union[Unset, "SeriesAreaStyle"] = UNSET
    hidden: Union[Unset, bool] = UNSET
    label: Union[Unset, "SeriesLabel"] = UNSET
    y_axis_index: Union[Unset, float] = UNSET
    color: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    stack_label: Union[Unset, "SeriesStackLabel"] = UNSET
    stack: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        encode = self.encode.to_dict()

        mark_line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mark_line, Unset):
            mark_line = self.mark_line.to_dict()

        smooth = self.smooth

        show_symbol = self.show_symbol

        area_style: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.area_style, Unset):
            area_style = self.area_style.to_dict()

        hidden = self.hidden

        label: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        y_axis_index = self.y_axis_index

        color = self.color

        name = self.name

        stack_label: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stack_label, Unset):
            stack_label = self.stack_label.to_dict()

        stack = self.stack

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "encode": encode,
            }
        )
        if mark_line is not UNSET:
            field_dict["markLine"] = mark_line
        if smooth is not UNSET:
            field_dict["smooth"] = smooth
        if show_symbol is not UNSET:
            field_dict["showSymbol"] = show_symbol
        if area_style is not UNSET:
            field_dict["areaStyle"] = area_style
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if label is not UNSET:
            field_dict["label"] = label
        if y_axis_index is not UNSET:
            field_dict["yAxisIndex"] = y_axis_index
        if color is not UNSET:
            field_dict["color"] = color
        if name is not UNSET:
            field_dict["name"] = name
        if stack_label is not UNSET:
            field_dict["stackLabel"] = stack_label
        if stack is not UNSET:
            field_dict["stack"] = stack

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mark_line import MarkLine
        from ..models.series_area_style import SeriesAreaStyle
        from ..models.series_encode import SeriesEncode
        from ..models.series_label import SeriesLabel
        from ..models.series_stack_label import SeriesStackLabel

        d = src_dict.copy()
        type = CartesianSeriesType(d.pop("type"))

        encode = SeriesEncode.from_dict(d.pop("encode"))

        _mark_line = d.pop("markLine", UNSET)
        mark_line: Union[Unset, MarkLine]
        if isinstance(_mark_line, Unset):
            mark_line = UNSET
        else:
            mark_line = MarkLine.from_dict(_mark_line)

        smooth = d.pop("smooth", UNSET)

        show_symbol = d.pop("showSymbol", UNSET)

        _area_style = d.pop("areaStyle", UNSET)
        area_style: Union[Unset, SeriesAreaStyle]
        if isinstance(_area_style, Unset):
            area_style = UNSET
        else:
            area_style = SeriesAreaStyle.from_dict(_area_style)

        hidden = d.pop("hidden", UNSET)

        _label = d.pop("label", UNSET)
        label: Union[Unset, SeriesLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = SeriesLabel.from_dict(_label)

        y_axis_index = d.pop("yAxisIndex", UNSET)

        color = d.pop("color", UNSET)

        name = d.pop("name", UNSET)

        _stack_label = d.pop("stackLabel", UNSET)
        stack_label: Union[Unset, SeriesStackLabel]
        if isinstance(_stack_label, Unset):
            stack_label = UNSET
        else:
            stack_label = SeriesStackLabel.from_dict(_stack_label)

        stack = d.pop("stack", UNSET)

        series = cls(
            type=type,
            encode=encode,
            mark_line=mark_line,
            smooth=smooth,
            show_symbol=show_symbol,
            area_style=area_style,
            hidden=hidden,
            label=label,
            y_axis_index=y_axis_index,
            color=color,
            name=name,
            stack_label=stack_label,
            stack=stack,
        )

        series.additional_properties = d
        return series

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
