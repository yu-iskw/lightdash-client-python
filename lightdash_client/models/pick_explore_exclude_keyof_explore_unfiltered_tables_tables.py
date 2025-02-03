from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compiled_table import CompiledTable


T = TypeVar("T", bound="PickExploreExcludeKeyofExploreUnfilteredTablesTables")


@_attrs_define
class PickExploreExcludeKeyofExploreUnfilteredTablesTables:
    """ """

    additional_properties: Dict[str, "CompiledTable"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.compiled_table import CompiledTable

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compiled_table import CompiledTable

        d = src_dict.copy()
        pick_explore_exclude_keyof_explore_unfiltered_tables_tables = cls()

        from ..models.default_time_dimension import DefaultTimeDimension
        from ..models.metric_filter_rule import MetricFilterRule
        from ..models.record_string_compiled_dimension import RecordStringCompiledDimension
        from ..models.record_string_compiled_metric import RecordStringCompiledMetric
        from ..models.record_string_group_type import RecordStringGroupType
        from ..models.record_string_lineage_node_dependency_array import RecordStringLineageNodeDependencyArray
        from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray
        from ..models.source import Source

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CompiledTable.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        pick_explore_exclude_keyof_explore_unfiltered_tables_tables.additional_properties = additional_properties
        return pick_explore_exclude_keyof_explore_unfiltered_tables_tables

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "CompiledTable":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "CompiledTable") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
