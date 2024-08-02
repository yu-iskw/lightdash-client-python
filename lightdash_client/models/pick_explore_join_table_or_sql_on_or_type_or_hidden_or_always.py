from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dbt_model_join_type import DbtModelJoinType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PickExploreJoinTableOrSqlOnOrTypeOrHiddenOrAlways")


@_attrs_define
class PickExploreJoinTableOrSqlOnOrTypeOrHiddenOrAlways:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        table (str):
        sql_on (str):
        type (Union[Unset, DbtModelJoinType]):
        hidden (Union[Unset, bool]):
        always (Union[Unset, bool]):
    """

    table: str
    sql_on: str
    type: Union[Unset, DbtModelJoinType] = UNSET
    hidden: Union[Unset, bool] = UNSET
    always: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table = self.table

        sql_on = self.sql_on

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        hidden = self.hidden

        always = self.always

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table": table,
                "sqlOn": sql_on,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if always is not UNSET:
            field_dict["always"] = always

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table = d.pop("table")

        sql_on = d.pop("sqlOn")

        _type = d.pop("type", UNSET)
        type: Union[Unset, DbtModelJoinType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DbtModelJoinType(_type)

        hidden = d.pop("hidden", UNSET)

        always = d.pop("always", UNSET)

        pick_explore_join_table_or_sql_on_or_type_or_hidden_or_always = cls(
            table=table,
            sql_on=sql_on,
            type=type,
            hidden=hidden,
            always=always,
        )

        pick_explore_join_table_or_sql_on_or_type_or_hidden_or_always.additional_properties = d
        return pick_explore_join_table_or_sql_on_or_type_or_hidden_or_always

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
