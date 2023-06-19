from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="DbtProjectEnvironmentVariable")


@attr.s(auto_attribs=True)
class DbtProjectEnvironmentVariable:
    """
    Attributes:
        value (str):
        key (str):
    """

    value: str
    key: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        key = d.pop("key")

        dbt_project_environment_variable = cls(
            value=value,
            key=key,
        )

        dbt_project_environment_variable.additional_properties = d
        return dbt_project_environment_variable

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
