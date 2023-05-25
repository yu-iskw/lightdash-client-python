from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="ProjectCatalogDatabaseSchemaTable")


@attr.s(auto_attribs=True)
class ProjectCatalogDatabaseSchemaTable:
    """
    Attributes:
        sql_table (str):
        description (Union[Unset, str]):
    """

    sql_table: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sql_table = self.sql_table
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sqlTable": sql_table,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sql_table = d.pop("sqlTable")

        description = d.pop("description", UNSET)

        project_catalog_database_schema_table = cls(
            sql_table=sql_table,
            description=description,
        )

        project_catalog_database_schema_table.additional_properties = d
        return project_catalog_database_schema_table

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
