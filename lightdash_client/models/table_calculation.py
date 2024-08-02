from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.table_calculation_type import TableCalculationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format import CustomFormat


T = TypeVar("T", bound="TableCalculation")


@_attrs_define
class TableCalculation:
    """
    Attributes:
        sql (str):
        display_name (str):
        name (str):
        type (Union[Unset, TableCalculationType]):
        format_ (Union[Unset, CustomFormat]):
        index (Union[Unset, float]):
    """

    sql: str
    display_name: str
    name: str
    type: Union[Unset, TableCalculationType] = UNSET
    format_: Union[Unset, "CustomFormat"] = UNSET
    index: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sql = self.sql

        display_name = self.display_name

        name = self.name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        format_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

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
        if type is not UNSET:
            field_dict["type"] = type
        if format_ is not UNSET:
            field_dict["format"] = format_
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_format import CustomFormat

        d = src_dict.copy()
        sql = d.pop("sql")

        display_name = d.pop("displayName")

        name = d.pop("name")

        _type = d.pop("type", UNSET)
        type: Union[Unset, TableCalculationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TableCalculationType(_type)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, CustomFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = CustomFormat.from_dict(_format_)

        index = d.pop("index", UNSET)

        table_calculation = cls(
            sql=sql,
            display_name=display_name,
            name=name,
            type=type,
            format_=format_,
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
