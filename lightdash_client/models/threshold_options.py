from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.threshold_operator import ThresholdOperator

T = TypeVar("T", bound="ThresholdOptions")


@_attrs_define
class ThresholdOptions:
    """
    Attributes:
        value (float):
        field_id (str):
        operator (ThresholdOperator):
    """

    value: float
    field_id: str
    operator: ThresholdOperator
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        field_id = self.field_id

        operator = self.operator.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "fieldId": field_id,
                "operator": operator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        field_id = d.pop("fieldId")

        operator = ThresholdOperator(d.pop("operator"))

        threshold_options = cls(
            value=value,
            field_id=field_id,
            operator=operator,
        )

        threshold_options.additional_properties = d
        return threshold_options

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
