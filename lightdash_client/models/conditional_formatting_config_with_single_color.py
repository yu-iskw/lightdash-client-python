from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.conditional_formatting_with_conditional_operator import (
        ConditionalFormattingWithConditionalOperator,
    )
    from ..models.field_target import FieldTarget


T = TypeVar("T", bound="ConditionalFormattingConfigWithSingleColor")


@_attrs_define
class ConditionalFormattingConfigWithSingleColor:
    """
    Attributes:
        rules (List['ConditionalFormattingWithConditionalOperator']):
        color (str):
        target (Union['FieldTarget', None]):
    """

    rules: List["ConditionalFormattingWithConditionalOperator"]
    color: str
    target: Union["FieldTarget", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.field_target import FieldTarget

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        color = self.color

        target: Union[Dict[str, Any], None]
        if isinstance(self.target, FieldTarget):
            target = self.target.to_dict()
        else:
            target = self.target

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rules": rules,
                "color": color,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.conditional_formatting_with_conditional_operator import (
            ConditionalFormattingWithConditionalOperator,
        )
        from ..models.field_target import FieldTarget

        d = src_dict.copy()
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = ConditionalFormattingWithConditionalOperator.from_dict(rules_item_data)

            rules.append(rules_item)

        color = d.pop("color")

        def _parse_target(data: object) -> Union["FieldTarget", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_type_1 = FieldTarget.from_dict(data)

                return target_type_1
            except:  # noqa: E722
                pass
            return cast(Union["FieldTarget", None], data)

        target = _parse_target(d.pop("target"))

        conditional_formatting_config_with_single_color = cls(
            rules=rules,
            color=color,
            target=target,
        )

        conditional_formatting_config_with_single_color.additional_properties = d
        return conditional_formatting_config_with_single_color

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
