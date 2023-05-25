from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="CreateSavedChartVersionPivotConfig")


@attr.s(auto_attribs=True)
class CreateSavedChartVersionPivotConfig:
    """
    Attributes:
        columns (List[str]):
    """

    columns: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        columns = self.columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        columns = cast(List[str], d.pop("columns"))

        create_saved_chart_version_pivot_config = cls(
            columns=columns,
        )

        create_saved_chart_version_pivot_config.additional_properties = d
        return create_saved_chart_version_pivot_config

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
