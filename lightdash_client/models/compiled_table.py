from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_fields_by_strategy import OrderFieldsByStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_filter_rule import MetricFilterRule
    from ..models.record_string_compiled_dimension import RecordStringCompiledDimension
    from ..models.record_string_compiled_metric import RecordStringCompiledMetric
    from ..models.record_string_group_type import RecordStringGroupType
    from ..models.record_string_lineage_node_dependency_array import (
        RecordStringLineageNodeDependencyArray,
    )
    from ..models.record_string_string_or_string_array import (
        RecordStringStringOrStringArray,
    )
    from ..models.source import Source


T = TypeVar("T", bound="CompiledTable")


@_attrs_define
class CompiledTable:
    """
    Attributes:
        sql_table (str):
        schema (str):
        database (str):
        label (str):
        name (str):
        lineage_graph (RecordStringLineageNodeDependencyArray): Construct a type with a set of properties K of type T
        metrics (RecordStringCompiledMetric): Construct a type with a set of properties K of type T
        dimensions (RecordStringCompiledDimension): Construct a type with a set of properties K of type T
        group_details (Union[Unset, RecordStringGroupType]): Construct a type with a set of properties K of type T
        required_attributes (Union[Unset, RecordStringStringOrStringArray]): Construct a type with a set of properties K
            of type T
        hidden (Union[Unset, bool]):
        required_filters (Union[Unset, List['MetricFilterRule']]):
        sql_where (Union[Unset, str]):
        group_label (Union[Unset, str]):
        order_fields_by (Union[Unset, OrderFieldsByStrategy]):
        description (Union[Unset, str]):
        original_name (Union[Unset, str]):
        source (Union[Unset, Source]):
    """

    sql_table: str
    schema: str
    database: str
    label: str
    name: str
    lineage_graph: "RecordStringLineageNodeDependencyArray"
    metrics: "RecordStringCompiledMetric"
    dimensions: "RecordStringCompiledDimension"
    group_details: Union[Unset, "RecordStringGroupType"] = UNSET
    required_attributes: Union[Unset, "RecordStringStringOrStringArray"] = UNSET
    hidden: Union[Unset, bool] = UNSET
    required_filters: Union[Unset, List["MetricFilterRule"]] = UNSET
    sql_where: Union[Unset, str] = UNSET
    group_label: Union[Unset, str] = UNSET
    order_fields_by: Union[Unset, OrderFieldsByStrategy] = UNSET
    description: Union[Unset, str] = UNSET
    original_name: Union[Unset, str] = UNSET
    source: Union[Unset, "Source"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sql_table = self.sql_table

        schema = self.schema

        database = self.database

        label = self.label

        name = self.name

        lineage_graph = self.lineage_graph.to_dict()

        metrics = self.metrics.to_dict()

        dimensions = self.dimensions.to_dict()

        group_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_details, Unset):
            group_details = self.group_details.to_dict()

        required_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.required_attributes, Unset):
            required_attributes = self.required_attributes.to_dict()

        hidden = self.hidden

        required_filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.required_filters, Unset):
            required_filters = []
            for required_filters_item_data in self.required_filters:
                required_filters_item = required_filters_item_data.to_dict()
                required_filters.append(required_filters_item)

        sql_where = self.sql_where

        group_label = self.group_label

        order_fields_by: Union[Unset, str] = UNSET
        if not isinstance(self.order_fields_by, Unset):
            order_fields_by = self.order_fields_by.value

        description = self.description

        original_name = self.original_name

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sqlTable": sql_table,
                "schema": schema,
                "database": database,
                "label": label,
                "name": name,
                "lineageGraph": lineage_graph,
                "metrics": metrics,
                "dimensions": dimensions,
            }
        )
        if group_details is not UNSET:
            field_dict["groupDetails"] = group_details
        if required_attributes is not UNSET:
            field_dict["requiredAttributes"] = required_attributes
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if required_filters is not UNSET:
            field_dict["requiredFilters"] = required_filters
        if sql_where is not UNSET:
            field_dict["sqlWhere"] = sql_where
        if group_label is not UNSET:
            field_dict["groupLabel"] = group_label
        if order_fields_by is not UNSET:
            field_dict["orderFieldsBy"] = order_fields_by
        if description is not UNSET:
            field_dict["description"] = description
        if original_name is not UNSET:
            field_dict["originalName"] = original_name
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metric_filter_rule import MetricFilterRule
        from ..models.record_string_compiled_dimension import (
            RecordStringCompiledDimension,
        )
        from ..models.record_string_compiled_metric import RecordStringCompiledMetric
        from ..models.record_string_group_type import RecordStringGroupType
        from ..models.record_string_lineage_node_dependency_array import (
            RecordStringLineageNodeDependencyArray,
        )
        from ..models.record_string_string_or_string_array import (
            RecordStringStringOrStringArray,
        )
        from ..models.source import Source

        d = src_dict.copy()
        sql_table = d.pop("sqlTable")

        schema = d.pop("schema")

        database = d.pop("database")

        label = d.pop("label")

        name = d.pop("name")

        lineage_graph = RecordStringLineageNodeDependencyArray.from_dict(d.pop("lineageGraph"))

        metrics = RecordStringCompiledMetric.from_dict(d.pop("metrics"))

        dimensions = RecordStringCompiledDimension.from_dict(d.pop("dimensions"))

        _group_details = d.pop("groupDetails", UNSET)
        group_details: Union[Unset, RecordStringGroupType]
        if isinstance(_group_details, Unset):
            group_details = UNSET
        else:
            group_details = RecordStringGroupType.from_dict(_group_details)

        _required_attributes = d.pop("requiredAttributes", UNSET)
        required_attributes: Union[Unset, RecordStringStringOrStringArray]
        if isinstance(_required_attributes, Unset):
            required_attributes = UNSET
        else:
            required_attributes = RecordStringStringOrStringArray.from_dict(_required_attributes)

        hidden = d.pop("hidden", UNSET)

        required_filters = []
        _required_filters = d.pop("requiredFilters", UNSET)
        for required_filters_item_data in _required_filters or []:
            required_filters_item = MetricFilterRule.from_dict(required_filters_item_data)

            required_filters.append(required_filters_item)

        sql_where = d.pop("sqlWhere", UNSET)

        group_label = d.pop("groupLabel", UNSET)

        _order_fields_by = d.pop("orderFieldsBy", UNSET)
        order_fields_by: Union[Unset, OrderFieldsByStrategy]
        if isinstance(_order_fields_by, Unset):
            order_fields_by = UNSET
        else:
            order_fields_by = OrderFieldsByStrategy(_order_fields_by)

        description = d.pop("description", UNSET)

        original_name = d.pop("originalName", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, Source]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = Source.from_dict(_source)

        compiled_table = cls(
            sql_table=sql_table,
            schema=schema,
            database=database,
            label=label,
            name=name,
            lineage_graph=lineage_graph,
            metrics=metrics,
            dimensions=dimensions,
            group_details=group_details,
            required_attributes=required_attributes,
            hidden=hidden,
            required_filters=required_filters,
            sql_where=sql_where,
            group_label=group_label,
            order_fields_by=order_fields_by,
            description=description,
            original_name=original_name,
            source=source,
        )

        compiled_table.additional_properties = d
        return compiled_table

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
