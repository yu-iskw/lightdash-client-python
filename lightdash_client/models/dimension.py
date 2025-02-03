from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compact import Compact
from ..models.compact_or_alias_type_1 import CompactOrAliasType1
from ..models.dimension_type import DimensionType
from ..models.field_type_dimension import FieldTypeDIMENSION
from ..models.format_ import Format
from ..models.time_frames import TimeFrames
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_url import FieldUrl
    from ..models.record_string_string import RecordStringString
    from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray
    from ..models.source import Source


T = TypeVar("T", bound="Dimension")


@_attrs_define
class Dimension:
    """
    Attributes:
        field_type (FieldTypeDIMENSION):
        type (DimensionType):
        name (str):
        label (str):
        table (str):
        table_label (str):
        sql (str):
        hidden (bool):
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
        group (Union[Unset, str]):
        required_attributes (Union[Unset, RecordStringStringOrStringArray]): Construct a type with a set of properties K
            of type T
        time_interval (Union[Unset, TimeFrames]):
        time_interval_base_dimension_name (Union[Unset, str]):
        is_additional_dimension (Union[Unset, bool]):
        colors (Union[Unset, RecordStringString]): Construct a type with a set of properties K of type T
        is_interval_base (Union[Unset, bool]):
    """

    field_type: FieldTypeDIMENSION
    type: DimensionType
    name: str
    label: str
    table: str
    table_label: str
    sql: str
    hidden: bool
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
    group: Union[Unset, str] = UNSET
    required_attributes: Union[Unset, "RecordStringStringOrStringArray"] = UNSET
    time_interval: Union[Unset, TimeFrames] = UNSET
    time_interval_base_dimension_name: Union[Unset, str] = UNSET
    is_additional_dimension: Union[Unset, bool] = UNSET
    colors: Union[Unset, "RecordStringString"] = UNSET
    is_interval_base: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.field_url import FieldUrl
        from ..models.record_string_string import RecordStringString
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

        group = self.group

        required_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.required_attributes, Unset):
            required_attributes = self.required_attributes.to_dict()

        time_interval: Union[Unset, str] = UNSET
        if not isinstance(self.time_interval, Unset):
            time_interval = self.time_interval.value

        time_interval_base_dimension_name = self.time_interval_base_dimension_name

        is_additional_dimension = self.is_additional_dimension

        colors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.colors, Unset):
            colors = self.colors.to_dict()

        is_interval_base = self.is_interval_base

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
        if group is not UNSET:
            field_dict["group"] = group
        if required_attributes is not UNSET:
            field_dict["requiredAttributes"] = required_attributes
        if time_interval is not UNSET:
            field_dict["timeInterval"] = time_interval
        if time_interval_base_dimension_name is not UNSET:
            field_dict["timeIntervalBaseDimensionName"] = time_interval_base_dimension_name
        if is_additional_dimension is not UNSET:
            field_dict["isAdditionalDimension"] = is_additional_dimension
        if colors is not UNSET:
            field_dict["colors"] = colors
        if is_interval_base is not UNSET:
            field_dict["isIntervalBase"] = is_interval_base

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.field_url import FieldUrl
        from ..models.record_string_string import RecordStringString
        from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray
        from ..models.source import Source

        d = src_dict.copy()
        field_type = FieldTypeDIMENSION(d.pop("fieldType"))

        type = DimensionType(d.pop("type"))

        name = d.pop("name")

        label = d.pop("label")

        table = d.pop("table")

        table_label = d.pop("tableLabel")

        sql = d.pop("sql")

        hidden = d.pop("hidden")

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

        group = d.pop("group", UNSET)

        _required_attributes = d.pop("requiredAttributes", UNSET)
        required_attributes: Union[Unset, RecordStringStringOrStringArray]
        if isinstance(_required_attributes, Unset):
            required_attributes = UNSET
        else:
            required_attributes = RecordStringStringOrStringArray.from_dict(_required_attributes)

        _time_interval = d.pop("timeInterval", UNSET)
        time_interval: Union[Unset, TimeFrames]
        if isinstance(_time_interval, Unset):
            time_interval = UNSET
        else:
            time_interval = TimeFrames(_time_interval)

        time_interval_base_dimension_name = d.pop("timeIntervalBaseDimensionName", UNSET)

        is_additional_dimension = d.pop("isAdditionalDimension", UNSET)

        _colors = d.pop("colors", UNSET)
        colors: Union[Unset, RecordStringString]
        if isinstance(_colors, Unset):
            colors = UNSET
        else:
            colors = RecordStringString.from_dict(_colors)

        is_interval_base = d.pop("isIntervalBase", UNSET)

        dimension = cls(
            field_type=field_type,
            type=type,
            name=name,
            label=label,
            table=table,
            table_label=table_label,
            sql=sql,
            hidden=hidden,
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
            group=group,
            required_attributes=required_attributes,
            time_interval=time_interval,
            time_interval_base_dimension_name=time_interval_base_dimension_name,
            is_additional_dimension=is_additional_dimension,
            colors=colors,
            is_interval_base=is_interval_base,
        )

        dimension.additional_properties = d
        return dimension

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
