import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="PersonalAccessToken")


@attr.s(auto_attribs=True)
class PersonalAccessToken:
    """
    Attributes:
        created_at (datetime.datetime):
        description (str):
        uuid (Union[Unset, str]):
        token (Union[Unset, str]):
        expires_at (Union[Unset, None, datetime.datetime]):
    """

    created_at: datetime.datetime
    description: str
    uuid: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    expires_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description
        uuid = self.uuid
        token = self.token
        expires_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat() if self.expires_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "description": description,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if token is not UNSET:
            field_dict["token"] = token
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        description = d.pop("description")

        uuid = d.pop("uuid", UNSET)

        token = d.pop("token", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: Union[Unset, None, datetime.datetime]
        if _expires_at is None:
            expires_at = None
        elif isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        personal_access_token = cls(
            created_at=created_at,
            description=description,
            uuid=uuid,
            token=token,
            expires_at=expires_at,
        )

        personal_access_token.additional_properties = d
        return personal_access_token

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
