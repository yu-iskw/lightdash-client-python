from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.run_metric_query_json_body_table_calculations_item_format_compact import (
    RunMetricQueryJsonBodyTableCalculationsItemFormatCompact,
)
from ..models.run_metric_query_json_body_table_calculations_item_format_separator import (
    RunMetricQueryJsonBodyTableCalculationsItemFormatSeparator,
)
from ..models.run_metric_query_json_body_table_calculations_item_format_type import (
    RunMetricQueryJsonBodyTableCalculationsItemFormatType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunMetricQueryJsonBodyTableCalculationsItemFormat")


@attr.s(auto_attribs=True)
class RunMetricQueryJsonBodyTableCalculationsItemFormat:
    """
    Attributes:
        type (RunMetricQueryJsonBodyTableCalculationsItemFormatType):
        suffix (Union[Unset, str]):
        prefix (Union[Unset, str]):
        compact (Union[Unset, RunMetricQueryJsonBodyTableCalculationsItemFormatCompact]):
        currency (Union[Unset, str]):
        separator (Union[Unset, RunMetricQueryJsonBodyTableCalculationsItemFormatSeparator]):
        round_ (Union[Unset, float]):
    """

    type: RunMetricQueryJsonBodyTableCalculationsItemFormatType
    suffix: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    compact: Union[Unset, RunMetricQueryJsonBodyTableCalculationsItemFormatCompact] = UNSET
    currency: Union[Unset, str] = UNSET
    separator: Union[Unset, RunMetricQueryJsonBodyTableCalculationsItemFormatSeparator] = UNSET
    round_: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        suffix = self.suffix
        prefix = self.prefix
        compact: Union[Unset, str] = UNSET
        if not isinstance(self.compact, Unset):
            compact = self.compact.value

        currency = self.currency
        separator: Union[Unset, str] = UNSET
        if not isinstance(self.separator, Unset):
            separator = self.separator.value

        round_ = self.round_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if compact is not UNSET:
            field_dict["compact"] = compact
        if currency is not UNSET:
            field_dict["currency"] = currency
        if separator is not UNSET:
            field_dict["separator"] = separator
        if round_ is not UNSET:
            field_dict["round"] = round_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = RunMetricQueryJsonBodyTableCalculationsItemFormatType(d.pop("type"))

        suffix = d.pop("suffix", UNSET)

        prefix = d.pop("prefix", UNSET)

        _compact = d.pop("compact", UNSET)
        compact: Union[Unset, RunMetricQueryJsonBodyTableCalculationsItemFormatCompact]
        if isinstance(_compact, Unset):
            compact = UNSET
        else:
            compact = RunMetricQueryJsonBodyTableCalculationsItemFormatCompact(_compact)

        currency = d.pop("currency", UNSET)

        _separator = d.pop("separator", UNSET)
        separator: Union[Unset, RunMetricQueryJsonBodyTableCalculationsItemFormatSeparator]
        if isinstance(_separator, Unset):
            separator = UNSET
        else:
            separator = RunMetricQueryJsonBodyTableCalculationsItemFormatSeparator(_separator)

        round_ = d.pop("round", UNSET)

        run_metric_query_json_body_table_calculations_item_format = cls(
            type=type,
            suffix=suffix,
            prefix=prefix,
            compact=compact,
            currency=currency,
            separator=separator,
            round_=round_,
        )

        run_metric_query_json_body_table_calculations_item_format.additional_properties = d
        return run_metric_query_json_body_table_calculations_item_format

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
