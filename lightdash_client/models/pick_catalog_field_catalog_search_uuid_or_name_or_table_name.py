from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickCatalogFieldCatalogSearchUuidOrNameOrTableName")


@_attrs_define
class PickCatalogFieldCatalogSearchUuidOrNameOrTableName:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        table_name (str):
        catalog_search_uuid (str):
    """

    name: str
    table_name: str
    catalog_search_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        table_name = self.table_name

        catalog_search_uuid = self.catalog_search_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "tableName": table_name,
                "catalogSearchUuid": catalog_search_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        table_name = d.pop("tableName")

        catalog_search_uuid = d.pop("catalogSearchUuid")

        pick_catalog_field_catalog_search_uuid_or_name_or_table_name = cls(
            name=name,
            table_name=table_name,
            catalog_search_uuid=catalog_search_uuid,
        )

        pick_catalog_field_catalog_search_uuid_or_name_or_table_name.additional_properties = d
        return pick_catalog_field_catalog_search_uuid_or_name_or_table_name

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
