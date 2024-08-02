from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialSummaryExtraFields")


@_attrs_define
class PartialSummaryExtraFields:
    """Make all properties in T optional

    Attributes:
        description (Union[Unset, str]):
        schema_name (Union[Unset, str]):
        database_name (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    schema_name: Union[Unset, str] = UNSET
    database_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        schema_name = self.schema_name

        database_name = self.database_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if schema_name is not UNSET:
            field_dict["schemaName"] = schema_name
        if database_name is not UNSET:
            field_dict["databaseName"] = database_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        schema_name = d.pop("schemaName", UNSET)

        database_name = d.pop("databaseName", UNSET)

        partial_summary_extra_fields = cls(
            description=description,
            schema_name=schema_name,
            database_name=database_name,
        )

        partial_summary_extra_fields.additional_properties = d
        return partial_summary_extra_fields

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
