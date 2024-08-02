from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalculateTotalFromSavedChartBody")


@_attrs_define
class CalculateTotalFromSavedChartBody:
    """
    Attributes:
        invalidate_cache (Union[Unset, bool]):
        dashboard_filters (Union[Unset, Any]):
    """

    invalidate_cache: Union[Unset, bool] = UNSET
    dashboard_filters: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invalidate_cache = self.invalidate_cache

        dashboard_filters = self.dashboard_filters

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invalidate_cache is not UNSET:
            field_dict["invalidateCache"] = invalidate_cache
        if dashboard_filters is not UNSET:
            field_dict["dashboardFilters"] = dashboard_filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invalidate_cache = d.pop("invalidateCache", UNSET)

        dashboard_filters = d.pop("dashboardFilters", UNSET)

        calculate_total_from_saved_chart_body = cls(
            invalidate_cache=invalidate_cache,
            dashboard_filters=dashboard_filters,
        )

        calculate_total_from_saved_chart_body.additional_properties = d
        return calculate_total_from_saved_chart_body

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
