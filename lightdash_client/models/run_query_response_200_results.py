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
    from ..models.query_result import QueryResult


T = TypeVar("T", bound="RunQueryResponse200Results")


@attr.s(auto_attribs=True)
class RunQueryResponse200Results:
    """
    Attributes:
        rows (Union[Unset, List['QueryResult']]):
    """

    rows: Union[Unset, List["QueryResult"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()

                rows.append(rows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_result import QueryResult

        d = src_dict.copy()
        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = QueryResult.from_dict(rows_item_data)

            rows.append(rows_item)

        run_query_response_200_results = cls(
            rows=rows,
        )

        run_query_response_200_results.additional_properties = d
        return run_query_response_200_results

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
