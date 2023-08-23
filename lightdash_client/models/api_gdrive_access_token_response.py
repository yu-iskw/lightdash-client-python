from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_gdrive_access_token_response_status import (
    ApiGdriveAccessTokenResponseStatus,
)

T = TypeVar("T", bound="ApiGdriveAccessTokenResponse")


@attr.s(auto_attribs=True)
class ApiGdriveAccessTokenResponse:
    """
    Attributes:
        results (str):
        status (ApiGdriveAccessTokenResponseStatus):
    """

    results: str
    status: ApiGdriveAccessTokenResponseStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = self.results
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
        d = src_dict.copy()
        results = d.pop("results")

        status = ApiGdriveAccessTokenResponseStatus(d.pop("status"))

        api_gdrive_access_token_response = cls(
            results=results,
            status=status,
        )

        api_gdrive_access_token_response.additional_properties = d
        return api_gdrive_access_token_response

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
