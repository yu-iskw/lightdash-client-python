from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.query_result_column_id_value import QueryResultColumnIdValue


T = TypeVar("T", bound="QueryResultColumnId")


@attr.s(auto_attribs=True)
class QueryResultColumnId:
    """
    Attributes:
        value (Union[Unset, QueryResultColumnIdValue]):
    """

    value: Union[Unset, "QueryResultColumnIdValue"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_result_column_id_value import QueryResultColumnIdValue

        d = src_dict.copy()
        _value = d.pop("value", UNSET)
        value: Union[Unset, QueryResultColumnIdValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = QueryResultColumnIdValue.from_dict(_value)

        query_result_column_id = cls(
            value=value,
        )

        query_result_column_id.additional_properties = d
        return query_result_column_id

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
