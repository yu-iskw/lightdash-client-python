from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_string_type_dimension_type_additional_property import (
        RecordStringTypeDimensionTypeAdditionalProperty,
    )


T = TypeVar("T", bound="RecordStringTypeDimensionType")


@_attrs_define
class RecordStringTypeDimensionType:
    """Construct a type with a set of properties K of type T"""

    additional_properties: Dict[str, "RecordStringTypeDimensionTypeAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        from ..models.record_string_type_dimension_type_additional_property import (
            RecordStringTypeDimensionTypeAdditionalProperty,
        )

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_string_type_dimension_type_additional_property import (
            RecordStringTypeDimensionTypeAdditionalProperty,
        )

        d = src_dict.copy()
        record_string_type_dimension_type = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RecordStringTypeDimensionTypeAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        record_string_type_dimension_type.additional_properties = additional_properties
        return record_string_type_dimension_type

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "RecordStringTypeDimensionTypeAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "RecordStringTypeDimensionTypeAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
