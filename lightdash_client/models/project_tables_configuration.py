from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

import attr

if TYPE_CHECKING:
    from ..models.project_tables_configuration_table_selection import ProjectTablesConfigurationTableSelection


T = TypeVar("T", bound="ProjectTablesConfiguration")


@attr.s(auto_attribs=True)
class ProjectTablesConfiguration:
    """
    Attributes:
        table_selection (ProjectTablesConfigurationTableSelection):
    """

    table_selection: "ProjectTablesConfigurationTableSelection"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_selection = self.table_selection.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableSelection": table_selection,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_tables_configuration_table_selection import ProjectTablesConfigurationTableSelection

        d = src_dict.copy()
        table_selection = ProjectTablesConfigurationTableSelection.from_dict(d.pop("tableSelection"))

        project_tables_configuration = cls(
            table_selection=table_selection,
        )

        project_tables_configuration.additional_properties = d
        return project_tables_configuration

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
