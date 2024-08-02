import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_user import CommentUser


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        mentions (List[str]):
        can_remove (bool):
        resolved (bool):
        user (CommentUser):
        created_at (datetime.datetime):
        text_html (str):
        text (str):
        comment_id (str):
        replies (Union[Unset, List['Comment']]):
        reply_to (Union[Unset, str]):
    """

    mentions: List[str]
    can_remove: bool
    resolved: bool
    user: "CommentUser"
    created_at: datetime.datetime
    text_html: str
    text: str
    comment_id: str
    replies: Union[Unset, List["Comment"]] = UNSET
    reply_to: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mentions = self.mentions

        can_remove = self.can_remove

        resolved = self.resolved

        user = self.user.to_dict()

        created_at = self.created_at.isoformat()

        text_html = self.text_html

        text = self.text

        comment_id = self.comment_id

        replies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.replies, Unset):
            replies = []
            for replies_item_data in self.replies:
                replies_item = replies_item_data.to_dict()
                replies.append(replies_item)

        reply_to = self.reply_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mentions": mentions,
                "canRemove": can_remove,
                "resolved": resolved,
                "user": user,
                "createdAt": created_at,
                "textHtml": text_html,
                "text": text,
                "commentId": comment_id,
            }
        )
        if replies is not UNSET:
            field_dict["replies"] = replies
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment_user import CommentUser

        d = src_dict.copy()
        mentions = cast(List[str], d.pop("mentions"))

        can_remove = d.pop("canRemove")

        resolved = d.pop("resolved")

        user = CommentUser.from_dict(d.pop("user"))

        created_at = isoparse(d.pop("createdAt"))

        text_html = d.pop("textHtml")

        text = d.pop("text")

        comment_id = d.pop("commentId")

        replies = []
        _replies = d.pop("replies", UNSET)
        for replies_item_data in _replies or []:
            replies_item = Comment.from_dict(replies_item_data)

            replies.append(replies_item)

        reply_to = d.pop("replyTo", UNSET)

        comment = cls(
            mentions=mentions,
            can_remove=can_remove,
            resolved=resolved,
            user=user,
            created_at=created_at,
            text_html=text_html,
            text=text,
            comment_id=comment_id,
            replies=replies,
            reply_to=reply_to,
        )

        comment.additional_properties = d
        return comment

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
