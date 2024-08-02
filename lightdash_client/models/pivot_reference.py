from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pivot_value import PivotValue


T = TypeVar("T", bound="PivotReference")


@_attrs_define
class PivotReference:
    """
    Attributes:
        field (str):
        pivot_values (Union[Unset, List['PivotValue']]):
    """

    field: str
    pivot_values: Union[Unset, List["PivotValue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field = self.field

        pivot_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pivot_values, Unset):
            pivot_values = []
            for pivot_values_item_data in self.pivot_values:
                pivot_values_item = pivot_values_item_data.to_dict()
                pivot_values.append(pivot_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
            }
        )
        if pivot_values is not UNSET:
            field_dict["pivotValues"] = pivot_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pivot_value import PivotValue

        d = src_dict.copy()
        field = d.pop("field")

        pivot_values = []
        _pivot_values = d.pop("pivotValues", UNSET)
        for pivot_values_item_data in _pivot_values or []:
            pivot_values_item = PivotValue.from_dict(pivot_values_item_data)

            pivot_values.append(pivot_values_item)

        pivot_reference = cls(
            field=field,
            pivot_values=pivot_values,
        )

        pivot_reference.additional_properties = d
        return pivot_reference

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
