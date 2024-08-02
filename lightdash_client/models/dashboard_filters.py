from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dashboard_filter_rule import DashboardFilterRule


T = TypeVar("T", bound="DashboardFilters")


@_attrs_define
class DashboardFilters:
    """
    Attributes:
        table_calculations (List['DashboardFilterRule']):
        metrics (List['DashboardFilterRule']):
        dimensions (List['DashboardFilterRule']):
    """

    table_calculations: List["DashboardFilterRule"]
    metrics: List["DashboardFilterRule"]
    dimensions: List["DashboardFilterRule"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_calculations = []
        for table_calculations_item_data in self.table_calculations:
            table_calculations_item = table_calculations_item_data.to_dict()
            table_calculations.append(table_calculations_item)

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        dimensions = []
        for dimensions_item_data in self.dimensions:
            dimensions_item = dimensions_item_data.to_dict()
            dimensions.append(dimensions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableCalculations": table_calculations,
                "metrics": metrics,
                "dimensions": dimensions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_filter_rule import DashboardFilterRule

        d = src_dict.copy()
        table_calculations = []
        _table_calculations = d.pop("tableCalculations")
        for table_calculations_item_data in _table_calculations:
            table_calculations_item = DashboardFilterRule.from_dict(table_calculations_item_data)

            table_calculations.append(table_calculations_item)

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = DashboardFilterRule.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        dimensions = []
        _dimensions = d.pop("dimensions")
        for dimensions_item_data in _dimensions:
            dimensions_item = DashboardFilterRule.from_dict(dimensions_item_data)

            dimensions.append(dimensions_item)

        dashboard_filters = cls(
            table_calculations=table_calculations,
            metrics=metrics,
            dimensions=dimensions,
        )

        dashboard_filters.additional_properties = d
        return dashboard_filters

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
