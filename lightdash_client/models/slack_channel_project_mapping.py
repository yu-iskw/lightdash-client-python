from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlackChannelProjectMapping")


@_attrs_define
class SlackChannelProjectMapping:
    """
    Attributes:
        available_tags (Union[List[str], None]):
        slack_channel_id (str):
        project_uuid (str):
    """

    available_tags: Union[List[str], None]
    slack_channel_id: str
    project_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_tags: Union[List[str], None]
        if isinstance(self.available_tags, list):
            available_tags = self.available_tags

        else:
            available_tags = self.available_tags

        slack_channel_id = self.slack_channel_id

        project_uuid = self.project_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availableTags": available_tags,
                "slackChannelId": slack_channel_id,
                "projectUuid": project_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_available_tags(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                available_tags_type_0 = cast(List[str], data)

                return available_tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        available_tags = _parse_available_tags(d.pop("availableTags"))

        slack_channel_id = d.pop("slackChannelId")

        project_uuid = d.pop("projectUuid")

        slack_channel_project_mapping = cls(
            available_tags=available_tags,
            slack_channel_id=slack_channel_id,
            project_uuid=project_uuid,
        )

        slack_channel_project_mapping.additional_properties = d
        return slack_channel_project_mapping

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
