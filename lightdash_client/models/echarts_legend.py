from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.echarts_legend_align import EchartsLegendAlign
from ..models.echarts_legend_icon import EchartsLegendIcon
from ..models.echarts_legend_orient import EchartsLegendOrient
from ..models.echarts_legend_type import EchartsLegendType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EchartsLegend")


@_attrs_define
class EchartsLegend:
    """
    Attributes:
        icon (Union[Unset, EchartsLegendIcon]):
        align (Union[Unset, EchartsLegendAlign]):
        height (Union[Unset, str]):
        width (Union[Unset, str]):
        left (Union[Unset, str]):
        bottom (Union[Unset, str]):
        right (Union[Unset, str]):
        top (Union[Unset, str]):
        orient (Union[Unset, EchartsLegendOrient]):
        type (Union[Unset, EchartsLegendType]):
        show (Union[Unset, bool]):
    """

    icon: Union[Unset, EchartsLegendIcon] = UNSET
    align: Union[Unset, EchartsLegendAlign] = UNSET
    height: Union[Unset, str] = UNSET
    width: Union[Unset, str] = UNSET
    left: Union[Unset, str] = UNSET
    bottom: Union[Unset, str] = UNSET
    right: Union[Unset, str] = UNSET
    top: Union[Unset, str] = UNSET
    orient: Union[Unset, EchartsLegendOrient] = UNSET
    type: Union[Unset, EchartsLegendType] = UNSET
    show: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        icon: Union[Unset, str] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.value

        align: Union[Unset, str] = UNSET
        if not isinstance(self.align, Unset):
            align = self.align.value

        height = self.height

        width = self.width

        left = self.left

        bottom = self.bottom

        right = self.right

        top = self.top

        orient: Union[Unset, str] = UNSET
        if not isinstance(self.orient, Unset):
            orient = self.orient.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        show = self.show

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if icon is not UNSET:
            field_dict["icon"] = icon
        if align is not UNSET:
            field_dict["align"] = align
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if left is not UNSET:
            field_dict["left"] = left
        if bottom is not UNSET:
            field_dict["bottom"] = bottom
        if right is not UNSET:
            field_dict["right"] = right
        if top is not UNSET:
            field_dict["top"] = top
        if orient is not UNSET:
            field_dict["orient"] = orient
        if type is not UNSET:
            field_dict["type"] = type
        if show is not UNSET:
            field_dict["show"] = show

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, EchartsLegendIcon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = EchartsLegendIcon(_icon)

        _align = d.pop("align", UNSET)
        align: Union[Unset, EchartsLegendAlign]
        if isinstance(_align, Unset):
            align = UNSET
        else:
            align = EchartsLegendAlign(_align)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        left = d.pop("left", UNSET)

        bottom = d.pop("bottom", UNSET)

        right = d.pop("right", UNSET)

        top = d.pop("top", UNSET)

        _orient = d.pop("orient", UNSET)
        orient: Union[Unset, EchartsLegendOrient]
        if isinstance(_orient, Unset):
            orient = UNSET
        else:
            orient = EchartsLegendOrient(_orient)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EchartsLegendType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EchartsLegendType(_type)

        show = d.pop("show", UNSET)

        echarts_legend = cls(
            icon=icon,
            align=align,
            height=height,
            width=width,
            left=left,
            bottom=bottom,
            right=right,
            top=top,
            orient=orient,
            type=type,
            show=show,
        )

        echarts_legend.additional_properties = d
        return echarts_legend

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
