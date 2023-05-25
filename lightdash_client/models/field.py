from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="Field")


@attr.s(auto_attribs=True)
class Field:
    """
    Attributes:
        field_type (str):
        type (str):
        name (str):
        label (str):
        table (str):
        table_label (str):
        sql (str):
        description (Union[Unset, str]):
    """

    field_type: str
    type: str
    name: str
    label: str
    table: str
    table_label: str
    sql: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type
        type = self.type
        name = self.name
        label = self.label
        table = self.table
        table_label = self.table_label
        sql = self.sql
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldType": field_type,
                "type": type,
                "name": name,
                "label": label,
                "table": table,
                "tableLabel": table_label,
                "sql": sql,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_type = d.pop("fieldType")

        type = d.pop("type")

        name = d.pop("name")

        label = d.pop("label")

        table = d.pop("table")

        table_label = d.pop("tableLabel")

        sql = d.pop("sql")

        description = d.pop("description", UNSET)

        field = cls(
            field_type=field_type,
            type=type,
            name=name,
            label=label,
            table=table,
            table_label=table_label,
            sql=sql,
            description=description,
        )

        field.additional_properties = d
        return field

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
