import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationBase")


@_attrs_define
class NotificationBase:
    """
    Attributes:
        viewed (bool):
        created_at (datetime.datetime):
        notification_id (str):
        url (Union[Unset, str]):
        message (Union[Unset, str]):
        resource_uuid (Union[Unset, str]):
    """

    viewed: bool
    created_at: datetime.datetime
    notification_id: str
    url: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    resource_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        viewed = self.viewed

        created_at = self.created_at.isoformat()

        notification_id = self.notification_id

        url = self.url

        message = self.message

        resource_uuid = self.resource_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "viewed": viewed,
                "createdAt": created_at,
                "notificationId": notification_id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if message is not UNSET:
            field_dict["message"] = message
        if resource_uuid is not UNSET:
            field_dict["resourceUuid"] = resource_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        viewed = d.pop("viewed")

        created_at = isoparse(d.pop("createdAt"))

        notification_id = d.pop("notificationId")

        url = d.pop("url", UNSET)

        message = d.pop("message", UNSET)

        resource_uuid = d.pop("resourceUuid", UNSET)

        notification_base = cls(
            viewed=viewed,
            created_at=created_at,
            notification_id=notification_id,
            url=url,
            message=message,
            resource_uuid=resource_uuid,
        )

        notification_base.additional_properties = d
        return notification_base

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
