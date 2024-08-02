from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mark_line_data import MarkLineData
    from ..models.mark_line_label import MarkLineLabel
    from ..models.mark_line_line_style import MarkLineLineStyle


T = TypeVar("T", bound="MarkLine")


@_attrs_define
class MarkLine:
    """
    Attributes:
        data (List['MarkLineData']):
        label (Union[Unset, MarkLineLabel]):
        line_style (Union[Unset, MarkLineLineStyle]):
        symbol (Union[Unset, str]):
    """

    data: List["MarkLineData"]
    label: Union[Unset, "MarkLineLabel"] = UNSET
    line_style: Union[Unset, "MarkLineLineStyle"] = UNSET
    symbol: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        label: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        line_style: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_style, Unset):
            line_style = self.line_style.to_dict()

        symbol = self.symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if line_style is not UNSET:
            field_dict["lineStyle"] = line_style
        if symbol is not UNSET:
            field_dict["symbol"] = symbol

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mark_line_data import MarkLineData
        from ..models.mark_line_label import MarkLineLabel
        from ..models.mark_line_line_style import MarkLineLineStyle

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = MarkLineData.from_dict(data_item_data)

            data.append(data_item)

        _label = d.pop("label", UNSET)
        label: Union[Unset, MarkLineLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = MarkLineLabel.from_dict(_label)

        _line_style = d.pop("lineStyle", UNSET)
        line_style: Union[Unset, MarkLineLineStyle]
        if isinstance(_line_style, Unset):
            line_style = UNSET
        else:
            line_style = MarkLineLineStyle.from_dict(_line_style)

        symbol = d.pop("symbol", UNSET)

        mark_line = cls(
            data=data,
            label=label,
            line_style=line_style,
            symbol=symbol,
        )

        mark_line.additional_properties = d
        return mark_line

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
