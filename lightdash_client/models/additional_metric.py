from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.compact import Compact
from ..models.compact_or_alias_type_1 import CompactOrAliasType1
from ..models.format_ import Format
from ..models.metric_type import MetricType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_filter_rule import MetricFilterRule


T = TypeVar("T", bound="AdditionalMetric")


@attr.s(auto_attribs=True)
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
        uuid (Union[Unset, None, str]):
        percentile (Union[Unset, float]):
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
    uuid: Union[Unset, None, str] = UNSET
    percentile: Union[Unset, float] = UNSET

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
        uuid = self.uuid
        percentile = self.percentile

        field_dict: Dict[str, Any] = {}
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        uuid = d.pop("uuid", UNSET)

        percentile = d.pop("percentile", UNSET)

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
        )

        return additional_metric
