from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_dimension_type_sql import CustomDimensionTypeSQL
from ..models.dimension_type import DimensionType

T = TypeVar("T", bound="CustomSqlDimension")


@_attrs_define
class CustomSqlDimension:
    """
    Attributes:
        id (str):
        name (str):
        table (str):
        type (CustomDimensionTypeSQL):
        sql (str):
        dimension_type (DimensionType):
    """

    id: str
    name: str
    table: str
    type: CustomDimensionTypeSQL
    sql: str
    dimension_type: DimensionType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        table = self.table

        type = self.type.value

        sql = self.sql

        dimension_type = self.dimension_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "table": table,
                "type": type,
                "sql": sql,
                "dimensionType": dimension_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        table = d.pop("table")

        type = CustomDimensionTypeSQL(d.pop("type"))

        sql = d.pop("sql")

        dimension_type = DimensionType(d.pop("dimensionType"))

        custom_sql_dimension = cls(
            id=id,
            name=name,
            table=table,
            type=type,
            sql=sql,
            dimension_type=dimension_type,
        )

        custom_sql_dimension.additional_properties = d
        return custom_sql_dimension

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
