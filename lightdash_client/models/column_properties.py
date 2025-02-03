from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColumnProperties")


@_attrs_define
class ColumnProperties:
    """
    Attributes:
        frozen (Union[Unset, bool]):
        name (Union[Unset, str]):
        visible (Union[Unset, bool]):
    """

    frozen: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        frozen = self.frozen

        name = self.name

        visible = self.visible

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if frozen is not UNSET:
            field_dict["frozen"] = frozen
        if name is not UNSET:
            field_dict["name"] = name
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        frozen = d.pop("frozen", UNSET)

        name = d.pop("name", UNSET)

        visible = d.pop("visible", UNSET)

        column_properties = cls(
            frozen=frozen,
            name=name,
            visible=visible,
        )

        column_properties.additional_properties = d
        return column_properties

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
