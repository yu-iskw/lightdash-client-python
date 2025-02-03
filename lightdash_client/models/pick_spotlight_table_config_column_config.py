from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_config_item import ColumnConfigItem


T = TypeVar("T", bound="PickSpotlightTableConfigColumnConfig")


@_attrs_define
class PickSpotlightTableConfigColumnConfig:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        column_config (List['ColumnConfigItem']):
    """

    column_config: List["ColumnConfigItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.column_config_item import ColumnConfigItem

        column_config = []
        for componentsschemas_column_config_item_data in self.column_config:
            componentsschemas_column_config_item = componentsschemas_column_config_item_data.to_dict()
            column_config.append(componentsschemas_column_config_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnConfig": column_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_config_item import ColumnConfigItem

        d = src_dict.copy()
        column_config = []
        _column_config = d.pop("columnConfig")
        for componentsschemas_column_config_item_data in _column_config:
            componentsschemas_column_config_item = ColumnConfigItem.from_dict(componentsschemas_column_config_item_data)

            column_config.append(componentsschemas_column_config_item)

        pick_spotlight_table_config_column_config = cls(
            column_config=column_config,
        )

        pick_spotlight_table_config_column_config.additional_properties = d
        return pick_spotlight_table_config_column_config

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
