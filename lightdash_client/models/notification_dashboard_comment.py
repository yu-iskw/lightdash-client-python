import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_notification_resource_type_dashboard_comments import (
    ApiNotificationResourceTypeDashboardComments,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_dashboard_tile_comment_metadata import (
        NotificationDashboardTileCommentMetadata,
    )


T = TypeVar("T", bound="NotificationDashboardComment")


@_attrs_define
class NotificationDashboardComment:
    """
    Attributes:
        viewed (bool):
        created_at (datetime.datetime):
        notification_id (str):
        resource_type (ApiNotificationResourceTypeDashboardComments):
        url (Union[Unset, str]):
        message (Union[Unset, str]):
        resource_uuid (Union[Unset, str]):
        metadata (Union[Unset, NotificationDashboardTileCommentMetadata]):
    """

    viewed: bool
    created_at: datetime.datetime
    notification_id: str
    resource_type: ApiNotificationResourceTypeDashboardComments
    url: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    resource_uuid: Union[Unset, str] = UNSET
    metadata: Union[Unset, "NotificationDashboardTileCommentMetadata"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        viewed = self.viewed

        created_at = self.created_at.isoformat()

        notification_id = self.notification_id

        resource_type = self.resource_type.value

        url = self.url

        message = self.message

        resource_uuid = self.resource_uuid

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "viewed": viewed,
                "createdAt": created_at,
                "notificationId": notification_id,
                "resourceType": resource_type,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if message is not UNSET:
            field_dict["message"] = message
        if resource_uuid is not UNSET:
            field_dict["resourceUuid"] = resource_uuid
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_dashboard_tile_comment_metadata import (
            NotificationDashboardTileCommentMetadata,
        )

        d = src_dict.copy()
        viewed = d.pop("viewed")

        created_at = isoparse(d.pop("createdAt"))

        notification_id = d.pop("notificationId")

        resource_type = ApiNotificationResourceTypeDashboardComments(d.pop("resourceType"))

        url = d.pop("url", UNSET)

        message = d.pop("message", UNSET)

        resource_uuid = d.pop("resourceUuid", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, NotificationDashboardTileCommentMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NotificationDashboardTileCommentMetadata.from_dict(_metadata)

        notification_dashboard_comment = cls(
            viewed=viewed,
            created_at=created_at,
            notification_id=notification_id,
            resource_type=resource_type,
            url=url,
            message=message,
            resource_uuid=resource_uuid,
            metadata=metadata,
        )

        notification_dashboard_comment.additional_properties = d
        return notification_dashboard_comment

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
