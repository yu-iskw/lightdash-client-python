from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compact import Compact
from ..models.compact_or_alias_type_1 import CompactOrAliasType1
from ..models.format_ import Format
from ..models.metric_type import MetricType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format import CustomFormat
    from ..models.metric_filter_rule import MetricFilterRule


T = TypeVar("T", bound="AdditionalMetric")


@_attrs_define
class AdditionalMetric:
    """
    Attributes:
        type (MetricType):
        sql (str):
        table (str):
        name (str):
        label (Union[Unset, str]):
        description (Union[Unset, str]):
        hidden (Union[Unset, bool]):
        round_ (Union[Unset, float]):
        compact (Union[Compact, CompactOrAliasType1, Unset]):
        format_ (Union[Unset, Format]):
        index (Union[Unset, float]):
        filters (Union[Unset, List['MetricFilterRule']]):
        base_dimension_name (Union[Unset, str]):
        uuid (Union[None, Unset, str]):
        percentile (Union[Unset, float]):
        format_options (Union[Unset, CustomFormat]):
    """

    type: MetricType
    sql: str
    table: str
    name: str
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    round_: Union[Unset, float] = UNSET
    compact: Union[Compact, CompactOrAliasType1, Unset] = UNSET
    format_: Union[Unset, Format] = UNSET
    index: Union[Unset, float] = UNSET
    filters: Union[Unset, List["MetricFilterRule"]] = UNSET
    base_dimension_name: Union[Unset, str] = UNSET
    uuid: Union[None, Unset, str] = UNSET
    percentile: Union[Unset, float] = UNSET
    format_options: Union[Unset, "CustomFormat"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        sql = self.sql

        table = self.table

        name = self.name

        label = self.label

        description = self.description

        hidden = self.hidden

        round_ = self.round_

        compact: Union[Unset, str]
        if isinstance(self.compact, Unset):
            compact = UNSET
        elif isinstance(self.compact, Compact):
            compact = self.compact.value
        else:
            compact = self.compact.value

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        index = self.index

        filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        base_dimension_name = self.base_dimension_name

        uuid: Union[None, Unset, str]
        if isinstance(self.uuid, Unset):
            uuid = UNSET
        else:
            uuid = self.uuid

        percentile = self.percentile

        format_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_options, Unset):
            format_options = self.format_options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "sql": sql,
                "table": table,
                "name": name,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if round_ is not UNSET:
            field_dict["round"] = round_
        if compact is not UNSET:
            field_dict["compact"] = compact
        if format_ is not UNSET:
            field_dict["format"] = format_
        if index is not UNSET:
            field_dict["index"] = index
        if filters is not UNSET:
            field_dict["filters"] = filters
        if base_dimension_name is not UNSET:
            field_dict["baseDimensionName"] = base_dimension_name
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if percentile is not UNSET:
            field_dict["percentile"] = percentile
        if format_options is not UNSET:
            field_dict["formatOptions"] = format_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_format import CustomFormat
        from ..models.metric_filter_rule import MetricFilterRule

        d = src_dict.copy()
        type = MetricType(d.pop("type"))

        sql = d.pop("sql")

        table = d.pop("table")

        name = d.pop("name")

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        round_ = d.pop("round", UNSET)

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

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, Format]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = Format(_format_)

        index = d.pop("index", UNSET)

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = MetricFilterRule.from_dict(filters_item_data)

            filters.append(filters_item)

        base_dimension_name = d.pop("baseDimensionName", UNSET)

        def _parse_uuid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        uuid = _parse_uuid(d.pop("uuid", UNSET))

        percentile = d.pop("percentile", UNSET)

        _format_options = d.pop("formatOptions", UNSET)
        format_options: Union[Unset, CustomFormat]
        if isinstance(_format_options, Unset):
            format_options = UNSET
        else:
            format_options = CustomFormat.from_dict(_format_options)

        additional_metric = cls(
            type=type,
            sql=sql,
            table=table,
            name=name,
            label=label,
            description=description,
            hidden=hidden,
            round_=round_,
            compact=compact,
            format_=format_,
            index=index,
            filters=filters,
            base_dimension_name=base_dimension_name,
            uuid=uuid,
            percentile=percentile,
            format_options=format_options,
        )

        additional_metric.additional_properties = d
        return additional_metric

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
