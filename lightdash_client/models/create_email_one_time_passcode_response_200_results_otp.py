import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="CreateEmailOneTimePasscodeResponse200ResultsOtp")


@attr.s(auto_attribs=True)
class CreateEmailOneTimePasscodeResponse200ResultsOtp:
    """One time passcode information
    If there is no active passcode, this will be undefined

        Attributes:
            number_of_attempts (float): Number of times the passcode has been attempted
            created_at (datetime.datetime): Time that the passcode was created
            is_max_attempts (bool):
            is_expired (bool):
            expires_at (datetime.datetime):
    """

    number_of_attempts: float
    created_at: datetime.datetime
    is_max_attempts: bool
    is_expired: bool
    expires_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number_of_attempts = self.number_of_attempts
        created_at = self.created_at.isoformat()

        is_max_attempts = self.is_max_attempts
        is_expired = self.is_expired
        expires_at = self.expires_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numberOfAttempts": number_of_attempts,
                "createdAt": created_at,
                "isMaxAttempts": is_max_attempts,
                "isExpired": is_expired,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number_of_attempts = d.pop("numberOfAttempts")

        created_at = isoparse(d.pop("createdAt"))

        is_max_attempts = d.pop("isMaxAttempts")

        is_expired = d.pop("isExpired")

        expires_at = isoparse(d.pop("expiresAt"))

        create_email_one_time_passcode_response_200_results_otp = cls(
            number_of_attempts=number_of_attempts,
            created_at=created_at,
            is_max_attempts=is_max_attempts,
            is_expired=is_expired,
            expires_at=expires_at,
        )

        create_email_one_time_passcode_response_200_results_otp.additional_properties = d
        return create_email_one_time_passcode_response_200_results_otp

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
