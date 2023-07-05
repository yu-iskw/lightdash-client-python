from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_email_status_response_results_otp import (
        ApiEmailStatusResponseResultsOtp,
    )


T = TypeVar("T", bound="ApiEmailStatusResponseResults")


@attr.s(auto_attribs=True)
class ApiEmailStatusResponseResults:
    """Verification status of an email address

    Attributes:
        is_verified (bool):
        email (str):
        otp (Union[Unset, ApiEmailStatusResponseResultsOtp]): One time passcode information
            If there is no active passcode, this will be undefined
    """

    is_verified: bool
    email: str
    otp: Union[Unset, "ApiEmailStatusResponseResultsOtp"] = UNSET
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
        from ..models.api_email_status_response_results_otp import (
            ApiEmailStatusResponseResultsOtp,
        )

        d = src_dict.copy()
        is_verified = d.pop("isVerified")

        email = d.pop("email")

        _otp = d.pop("otp", UNSET)
        otp: Union[Unset, ApiEmailStatusResponseResultsOtp]
        if isinstance(_otp, Unset):
            otp = UNSET
        else:
            otp = ApiEmailStatusResponseResultsOtp.from_dict(_otp)

        api_email_status_response_results = cls(
            is_verified=is_verified,
            email=email,
            otp=otp,
        )

        api_email_status_response_results.additional_properties = d
        return api_email_status_response_results

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
