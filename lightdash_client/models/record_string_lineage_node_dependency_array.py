from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lineage_node_dependency import LineageNodeDependency


T = TypeVar("T", bound="RecordStringLineageNodeDependencyArray")


@_attrs_define
class RecordStringLineageNodeDependencyArray:
    """Construct a type with a set of properties K of type T"""

    additional_properties: Dict[str, List["LineageNodeDependency"]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.lineage_node_dependency import LineageNodeDependency

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()
                field_dict[prop_name].append(additional_property_item)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lineage_node_dependency import LineageNodeDependency

        d = src_dict.copy()
        record_string_lineage_node_dependency_array = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = LineageNodeDependency.from_dict(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        record_string_lineage_node_dependency_array.additional_properties = additional_properties
        return record_string_lineage_node_dependency_array

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List["LineageNodeDependency"]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List["LineageNodeDependency"]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
