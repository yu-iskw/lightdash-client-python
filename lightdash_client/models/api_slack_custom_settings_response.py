from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_slack_custom_settings_response_status import ApiSlackCustomSettingsResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSlackCustomSettingsResponse")


@_attrs_define
class ApiSlackCustomSettingsResponse:
    """
    Attributes:
        results (Any):
        status (ApiSlackCustomSettingsResponseStatus):
    """

    results: Any
    status: ApiSlackCustomSettingsResponseStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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

        status = ApiSlackCustomSettingsResponseStatus(d.pop("status"))

        api_slack_custom_settings_response = cls(
            results=results,
            status=status,
        )

        api_slack_custom_settings_response.additional_properties = d
        return api_slack_custom_settings_response

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
