from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.conditional_formatting_with_conditional_operator import (
        ConditionalFormattingWithConditionalOperator,
    )
    from ..models.field_target import FieldTarget


T = TypeVar("T", bound="ConditionalFormattingConfigWithSingleColor")


@attr.s(auto_attribs=True)
class ConditionalFormattingConfigWithSingleColor:
    """
    Attributes:
        rules (List['ConditionalFormattingWithConditionalOperator']):
        color (str):
        target (Optional[FieldTarget]):
    """

    rules: List["ConditionalFormattingWithConditionalOperator"]
    color: str
    target: Optional["FieldTarget"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()

            rules.append(rules_item)

        color = self.color
        target = self.target.to_dict() if self.target else None

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

        _target = d.pop("target")
        target: Optional[FieldTarget]
        if _target is None:
            target = None
        else:
            target = FieldTarget.from_dict(_target)

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
