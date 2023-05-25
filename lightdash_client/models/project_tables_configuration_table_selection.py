from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

import attr

from ..models.project_tables_configuration_table_selection_type import ProjectTablesConfigurationTableSelectionType

T = TypeVar("T", bound="ProjectTablesConfigurationTableSelection")


@attr.s(auto_attribs=True)
class ProjectTablesConfigurationTableSelection:
    """
    Attributes:
        type (ProjectTablesConfigurationTableSelectionType):
        value (Optional[List[str]]):
    """

    type: ProjectTablesConfigurationTableSelectionType
    value: Optional[List[str]]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        if self.value is None:
            value = None
        else:
            value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ProjectTablesConfigurationTableSelectionType(d.pop("type"))

        value = cast(List[str], d.pop("value"))

        project_tables_configuration_table_selection = cls(
            type=type,
            value=value,
        )

        project_tables_configuration_table_selection.additional_properties = d
        return project_tables_configuration_table_selection

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
