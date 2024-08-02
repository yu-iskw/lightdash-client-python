from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_pinned_items_status import ApiPinnedItemsStatus

if TYPE_CHECKING:
    from ..models.resource_view_chart_item import ResourceViewChartItem
    from ..models.resource_view_dashboard_item import ResourceViewDashboardItem
    from ..models.resource_view_space_item import ResourceViewSpaceItem


T = TypeVar("T", bound="ApiPinnedItems")


@_attrs_define
class ApiPinnedItems:
    """
    Attributes:
        results (List[Union['ResourceViewChartItem', 'ResourceViewDashboardItem', 'ResourceViewSpaceItem']]):
        status (ApiPinnedItemsStatus):
    """

    results: List[Union["ResourceViewChartItem", "ResourceViewDashboardItem", "ResourceViewSpaceItem"]]
    status: ApiPinnedItemsStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.resource_view_chart_item import ResourceViewChartItem
        from ..models.resource_view_dashboard_item import ResourceViewDashboardItem

        results = []
        for componentsschemas_pinned_items_item_data in self.results:
            componentsschemas_pinned_items_item: Dict[str, Any]
            if isinstance(componentsschemas_pinned_items_item_data, ResourceViewDashboardItem):
                componentsschemas_pinned_items_item = componentsschemas_pinned_items_item_data.to_dict()
            elif isinstance(componentsschemas_pinned_items_item_data, ResourceViewChartItem):
                componentsschemas_pinned_items_item = componentsschemas_pinned_items_item_data.to_dict()
            else:
                componentsschemas_pinned_items_item = componentsschemas_pinned_items_item_data.to_dict()

            results.append(componentsschemas_pinned_items_item)

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resource_view_chart_item import ResourceViewChartItem
        from ..models.resource_view_dashboard_item import ResourceViewDashboardItem
        from ..models.resource_view_space_item import ResourceViewSpaceItem

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for componentsschemas_pinned_items_item_data in _results:

            def _parse_componentsschemas_pinned_items_item(
                data: object,
            ) -> Union["ResourceViewChartItem", "ResourceViewDashboardItem", "ResourceViewSpaceItem"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_pinned_items_item_type_0 = ResourceViewDashboardItem.from_dict(data)

                    return componentsschemas_pinned_items_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_pinned_items_item_type_1 = ResourceViewChartItem.from_dict(data)

                    return componentsschemas_pinned_items_item_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_pinned_items_item_type_2 = ResourceViewSpaceItem.from_dict(data)

                return componentsschemas_pinned_items_item_type_2

            componentsschemas_pinned_items_item = _parse_componentsschemas_pinned_items_item(
                componentsschemas_pinned_items_item_data
            )

            results.append(componentsschemas_pinned_items_item)

        status = ApiPinnedItemsStatus(d.pop("status"))

        api_pinned_items = cls(
            results=results,
            status=status,
        )

        api_pinned_items.additional_properties = d
        return api_pinned_items

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
