from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_properties import ColumnProperties


T = TypeVar("T", bound="RecordStringColumnProperties")


@_attrs_define
class RecordStringColumnProperties:
    """Construct a type with a set of properties K of type T"""

    additional_properties: Dict[str, "ColumnProperties"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.column_properties import ColumnProperties

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_properties import ColumnProperties

        d = src_dict.copy()
        record_string_column_properties = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ColumnProperties.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        record_string_column_properties.additional_properties = additional_properties
        return record_string_column_properties

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ColumnProperties":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ColumnProperties") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
