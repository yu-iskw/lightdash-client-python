from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="TableCalculation")


@attr.s(auto_attribs=True)
class TableCalculation:
    """
    Attributes:
        sql (str):
        display_name (str):
        name (str):
        index (Union[Unset, float]):
    """

    sql: str
    display_name: str
    name: str
    index: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sql = self.sql
        display_name = self.display_name
        name = self.name
        index = self.index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sql": sql,
                "displayName": display_name,
                "name": name,
            }
        )
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sql = d.pop("sql")

        display_name = d.pop("displayName")

        name = d.pop("name")

        index = d.pop("index", UNSET)

        table_calculation = cls(
            sql=sql,
            display_name=display_name,
            name=name,
            index=index,
        )

        table_calculation.additional_properties = d
        return table_calculation

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
