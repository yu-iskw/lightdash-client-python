from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_type import FieldType
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
        label (str):
        name (str):
        field_type (Union[Unset, FieldType]):
        table_label (Union[Unset, str]):
        source (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    joined_tables: List[str]
    fields: List["CatalogField"]
    model_name: str
    label: str
    name: str
    field_type: Union[Unset, FieldType] = UNSET
    table_label: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.catalog_field import CatalogField

        joined_tables = self.joined_tables

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        model_name = self.model_name

        label = self.label

        name = self.name

        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        table_label = self.table_label

        source = self.source

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "joinedTables": joined_tables,
                "fields": fields,
                "modelName": model_name,
                "label": label,
                "name": name,
            }
        )
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if table_label is not UNSET:
            field_dict["tableLabel"] = table_label
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

        label = d.pop("label")

        name = d.pop("name")

        _field_type = d.pop("fieldType", UNSET)
        field_type: Union[Unset, FieldType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = FieldType(_field_type)

        table_label = d.pop("tableLabel", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        catalog_metadata = cls(
            joined_tables=joined_tables,
            fields=fields,
            model_name=model_name,
            label=label,
            name=name,
            field_type=field_type,
            table_label=table_label,
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
