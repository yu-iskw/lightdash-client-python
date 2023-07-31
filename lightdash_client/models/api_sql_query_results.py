from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_sql_query_results_fields import ApiSqlQueryResultsFields
    from ..models.api_sql_query_results_rows_item import ApiSqlQueryResultsRowsItem


T = TypeVar("T", bound="ApiSqlQueryResults")


@attr.s(auto_attribs=True)
class ApiSqlQueryResults:
    """
    Attributes:
        rows (List['ApiSqlQueryResultsRowsItem']):
        fields (ApiSqlQueryResultsFields): Construct a type with a set of properties K of type T
    """

    rows: List["ApiSqlQueryResultsRowsItem"]
    fields: "ApiSqlQueryResultsFields"
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
        from ..models.api_sql_query_results_fields import ApiSqlQueryResultsFields
        from ..models.api_sql_query_results_rows_item import ApiSqlQueryResultsRowsItem

        d = src_dict.copy()
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = ApiSqlQueryResultsRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        fields = ApiSqlQueryResultsFields.from_dict(d.pop("fields"))

        api_sql_query_results = cls(
            rows=rows,
            fields=fields,
        )

        api_sql_query_results.additional_properties = d
        return api_sql_query_results

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
