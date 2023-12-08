from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.compact import Compact
from ..models.number_separator import NumberSeparator
from ..models.table_calculation_format_type import TableCalculationFormatType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TableCalculationFormat")


@attr.s(auto_attribs=True)
class TableCalculationFormat:
    """
    Attributes:
        type (TableCalculationFormatType):
        suffix (Union[Unset, str]):
        prefix (Union[Unset, str]):
        compact (Union[Unset, Compact]):
        currency (Union[Unset, str]):
        separator (Union[Unset, NumberSeparator]):
        round_ (Union[Unset, float]):
    """

    type: TableCalculationFormatType
    suffix: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    compact: Union[Unset, Compact] = UNSET
    currency: Union[Unset, str] = UNSET
    separator: Union[Unset, NumberSeparator] = UNSET
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
        type = TableCalculationFormatType(d.pop("type"))

        suffix = d.pop("suffix", UNSET)

        prefix = d.pop("prefix", UNSET)

        _compact = d.pop("compact", UNSET)
        compact: Union[Unset, Compact]
        if isinstance(_compact, Unset):
            compact = UNSET
        else:
            compact = Compact(_compact)

        currency = d.pop("currency", UNSET)

        _separator = d.pop("separator", UNSET)
        separator: Union[Unset, NumberSeparator]
        if isinstance(_separator, Unset):
            separator = UNSET
        else:
            separator = NumberSeparator(_separator)

        round_ = d.pop("round", UNSET)

        table_calculation_format = cls(
            type=type,
            suffix=suffix,
            prefix=prefix,
            compact=compact,
            currency=currency,
            separator=separator,
            round_=round_,
        )

        table_calculation_format.additional_properties = d
        return table_calculation_format

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
