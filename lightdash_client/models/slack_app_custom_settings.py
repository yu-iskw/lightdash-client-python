from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slack_channel_project_mapping import SlackChannelProjectMapping


T = TypeVar("T", bound="SlackAppCustomSettings")


@_attrs_define
class SlackAppCustomSettings:
    """
    Attributes:
        app_profile_photo_url (Union[None, str]):
        notification_channel (Union[None, str]):
        slack_channel_project_mappings (Union[Unset, List['SlackChannelProjectMapping']]):
    """

    app_profile_photo_url: Union[None, str]
    notification_channel: Union[None, str]
    slack_channel_project_mappings: Union[Unset, List["SlackChannelProjectMapping"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_profile_photo_url: Union[None, str]
        app_profile_photo_url = self.app_profile_photo_url

        notification_channel: Union[None, str]
        notification_channel = self.notification_channel

        slack_channel_project_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.slack_channel_project_mappings, Unset):
            slack_channel_project_mappings = []
            for slack_channel_project_mappings_item_data in self.slack_channel_project_mappings:
                slack_channel_project_mappings_item = slack_channel_project_mappings_item_data.to_dict()
                slack_channel_project_mappings.append(slack_channel_project_mappings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appProfilePhotoUrl": app_profile_photo_url,
                "notificationChannel": notification_channel,
            }
        )
        if slack_channel_project_mappings is not UNSET:
            field_dict["slackChannelProjectMappings"] = slack_channel_project_mappings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.slack_channel_project_mapping import SlackChannelProjectMapping

        d = src_dict.copy()

        def _parse_app_profile_photo_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        app_profile_photo_url = _parse_app_profile_photo_url(d.pop("appProfilePhotoUrl"))

        def _parse_notification_channel(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        notification_channel = _parse_notification_channel(d.pop("notificationChannel"))

        slack_channel_project_mappings = []
        _slack_channel_project_mappings = d.pop("slackChannelProjectMappings", UNSET)
        for slack_channel_project_mappings_item_data in _slack_channel_project_mappings or []:
            slack_channel_project_mappings_item = SlackChannelProjectMapping.from_dict(
                slack_channel_project_mappings_item_data
            )

            slack_channel_project_mappings.append(slack_channel_project_mappings_item)

        slack_app_custom_settings = cls(
            app_profile_photo_url=app_profile_photo_url,
            notification_channel=notification_channel,
            slack_channel_project_mappings=slack_channel_project_mappings,
        )

        slack_app_custom_settings.additional_properties = d
        return slack_app_custom_settings

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
