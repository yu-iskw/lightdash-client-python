import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="InviteLink")


@attr.s(auto_attribs=True)
class InviteLink:
    """
    Attributes:
        expires_at (datetime.datetime):
        invite_code (str):
        invite_url (str):
    """

    expires_at: datetime.datetime
    invite_code: str
    invite_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expires_at = self.expires_at.isoformat()

        invite_code = self.invite_code
        invite_url = self.invite_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiresAt": expires_at,
                "inviteCode": invite_code,
                "inviteUrl": invite_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expires_at = isoparse(d.pop("expiresAt"))

        invite_code = d.pop("inviteCode")

        invite_url = d.pop("inviteUrl")

        invite_link = cls(
            expires_at=expires_at,
            invite_code=invite_code,
            invite_url=invite_url,
        )

        invite_link.additional_properties = d
        return invite_link

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
