from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

import attr

if TYPE_CHECKING:
    from ..models.query_result_column_id import QueryResultColumnId


T = TypeVar("T", bound="QueryResult")


@attr.s(auto_attribs=True)
class QueryResult:
    """ """

    additional_properties: Dict[str, "QueryResultColumnId"] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_result_column_id import QueryResultColumnId

        d = src_dict.copy()
        query_result = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = QueryResultColumnId.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        query_result.additional_properties = additional_properties
        return query_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "QueryResultColumnId":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "QueryResultColumnId") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
