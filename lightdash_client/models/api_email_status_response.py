from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

import attr

from ..models.api_email_status_response_status import ApiEmailStatusResponseStatus

if TYPE_CHECKING:
    from ..models.api_email_status_response_results import ApiEmailStatusResponseResults


T = TypeVar("T", bound="ApiEmailStatusResponse")


@attr.s(auto_attribs=True)
class ApiEmailStatusResponse:
    """Shows the current verification status of an email address

    Attributes:
        results (ApiEmailStatusResponseResults): Verification status of an email address
        status (ApiEmailStatusResponseStatus):
    """

    results: "ApiEmailStatusResponseResults"
    status: ApiEmailStatusResponseStatus
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
        from ..models.api_email_status_response_results import ApiEmailStatusResponseResults

        d = src_dict.copy()
        results = ApiEmailStatusResponseResults.from_dict(d.pop("results"))

        status = ApiEmailStatusResponseStatus(d.pop("status"))

        api_email_status_response = cls(
            results=results,
            status=status,
        )

        api_email_status_response.additional_properties = d
        return api_email_status_response

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
