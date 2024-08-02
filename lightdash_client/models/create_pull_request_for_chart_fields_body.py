from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_pull_request_for_chart_fields_body_quote_char import (
    CreatePullRequestForChartFieldsBodyQuoteChar,
)

T = TypeVar("T", bound="CreatePullRequestForChartFieldsBody")


@_attrs_define
class CreatePullRequestForChartFieldsBody:
    """
    Attributes:
        quote_char (CreatePullRequestForChartFieldsBodyQuoteChar):
        custom_metrics (List[str]):
    """

    quote_char: CreatePullRequestForChartFieldsBodyQuoteChar
    custom_metrics: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quote_char = self.quote_char.value

        custom_metrics = self.custom_metrics

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quoteChar": quote_char,
                "customMetrics": custom_metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quote_char = CreatePullRequestForChartFieldsBodyQuoteChar(d.pop("quoteChar"))

        custom_metrics = cast(List[str], d.pop("customMetrics"))

        create_pull_request_for_chart_fields_body = cls(
            quote_char=quote_char,
            custom_metrics=custom_metrics,
        )

        create_pull_request_for_chart_fields_body.additional_properties = d
        return create_pull_request_for_chart_fields_body

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
