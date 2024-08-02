from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compact import Compact
from ..models.compact_or_alias_type_1 import CompactOrAliasType1
from ..models.custom_format_type import CustomFormatType
from ..models.number_separator import NumberSeparator
from ..models.time_frames import TimeFrames
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFormat")


@_attrs_define
class CustomFormat:
    """
    Attributes:
        type (CustomFormatType):
        round_ (Union[Unset, float]):
        separator (Union[Unset, NumberSeparator]):
        currency (Union[Unset, str]):
        compact (Union[Compact, CompactOrAliasType1, Unset]):
        prefix (Union[Unset, str]):
        suffix (Union[Unset, str]):
        time_interval (Union[Unset, TimeFrames]):
    """

    type: CustomFormatType
    round_: Union[Unset, float] = UNSET
    separator: Union[Unset, NumberSeparator] = UNSET
    currency: Union[Unset, str] = UNSET
    compact: Union[Compact, CompactOrAliasType1, Unset] = UNSET
    prefix: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET
    time_interval: Union[Unset, TimeFrames] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        round_ = self.round_

        separator: Union[Unset, str] = UNSET
        if not isinstance(self.separator, Unset):
            separator = self.separator.value

        currency = self.currency

        compact: Union[Unset, str]
        if isinstance(self.compact, Unset):
            compact = UNSET
        elif isinstance(self.compact, Compact):
            compact = self.compact.value
        else:
            compact = self.compact.value

        prefix = self.prefix

        suffix = self.suffix

        time_interval: Union[Unset, str] = UNSET
        if not isinstance(self.time_interval, Unset):
            time_interval = self.time_interval.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if round_ is not UNSET:
            field_dict["round"] = round_
        if separator is not UNSET:
            field_dict["separator"] = separator
        if currency is not UNSET:
            field_dict["currency"] = currency
        if compact is not UNSET:
            field_dict["compact"] = compact
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if time_interval is not UNSET:
            field_dict["timeInterval"] = time_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CustomFormatType(d.pop("type"))

        round_ = d.pop("round", UNSET)

        _separator = d.pop("separator", UNSET)
        separator: Union[Unset, NumberSeparator]
        if isinstance(_separator, Unset):
            separator = UNSET
        else:
            separator = NumberSeparator(_separator)

        currency = d.pop("currency", UNSET)

        def _parse_compact(data: object) -> Union[Compact, CompactOrAliasType1, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_compact_or_alias_type_0 = Compact(data)

                return componentsschemas_compact_or_alias_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            componentsschemas_compact_or_alias_type_1 = CompactOrAliasType1(data)

            return componentsschemas_compact_or_alias_type_1

        compact = _parse_compact(d.pop("compact", UNSET))

        prefix = d.pop("prefix", UNSET)

        suffix = d.pop("suffix", UNSET)

        _time_interval = d.pop("timeInterval", UNSET)
        time_interval: Union[Unset, TimeFrames]
        if isinstance(_time_interval, Unset):
            time_interval = UNSET
        else:
            time_interval = TimeFrames(_time_interval)

        custom_format = cls(
            type=type,
            round_=round_,
            separator=separator,
            currency=currency,
            compact=compact,
            prefix=prefix,
            suffix=suffix,
            time_interval=time_interval,
        )

        custom_format.additional_properties = d
        return custom_format

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
