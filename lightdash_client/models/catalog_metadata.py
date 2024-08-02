from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_field import CatalogField


T = TypeVar("T", bound="CatalogMetadata")


@_attrs_define
class CatalogMetadata:
    """
    Attributes:
        joined_tables (List[str]):
        fields (List['CatalogField']):
        model_name (str):
        name (str):
        source (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    joined_tables: List[str]
    fields: List["CatalogField"]
    model_name: str
    name: str
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        joined_tables = self.joined_tables

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        model_name = self.model_name

        name = self.name

        source = self.source

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "joinedTables": joined_tables,
                "fields": fields,
                "modelName": model_name,
                "name": name,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_field import CatalogField

        d = src_dict.copy()
        joined_tables = cast(List[str], d.pop("joinedTables"))

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = CatalogField.from_dict(fields_item_data)

            fields.append(fields_item)

        model_name = d.pop("modelName")

        name = d.pop("name")

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        catalog_metadata = cls(
            joined_tables=joined_tables,
            fields=fields,
            model_name=model_name,
            name=name,
            source=source,
            description=description,
        )

        catalog_metadata.additional_properties = d
        return catalog_metadata

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
