from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickCommentTextOrReplyToOrMentionsOrTextHtml")


@_attrs_define
class PickCommentTextOrReplyToOrMentionsOrTextHtml:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        text (str):
        mentions (List[str]):
        text_html (str):
        reply_to (Union[Unset, str]):
    """

    text: str
    mentions: List[str]
    text_html: str
    reply_to: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        mentions = self.mentions

        text_html = self.text_html

        reply_to = self.reply_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "mentions": mentions,
                "textHtml": text_html,
            }
        )
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        mentions = cast(List[str], d.pop("mentions"))

        text_html = d.pop("textHtml")

        reply_to = d.pop("replyTo", UNSET)

        pick_comment_text_or_reply_to_or_mentions_or_text_html = cls(
            text=text,
            mentions=mentions,
            text_html=text_html,
            reply_to=reply_to,
        )

        pick_comment_text_or_reply_to_or_mentions_or_text_html.additional_properties = d
        return pick_comment_text_or_reply_to_or_mentions_or_text_html

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
