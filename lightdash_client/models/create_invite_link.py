import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="CreateInviteLink")


@attr.s(auto_attribs=True)
class CreateInviteLink:
    """
    Attributes:
        expires_at (datetime.datetime):
    """

    expires_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expires_at = self.expires_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expires_at = isoparse(d.pop("expiresAt"))

        create_invite_link = cls(
            expires_at=expires_at,
        )

        create_invite_link.additional_properties = d
        return create_invite_link

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
