from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compact import Compact
from ..models.compact_or_alias_type_1 import CompactOrAliasType1
from ..models.comparison_format_types import ComparisonFormatTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="BigNumber")


@_attrs_define
class BigNumber:
    """
    Attributes:
        comparison_label (Union[Unset, str]):
        flip_colors (Union[Unset, bool]):
        comparison_format (Union[Unset, ComparisonFormatTypes]):
        show_comparison (Union[Unset, bool]):
        show_big_number_label (Union[Unset, bool]):
        selected_field (Union[Unset, str]):
        style (Union[Compact, CompactOrAliasType1, Unset]):
        label (Union[Unset, str]):
    """

    comparison_label: Union[Unset, str] = UNSET
    flip_colors: Union[Unset, bool] = UNSET
    comparison_format: Union[Unset, ComparisonFormatTypes] = UNSET
    show_comparison: Union[Unset, bool] = UNSET
    show_big_number_label: Union[Unset, bool] = UNSET
    selected_field: Union[Unset, str] = UNSET
    style: Union[Compact, CompactOrAliasType1, Unset] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comparison_label = self.comparison_label

        flip_colors = self.flip_colors

        comparison_format: Union[Unset, str] = UNSET
        if not isinstance(self.comparison_format, Unset):
            comparison_format = self.comparison_format.value

        show_comparison = self.show_comparison

        show_big_number_label = self.show_big_number_label

        selected_field = self.selected_field

        style: Union[Unset, str]
        if isinstance(self.style, Unset):
            style = UNSET
        elif isinstance(self.style, Compact):
            style = self.style.value
        else:
            style = self.style.value

        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comparison_label is not UNSET:
            field_dict["comparisonLabel"] = comparison_label
        if flip_colors is not UNSET:
            field_dict["flipColors"] = flip_colors
        if comparison_format is not UNSET:
            field_dict["comparisonFormat"] = comparison_format
        if show_comparison is not UNSET:
            field_dict["showComparison"] = show_comparison
        if show_big_number_label is not UNSET:
            field_dict["showBigNumberLabel"] = show_big_number_label
        if selected_field is not UNSET:
            field_dict["selectedField"] = selected_field
        if style is not UNSET:
            field_dict["style"] = style
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        comparison_label = d.pop("comparisonLabel", UNSET)

        flip_colors = d.pop("flipColors", UNSET)

        _comparison_format = d.pop("comparisonFormat", UNSET)
        comparison_format: Union[Unset, ComparisonFormatTypes]
        if isinstance(_comparison_format, Unset):
            comparison_format = UNSET
        else:
            comparison_format = ComparisonFormatTypes(_comparison_format)

        show_comparison = d.pop("showComparison", UNSET)

        show_big_number_label = d.pop("showBigNumberLabel", UNSET)

        selected_field = d.pop("selectedField", UNSET)

        def _parse_style(data: object) -> Union[Compact, CompactOrAliasType1, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_compact_or_alias_type_0 = Compact(data)

                return componentsschemas_compact_or_alias_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            componentsschemas_compact_or_alias_type_1 = CompactOrAliasType1(data)

            return componentsschemas_compact_or_alias_type_1

        style = _parse_style(d.pop("style", UNSET))

        label = d.pop("label", UNSET)

        big_number = cls(
            comparison_label=comparison_label,
            flip_colors=flip_colors,
            comparison_format=comparison_format,
            show_comparison=show_comparison,
            show_big_number_label=show_big_number_label,
            selected_field=selected_field,
            style=style,
            label=label,
        )

        big_number.additional_properties = d
        return big_number

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
