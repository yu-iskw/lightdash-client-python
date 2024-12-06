import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonalAccessToken")


@_attrs_define
class PersonalAccessToken:
    """
    Attributes:
        description (str):
        expires_at (Union[None, datetime.datetime]):
        rotated_at (Union[None, datetime.datetime]):
        last_used_at (Union[None, datetime.datetime]):
        created_at (datetime.datetime):
        uuid (str):
    """

    description: str
    expires_at: Union[None, datetime.datetime]
    rotated_at: Union[None, datetime.datetime]
    last_used_at: Union[None, datetime.datetime]
    created_at: datetime.datetime
    uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        expires_at: Union[None, str]
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        rotated_at: Union[None, str]
        if isinstance(self.rotated_at, datetime.datetime):
            rotated_at = self.rotated_at.isoformat()
        else:
            rotated_at = self.rotated_at

        last_used_at: Union[None, str]
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        created_at = self.created_at.isoformat()

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "expiresAt": expires_at,
                "rotatedAt": rotated_at,
                "lastUsedAt": last_used_at,
                "createdAt": created_at,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        def _parse_expires_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        def _parse_rotated_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rotated_at_type_0 = isoparse(data)

                return rotated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        rotated_at = _parse_rotated_at(d.pop("rotatedAt"))

        def _parse_last_used_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = isoparse(data)

                return last_used_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_used_at = _parse_last_used_at(d.pop("lastUsedAt"))

        created_at = isoparse(d.pop("createdAt"))

        uuid = d.pop("uuid")

        personal_access_token = cls(
            description=description,
            expires_at=expires_at,
            rotated_at=rotated_at,
            last_used_at=last_used_at,
            created_at=created_at,
            uuid=uuid,
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
