from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spotlight_table_columns import SpotlightTableColumns
from ..types import UNSET, Unset

T = TypeVar("T", bound="ColumnConfigItem")


@_attrs_define
class ColumnConfigItem:
    """
    Attributes:
        is_visible (bool):
        column (SpotlightTableColumns):
    """

    is_visible: bool
    column: SpotlightTableColumns
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_visible = self.is_visible

        column = self.column.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isVisible": is_visible,
                "column": column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_visible = d.pop("isVisible")

        column = SpotlightTableColumns(d.pop("column"))

        column_config_item = cls(
            is_visible=is_visible,
            column=column,
        )

        column_config_item.additional_properties = d
        return column_config_item

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
