from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_item_category import ResourceItemCategory
from ..models.resource_view_item_type_dashboard import ResourceViewItemTypeDASHBOARD
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_dashboard_basic_details_uuid_or_space_uuid_or_description_or_name_or_views_or_first_viewed_at_or_pinned_list_uuid_or_pinned_list_order_or_updated_at_or_updated_by_user_or_validation_errors import (
        PickDashboardBasicDetailsUuidOrSpaceUuidOrDescriptionOrNameOrViewsOrFirstViewedAtOrPinnedListUuidOrPinnedListOrderOrUpdatedAtOrUpdatedByUserOrValidationErrors,
    )


T = TypeVar("T", bound="ResourceViewDashboardItem")


@_attrs_define
class ResourceViewDashboardItem:
    """
    Attributes:
        data (PickDashboardBasicDetailsUuidOrSpaceUuidOrDescriptionOrNameOrViewsOrFirstViewedAtOrPinnedListUuidOrPinnedL
            istOrderOrUpdatedAtOrUpdatedByUserOrValidationErrors): From T, pick a set of properties whose keys are in the
            union K
        type (ResourceViewItemTypeDASHBOARD):
        category (Union[Unset, ResourceItemCategory]):
    """

    data: "PickDashboardBasicDetailsUuidOrSpaceUuidOrDescriptionOrNameOrViewsOrFirstViewedAtOrPinnedListUuidOrPinnedListOrderOrUpdatedAtOrUpdatedByUserOrValidationErrors"
    type: ResourceViewItemTypeDASHBOARD
    category: Union[Unset, ResourceItemCategory] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        type = self.type.value

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "type": type,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_dashboard_basic_details_uuid_or_space_uuid_or_description_or_name_or_views_or_first_viewed_at_or_pinned_list_uuid_or_pinned_list_order_or_updated_at_or_updated_by_user_or_validation_errors import (
            PickDashboardBasicDetailsUuidOrSpaceUuidOrDescriptionOrNameOrViewsOrFirstViewedAtOrPinnedListUuidOrPinnedListOrderOrUpdatedAtOrUpdatedByUserOrValidationErrors,
        )

        d = src_dict.copy()
        data = PickDashboardBasicDetailsUuidOrSpaceUuidOrDescriptionOrNameOrViewsOrFirstViewedAtOrPinnedListUuidOrPinnedListOrderOrUpdatedAtOrUpdatedByUserOrValidationErrors.from_dict(
            d.pop("data")
        )

        type = ResourceViewItemTypeDASHBOARD(d.pop("type"))

        _category = d.pop("category", UNSET)
        category: Union[Unset, ResourceItemCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ResourceItemCategory(_category)

        resource_view_dashboard_item = cls(
            data=data,
            type=type,
            category=category,
        )

        resource_view_dashboard_item.additional_properties = d
        return resource_view_dashboard_item

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
