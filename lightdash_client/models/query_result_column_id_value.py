from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="QueryResultColumnIdValue")


@attr.s(auto_attribs=True)
class QueryResultColumnIdValue:
    """
    Attributes:
        raw (Union[Unset, Any]):
        formatted (Union[Unset, Any]):
    """

    raw: Union[Unset, Any] = UNSET
    formatted: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        raw = self.raw
        formatted = self.formatted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if raw is not UNSET:
            field_dict["raw"] = raw
        if formatted is not UNSET:
            field_dict["formatted"] = formatted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        raw = d.pop("raw", UNSET)

        formatted = d.pop("formatted", UNSET)

        query_result_column_id_value = cls(
            raw=raw,
            formatted=formatted,
        )

        query_result_column_id_value.additional_properties = d
        return query_result_column_id_value

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
