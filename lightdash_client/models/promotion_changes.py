from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.promotion_changes_charts_item import PromotionChangesChartsItem
    from ..models.promotion_changes_dashboards_item import (
        PromotionChangesDashboardsItem,
    )
    from ..models.promotion_changes_spaces_item import PromotionChangesSpacesItem


T = TypeVar("T", bound="PromotionChanges")


@_attrs_define
class PromotionChanges:
    """
    Attributes:
        charts (List['PromotionChangesChartsItem']):
        dashboards (List['PromotionChangesDashboardsItem']):
        spaces (List['PromotionChangesSpacesItem']):
    """

    charts: List["PromotionChangesChartsItem"]
    dashboards: List["PromotionChangesDashboardsItem"]
    spaces: List["PromotionChangesSpacesItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charts = []
        for charts_item_data in self.charts:
            charts_item = charts_item_data.to_dict()
            charts.append(charts_item)

        dashboards = []
        for dashboards_item_data in self.dashboards:
            dashboards_item = dashboards_item_data.to_dict()
            dashboards.append(dashboards_item)

        spaces = []
        for spaces_item_data in self.spaces:
            spaces_item = spaces_item_data.to_dict()
            spaces.append(spaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "charts": charts,
                "dashboards": dashboards,
                "spaces": spaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.promotion_changes_charts_item import PromotionChangesChartsItem
        from ..models.promotion_changes_dashboards_item import (
            PromotionChangesDashboardsItem,
        )
        from ..models.promotion_changes_spaces_item import PromotionChangesSpacesItem

        d = src_dict.copy()
        charts = []
        _charts = d.pop("charts")
        for charts_item_data in _charts:
            charts_item = PromotionChangesChartsItem.from_dict(charts_item_data)

            charts.append(charts_item)

        dashboards = []
        _dashboards = d.pop("dashboards")
        for dashboards_item_data in _dashboards:
            dashboards_item = PromotionChangesDashboardsItem.from_dict(dashboards_item_data)

            dashboards.append(dashboards_item)

        spaces = []
        _spaces = d.pop("spaces")
        for spaces_item_data in _spaces:
            spaces_item = PromotionChangesSpacesItem.from_dict(spaces_item_data)

            spaces.append(spaces_item)

        promotion_changes = cls(
            charts=charts,
            dashboards=dashboards,
            spaces=spaces,
        )

        promotion_changes.additional_properties = d
        return promotion_changes

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
