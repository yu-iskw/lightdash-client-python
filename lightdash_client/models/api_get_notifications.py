from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_get_notifications_status import ApiGetNotificationsStatus

if TYPE_CHECKING:
    from ..models.notification_dashboard_comment import NotificationDashboardComment


T = TypeVar("T", bound="ApiGetNotifications")


@_attrs_define
class ApiGetNotifications:
    """
    Attributes:
        results (List['NotificationDashboardComment']):
        status (ApiGetNotificationsStatus):
    """

    results: List["NotificationDashboardComment"]
    status: ApiGetNotificationsStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = []
        for componentsschemas_api_notifications_results_item_data in self.results:
            componentsschemas_api_notifications_results_item = (
                componentsschemas_api_notifications_results_item_data.to_dict()
            )
            results.append(componentsschemas_api_notifications_results_item)

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
        from ..models.notification_dashboard_comment import NotificationDashboardComment

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for componentsschemas_api_notifications_results_item_data in _results:
            componentsschemas_api_notifications_results_item = NotificationDashboardComment.from_dict(
                componentsschemas_api_notifications_results_item_data
            )

            results.append(componentsschemas_api_notifications_results_item)

        status = ApiGetNotificationsStatus(d.pop("status"))

        api_get_notifications = cls(
            results=results,
            status=status,
        )

        api_get_notifications.additional_properties = d
        return api_get_notifications

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
