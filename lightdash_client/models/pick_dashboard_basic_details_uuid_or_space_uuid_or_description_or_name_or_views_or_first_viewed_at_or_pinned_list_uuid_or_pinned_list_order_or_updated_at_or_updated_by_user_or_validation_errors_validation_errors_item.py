import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar(
    "T",
    bound="PickDashboardBasicDetailsUuidOrSpaceUuidOrDescriptionOrNameOrViewsOrFirstViewedAtOrPinnedListUuidOrPinnedListOrderOrUpdatedAtOrUpdatedByUserOrValidationErrorsValidationErrorsItem",
)


@attr.s(auto_attribs=True)
class PickDashboardBasicDetailsUuidOrSpaceUuidOrDescriptionOrNameOrViewsOrFirstViewedAtOrPinnedListUuidOrPinnedListOrderOrUpdatedAtOrUpdatedByUserOrValidationErrorsValidationErrorsItem:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        validation_id (float):
        created_at (datetime.datetime):
        error (str):
    """

    validation_id: float
    created_at: datetime.datetime
    error: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        validation_id = self.validation_id
        created_at = self.created_at.isoformat()

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "validationId": validation_id,
                "createdAt": created_at,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        validation_id = d.pop("validationId")

        created_at = isoparse(d.pop("createdAt"))

        error = d.pop("error")

        pick_dashboard_basic_details_uuid_or_space_uuid_or_description_or_name_or_views_or_first_viewed_at_or_pinned_list_uuid_or_pinned_list_order_or_updated_at_or_updated_by_user_or_validation_errors_validation_errors_item = cls(
            validation_id=validation_id,
            created_at=created_at,
            error=error,
        )

        pick_dashboard_basic_details_uuid_or_space_uuid_or_description_or_name_or_views_or_first_viewed_at_or_pinned_list_uuid_or_pinned_list_order_or_updated_at_or_updated_by_user_or_validation_errors_validation_errors_item.additional_properties = (
            d
        )
        return pick_dashboard_basic_details_uuid_or_space_uuid_or_description_or_name_or_views_or_first_viewed_at_or_pinned_list_uuid_or_pinned_list_order_or_updated_at_or_updated_by_user_or_validation_errors_validation_errors_item

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
