from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.conditional_formatting_config_with_color_range_color import (
        ConditionalFormattingConfigWithColorRangeColor,
    )
    from ..models.conditional_formatting_with_range import (
        ConditionalFormattingWithRange,
    )
    from ..models.field_target import FieldTarget


T = TypeVar("T", bound="ConditionalFormattingConfigWithColorRange")


@attr.s(auto_attribs=True)
class ConditionalFormattingConfigWithColorRange:
    """
    Attributes:
        rule (ConditionalFormattingWithRange):
        color (ConditionalFormattingConfigWithColorRangeColor):
        target (Optional[FieldTarget]):
    """

    rule: "ConditionalFormattingWithRange"
    color: "ConditionalFormattingConfigWithColorRangeColor"
    target: Optional["FieldTarget"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rule = self.rule.to_dict()

        color = self.color.to_dict()

        target = self.target.to_dict() if self.target else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
                "color": color,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.conditional_formatting_config_with_color_range_color import (
            ConditionalFormattingConfigWithColorRangeColor,
        )
        from ..models.conditional_formatting_with_range import (
            ConditionalFormattingWithRange,
        )
        from ..models.field_target import FieldTarget

        d = src_dict.copy()
        rule = ConditionalFormattingWithRange.from_dict(d.pop("rule"))

        color = ConditionalFormattingConfigWithColorRangeColor.from_dict(d.pop("color"))

        _target = d.pop("target")
        target: Optional[FieldTarget]
        if _target is None:
            target = None
        else:
            target = FieldTarget.from_dict(_target)

        conditional_formatting_config_with_color_range = cls(
            rule=rule,
            color=color,
            target=target,
        )

        conditional_formatting_config_with_color_range.additional_properties = d
        return conditional_formatting_config_with_color_range

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
