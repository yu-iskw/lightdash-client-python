from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.record_string_type_dimension_type import RecordStringTypeDimensionType
    from ..models.record_string_unknown import RecordStringUnknown


T = TypeVar("T", bound="ApiSqlQueryResults")


@_attrs_define
class ApiSqlQueryResults:
    """
    Attributes:
        rows (List['RecordStringUnknown']):
        fields (RecordStringTypeDimensionType): Construct a type with a set of properties K of type T
    """

    rows: List["RecordStringUnknown"]
    fields: "RecordStringTypeDimensionType"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        from ..models.record_string_type_dimension_type import (
            RecordStringTypeDimensionType,
        )
        from ..models.record_string_unknown import RecordStringUnknown

        d = src_dict.copy()
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = RecordStringUnknown.from_dict(rows_item_data)

            rows.append(rows_item)

        fields = RecordStringTypeDimensionType.from_dict(d.pop("fields"))

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
