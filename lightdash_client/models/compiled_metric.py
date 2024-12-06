from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compact import Compact
from ..models.compact_or_alias_type_1 import CompactOrAliasType1
from ..models.field_type_metric import FieldTypeMETRIC
from ..models.format_ import Format
from ..models.metric_type import MetricType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format import CustomFormat
    from ..models.default_time_dimension import DefaultTimeDimension
    from ..models.field_url import FieldUrl
    from ..models.metric_filter_rule import MetricFilterRule
    from ..models.record_string_record_string_string_or_string_array import RecordStringRecordStringStringOrStringArray
    from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray
    from ..models.source import Source


T = TypeVar("T", bound="CompiledMetric")


@_attrs_define
class CompiledMetric:
    """
    Attributes:
        field_type (FieldTypeMETRIC):
        type (MetricType):
        name (str):
        label (str):
        table (str):
        table_label (str):
        sql (str):
        hidden (bool):
        is_auto_generated (bool):
        compiled_sql (str):
        description (Union[Unset, str]):
        source (Union[Unset, Source]):
        compact (Union[Compact, CompactOrAliasType1, Unset]):
        round_ (Union[Unset, float]):
        format_ (Union[Unset, Format]):
        group_label (Union[Unset, str]):
        groups (Union[Unset, List[str]]):
        urls (Union[Unset, List['FieldUrl']]):
        index (Union[Unset, float]):
        tags (Union[Unset, List[str]]):
        show_underlying_values (Union[Unset, List[str]]):
        filters (Union[Unset, List['MetricFilterRule']]):
        percentile (Union[Unset, float]):
        format_options (Union[Unset, CustomFormat]):
        dimension_reference (Union[Unset, str]):
        required_attributes (Union[Unset, RecordStringStringOrStringArray]): Construct a type with a set of properties K
            of type T
        default_time_dimension (Union[Unset, DefaultTimeDimension]):
        tables_references (Union[Unset, List[str]]):
        tables_required_attributes (Union[Unset, RecordStringRecordStringStringOrStringArray]): Construct a type with a
            set of properties K of type T
    """

    field_type: FieldTypeMETRIC
    type: MetricType
    name: str
    label: str
    table: str
    table_label: str
    sql: str
    hidden: bool
    is_auto_generated: bool
    compiled_sql: str
    description: Union[Unset, str] = UNSET
    source: Union[Unset, "Source"] = UNSET
    compact: Union[Compact, CompactOrAliasType1, Unset] = UNSET
    round_: Union[Unset, float] = UNSET
    format_: Union[Unset, Format] = UNSET
    group_label: Union[Unset, str] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    urls: Union[Unset, List["FieldUrl"]] = UNSET
    index: Union[Unset, float] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    show_underlying_values: Union[Unset, List[str]] = UNSET
    filters: Union[Unset, List["MetricFilterRule"]] = UNSET
    percentile: Union[Unset, float] = UNSET
    format_options: Union[Unset, "CustomFormat"] = UNSET
    dimension_reference: Union[Unset, str] = UNSET
    required_attributes: Union[Unset, "RecordStringStringOrStringArray"] = UNSET
    default_time_dimension: Union[Unset, "DefaultTimeDimension"] = UNSET
    tables_references: Union[Unset, List[str]] = UNSET
    tables_required_attributes: Union[Unset, "RecordStringRecordStringStringOrStringArray"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.custom_format import CustomFormat
        from ..models.default_time_dimension import DefaultTimeDimension
        from ..models.field_url import FieldUrl
        from ..models.metric_filter_rule import MetricFilterRule
        from ..models.record_string_record_string_string_or_string_array import (
            RecordStringRecordStringStringOrStringArray,
        )
        from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray
        from ..models.source import Source

        field_type = self.field_type.value

        type = self.type.value

        name = self.name

        label = self.label

        table = self.table

        table_label = self.table_label

        sql = self.sql

        hidden = self.hidden

        is_auto_generated = self.is_auto_generated

        compiled_sql = self.compiled_sql

        description = self.description

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        compact: Union[Unset, str]
        if isinstance(self.compact, Unset):
            compact = UNSET
        elif isinstance(self.compact, Compact):
            compact = self.compact.value
        else:
            compact = self.compact.value

        round_ = self.round_

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        group_label = self.group_label

        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        urls: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.urls, Unset):
            urls = []
            for urls_item_data in self.urls:
                urls_item = urls_item_data.to_dict()
                urls.append(urls_item)

        index = self.index

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        show_underlying_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.show_underlying_values, Unset):
            show_underlying_values = self.show_underlying_values

        filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        percentile = self.percentile

        format_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_options, Unset):
            format_options = self.format_options.to_dict()

        dimension_reference = self.dimension_reference

        required_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.required_attributes, Unset):
            required_attributes = self.required_attributes.to_dict()

        default_time_dimension: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_time_dimension, Unset):
            default_time_dimension = self.default_time_dimension.to_dict()

        tables_references: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tables_references, Unset):
            tables_references = self.tables_references

        tables_required_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tables_required_attributes, Unset):
            tables_required_attributes = self.tables_required_attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldType": field_type,
                "type": type,
                "name": name,
                "label": label,
                "table": table,
                "tableLabel": table_label,
                "sql": sql,
                "hidden": hidden,
                "isAutoGenerated": is_auto_generated,
                "compiledSql": compiled_sql,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if compact is not UNSET:
            field_dict["compact"] = compact
        if round_ is not UNSET:
            field_dict["round"] = round_
        if format_ is not UNSET:
            field_dict["format"] = format_
        if group_label is not UNSET:
            field_dict["groupLabel"] = group_label
        if groups is not UNSET:
            field_dict["groups"] = groups
        if urls is not UNSET:
            field_dict["urls"] = urls
        if index is not UNSET:
            field_dict["index"] = index
        if tags is not UNSET:
            field_dict["tags"] = tags
        if show_underlying_values is not UNSET:
            field_dict["showUnderlyingValues"] = show_underlying_values
        if filters is not UNSET:
            field_dict["filters"] = filters
        if percentile is not UNSET:
            field_dict["percentile"] = percentile
        if format_options is not UNSET:
            field_dict["formatOptions"] = format_options
        if dimension_reference is not UNSET:
            field_dict["dimensionReference"] = dimension_reference
        if required_attributes is not UNSET:
            field_dict["requiredAttributes"] = required_attributes
        if default_time_dimension is not UNSET:
            field_dict["defaultTimeDimension"] = default_time_dimension
        if tables_references is not UNSET:
            field_dict["tablesReferences"] = tables_references
        if tables_required_attributes is not UNSET:
            field_dict["tablesRequiredAttributes"] = tables_required_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_format import CustomFormat
        from ..models.default_time_dimension import DefaultTimeDimension
        from ..models.field_url import FieldUrl
        from ..models.metric_filter_rule import MetricFilterRule
        from ..models.record_string_record_string_string_or_string_array import (
            RecordStringRecordStringStringOrStringArray,
        )
        from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray
        from ..models.source import Source

        d = src_dict.copy()
        field_type = FieldTypeMETRIC(d.pop("fieldType"))

        type = MetricType(d.pop("type"))

        name = d.pop("name")

        label = d.pop("label")

        table = d.pop("table")

        table_label = d.pop("tableLabel")

        sql = d.pop("sql")

        hidden = d.pop("hidden")

        is_auto_generated = d.pop("isAutoGenerated")

        compiled_sql = d.pop("compiledSql")

        description = d.pop("description", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, Source]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = Source.from_dict(_source)

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

        round_ = d.pop("round", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, Format]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = Format(_format_)

        group_label = d.pop("groupLabel", UNSET)

        groups = cast(List[str], d.pop("groups", UNSET))

        urls = []
        _urls = d.pop("urls", UNSET)
        for urls_item_data in _urls or []:
            urls_item = FieldUrl.from_dict(urls_item_data)

            urls.append(urls_item)

        index = d.pop("index", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        show_underlying_values = cast(List[str], d.pop("showUnderlyingValues", UNSET))

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = MetricFilterRule.from_dict(filters_item_data)

            filters.append(filters_item)

        percentile = d.pop("percentile", UNSET)

        _format_options = d.pop("formatOptions", UNSET)
        format_options: Union[Unset, CustomFormat]
        if isinstance(_format_options, Unset):
            format_options = UNSET
        else:
            format_options = CustomFormat.from_dict(_format_options)

        dimension_reference = d.pop("dimensionReference", UNSET)

        _required_attributes = d.pop("requiredAttributes", UNSET)
        required_attributes: Union[Unset, RecordStringStringOrStringArray]
        if isinstance(_required_attributes, Unset):
            required_attributes = UNSET
        else:
            required_attributes = RecordStringStringOrStringArray.from_dict(_required_attributes)

        _default_time_dimension = d.pop("defaultTimeDimension", UNSET)
        default_time_dimension: Union[Unset, DefaultTimeDimension]
        if isinstance(_default_time_dimension, Unset):
            default_time_dimension = UNSET
        else:
            default_time_dimension = DefaultTimeDimension.from_dict(_default_time_dimension)

        tables_references = cast(List[str], d.pop("tablesReferences", UNSET))

        _tables_required_attributes = d.pop("tablesRequiredAttributes", UNSET)
        tables_required_attributes: Union[Unset, RecordStringRecordStringStringOrStringArray]
        if isinstance(_tables_required_attributes, Unset):
            tables_required_attributes = UNSET
        else:
            tables_required_attributes = RecordStringRecordStringStringOrStringArray.from_dict(
                _tables_required_attributes
            )

        compiled_metric = cls(
            field_type=field_type,
            type=type,
            name=name,
            label=label,
            table=table,
            table_label=table_label,
            sql=sql,
            hidden=hidden,
            is_auto_generated=is_auto_generated,
            compiled_sql=compiled_sql,
            description=description,
            source=source,
            compact=compact,
            round_=round_,
            format_=format_,
            group_label=group_label,
            groups=groups,
            urls=urls,
            index=index,
            tags=tags,
            show_underlying_values=show_underlying_values,
            filters=filters,
            percentile=percentile,
            format_options=format_options,
            dimension_reference=dimension_reference,
            required_attributes=required_attributes,
            default_time_dimension=default_time_dimension,
            tables_references=tables_references,
            tables_required_attributes=tables_required_attributes,
        )

        compiled_metric.additional_properties = d
        return compiled_metric

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
