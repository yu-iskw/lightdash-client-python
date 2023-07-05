from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_email_verification_status_response_200_results_otp import (
        GetEmailVerificationStatusResponse200ResultsOtp,
    )


T = TypeVar("T", bound="GetEmailVerificationStatusResponse200Results")


@attr.s(auto_attribs=True)
class GetEmailVerificationStatusResponse200Results:
    """Verification status of an email address

    Attributes:
        is_verified (bool):
        email (str):
        otp (Union[Unset, GetEmailVerificationStatusResponse200ResultsOtp]): One time passcode information
            If there is no active passcode, this will be undefined
    """

    is_verified: bool
    email: str
    otp: Union[Unset, "GetEmailVerificationStatusResponse200ResultsOtp"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_verified = self.is_verified
        email = self.email
        otp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.otp, Unset):
            otp = self.otp.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isVerified": is_verified,
                "email": email,
            }
        )
        if otp is not UNSET:
            field_dict["otp"] = otp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_email_verification_status_response_200_results_otp import (
            GetEmailVerificationStatusResponse200ResultsOtp,
        )

        d = src_dict.copy()
        is_verified = d.pop("isVerified")

        email = d.pop("email")

        _otp = d.pop("otp", UNSET)
        otp: Union[Unset, GetEmailVerificationStatusResponse200ResultsOtp]
        if isinstance(_otp, Unset):
            otp = UNSET
        else:
            otp = GetEmailVerificationStatusResponse200ResultsOtp.from_dict(_otp)

        get_email_verification_status_response_200_results = cls(
            is_verified=is_verified,
            email=email,
            otp=otp,
        )

        get_email_verification_status_response_200_results.additional_properties = d
        return get_email_verification_status_response_200_results

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
