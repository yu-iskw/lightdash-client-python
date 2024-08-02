from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummaryExtraFields")


@_attrs_define
class SummaryExtraFields:
    """
    Attributes:
        database_name (str):
        schema_name (str):
        description (Union[Unset, str]):
    """

    database_name: str
    schema_name: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        database_name = self.database_name

        schema_name = self.schema_name

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "databaseName": database_name,
                "schemaName": schema_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        database_name = d.pop("databaseName")

        schema_name = d.pop("schemaName")

        description = d.pop("description", UNSET)

        summary_extra_fields = cls(
            database_name=database_name,
            schema_name=schema_name,
            description=description,
        )

        summary_extra_fields.additional_properties = d
        return summary_extra_fields

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
