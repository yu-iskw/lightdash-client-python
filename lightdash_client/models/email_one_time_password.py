import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="EmailOneTimePassword")


@_attrs_define
class EmailOneTimePassword:
    """
    Attributes:
        number_of_attempts (float): Number of times the passcode has been attempted
        created_at (datetime.datetime): Time that the passcode was created
    """

    number_of_attempts: float
    created_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number_of_attempts = self.number_of_attempts

        created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numberOfAttempts": number_of_attempts,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number_of_attempts = d.pop("numberOfAttempts")

        created_at = isoparse(d.pop("createdAt"))

        email_one_time_password = cls(
            number_of_attempts=number_of_attempts,
            created_at=created_at,
        )

        email_one_time_password.additional_properties = d
        return email_one_time_password

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
