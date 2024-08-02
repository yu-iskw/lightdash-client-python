from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conditional_operator import ConditionalOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConditionalRuleConditionalOperatorNumber")


@_attrs_define
class ConditionalRuleConditionalOperatorNumber:
    """
    Attributes:
        operator (ConditionalOperator):
        id (str):
        values (Union[Unset, List[float]]):
    """

    operator: ConditionalOperator
    id: str
    values: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operator = self.operator.value

        id = self.id

        values: Union[Unset, List[float]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
                "id": id,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operator = ConditionalOperator(d.pop("operator"))

        id = d.pop("id")

        values = cast(List[float], d.pop("values", UNSET))

        conditional_rule_conditional_operator_number = cls(
            operator=operator,
            id=id,
            values=values,
        )

        conditional_rule_conditional_operator_number.additional_properties = d
        return conditional_rule_conditional_operator_number

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
