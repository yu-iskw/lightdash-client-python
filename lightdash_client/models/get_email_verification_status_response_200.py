from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.get_email_verification_status_response_200_status import (
    GetEmailVerificationStatusResponse200Status,
)

if TYPE_CHECKING:
    from ..models.get_email_verification_status_response_200_results import (
        GetEmailVerificationStatusResponse200Results,
    )


T = TypeVar("T", bound="GetEmailVerificationStatusResponse200")


@attr.s(auto_attribs=True)
class GetEmailVerificationStatusResponse200:
    """Shows the current verification status of an email address

    Attributes:
        results (GetEmailVerificationStatusResponse200Results): Verification status of an email address
        status (GetEmailVerificationStatusResponse200Status):
    """

    results: "GetEmailVerificationStatusResponse200Results"
    status: GetEmailVerificationStatusResponse200Status
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = self.results.to_dict()

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_email_verification_status_response_200_results import (
            GetEmailVerificationStatusResponse200Results,
        )

        d = src_dict.copy()
        results = GetEmailVerificationStatusResponse200Results.from_dict(d.pop("results"))

        status = GetEmailVerificationStatusResponse200Status(d.pop("status"))

        get_email_verification_status_response_200 = cls(
            results=results,
            status=status,
        )

        get_email_verification_status_response_200.additional_properties = d
        return get_email_verification_status_response_200

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
