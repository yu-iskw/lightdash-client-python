from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conditional_formatting_config_with_color_range_color_steps import (
    ConditionalFormattingConfigWithColorRangeColorSteps,
)

T = TypeVar("T", bound="ConditionalFormattingConfigWithColorRangeColor")


@_attrs_define
class ConditionalFormattingConfigWithColorRangeColor:
    """
    Attributes:
        steps (ConditionalFormattingConfigWithColorRangeColorSteps):
        end (str):
        start (str):
    """

    steps: ConditionalFormattingConfigWithColorRangeColorSteps
    end: str
    start: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        steps = self.steps.value

        end = self.end

        start = self.start

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
                "end": end,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        steps = ConditionalFormattingConfigWithColorRangeColorSteps(d.pop("steps"))

        end = d.pop("end")

        start = d.pop("start")

        conditional_formatting_config_with_color_range_color = cls(
            steps=steps,
            end=end,
            start=start,
        )

        conditional_formatting_config_with_color_range_color.additional_properties = d
        return conditional_formatting_config_with_color_range_color

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
