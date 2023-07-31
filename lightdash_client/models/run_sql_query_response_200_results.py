from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.run_sql_query_response_200_results_fields import (
        RunSqlQueryResponse200ResultsFields,
    )
    from ..models.run_sql_query_response_200_results_rows_item import (
        RunSqlQueryResponse200ResultsRowsItem,
    )


T = TypeVar("T", bound="RunSqlQueryResponse200Results")


@attr.s(auto_attribs=True)
class RunSqlQueryResponse200Results:
    """
    Attributes:
        rows (List['RunSqlQueryResponse200ResultsRowsItem']):
        fields (RunSqlQueryResponse200ResultsFields): Construct a type with a set of properties K of type T
    """

    rows: List["RunSqlQueryResponse200ResultsRowsItem"]
    fields: "RunSqlQueryResponse200ResultsFields"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()

            rows.append(rows_item)

        fields = self.fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.run_sql_query_response_200_results_fields import (
            RunSqlQueryResponse200ResultsFields,
        )
        from ..models.run_sql_query_response_200_results_rows_item import (
            RunSqlQueryResponse200ResultsRowsItem,
        )

        d = src_dict.copy()
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = RunSqlQueryResponse200ResultsRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        fields = RunSqlQueryResponse200ResultsFields.from_dict(d.pop("fields"))

        run_sql_query_response_200_results = cls(
            rows=rows,
            fields=fields,
        )

        run_sql_query_response_200_results.additional_properties = d
        return run_sql_query_response_200_results

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
