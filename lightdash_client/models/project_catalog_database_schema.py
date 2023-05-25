from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

import attr

if TYPE_CHECKING:
    from ..models.project_catalog_database_schema_table import ProjectCatalogDatabaseSchemaTable


T = TypeVar("T", bound="ProjectCatalogDatabaseSchema")


@attr.s(auto_attribs=True)
class ProjectCatalogDatabaseSchema:
    """ """

    additional_properties: Dict[str, "ProjectCatalogDatabaseSchemaTable"] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_catalog_database_schema_table import ProjectCatalogDatabaseSchemaTable

        d = src_dict.copy()
        project_catalog_database_schema = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ProjectCatalogDatabaseSchemaTable.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        project_catalog_database_schema.additional_properties = additional_properties
        return project_catalog_database_schema

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ProjectCatalogDatabaseSchemaTable":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ProjectCatalogDatabaseSchemaTable") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
